#!/usr/bin/env python3
"""Pink Jupyter Theme installer.

Installs (or removes) a Jupyter custom CSS, a matplotlib rc file, and an
IPython startup script that sets the inline backend to SVG.

Examples
--------

Interactive (recommended):
    python install_theme.py

Non-interactive, install the recommended Lab Light theme:
    python install_theme.py --theme lab-light --yes

Uninstall everything:
    python install_theme.py uninstall
"""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path

REPO_DIR = Path(__file__).parent.resolve()


# ─── Theme registry ─────────────────────────────────────────────────────────

@dataclass
class Theme:
    key: str            # CLI key, e.g. 'lab-light'
    label: str          # Human label
    css: str            # CSS file under theme/
    mplstyle: str       # mplstyle file at repo root
    description: str    # One-line description

THEMES: dict[str, Theme] = {
    'lab-light':  Theme('lab-light',  'Pink Light · Jupyter Lab',
                        'lablight.css',  'pinklight.mplstyle',
                        'Cream-pink page, card-style cells, polars/pandas table polish'),
    'lab-dark':   Theme('lab-dark',   'Pink Dark · Jupyter Lab',
                        'labdark.css',   'pinkdark.mplstyle',
                        'Dark-mode pink for JupyterLab'),
    'lab-sage':   Theme('lab-sage',   'Sage Blue Dark · Jupyter Lab',
                        'labsageblue.css', 'sageblue.mplstyle',
                        'A blue-green twist on the Lab dark theme'),
    'nb-light':   Theme('nb-light',   'Pink Light · Classic Notebook',
                        'notebooklight.css', 'pinklight.mplstyle',
                        'Classic Jupyter Notebook (legacy nbclassic)'),
    'nb-dark':    Theme('nb-dark',    'Pink Dark · Classic Notebook',
                        'notebookdark.css',  'pinkdark.mplstyle',
                        'Classic Jupyter Notebook dark mode'),
}

DEFAULT_THEME = 'lab-light'


# ─── Path helpers ───────────────────────────────────────────────────────────

def jupyter_config_dir() -> Path:
    """Resolve the Jupyter config directory (uses jupyter_core if available)."""
    try:
        from jupyter_core.paths import jupyter_config_dir as _j
        return Path(_j())
    except ImportError:
        return Path.home() / '.jupyter'


def matplotlib_config_dir() -> Path:
    """User-level matplotlibrc directory, per platform conventions."""
    if platform.system().lower() in ('linux', 'freebsd'):
        xdg = os.environ.get('XDG_CONFIG_HOME')
        return (Path(xdg) if xdg else Path.home() / '.config') / 'matplotlib'
    return Path.home() / '.matplotlib'


def ipython_startup_dir() -> Path:
    return Path.home() / '.ipython' / 'profile_default' / 'startup'


def _backup(path: Path) -> Path | None:
    """Copy `path` to `path.backup`, return backup path, or None if no source."""
    if not path.exists():
        return None
    backup = path.with_name(path.name + '.backup')
    shutil.copy2(path, backup)
    return backup


# ─── Install steps ──────────────────────────────────────────────────────────

def install_jupyter_css(theme: Theme) -> Path:
    src = REPO_DIR / 'theme' / theme.css
    if not src.exists():
        raise FileNotFoundError(f'CSS not found: {src}')
    dest_dir = jupyter_config_dir() / 'custom'
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / 'custom.css'
    if backup := _backup(dest):
        print(f'  • backed up existing CSS → {backup.name}')
    shutil.copy2(src, dest)
    print(f'  ✓ Jupyter CSS → {dest}')
    return dest


def install_matplotlibrc(theme: Theme, *, yes: bool) -> Path | None:
    src = REPO_DIR / theme.mplstyle
    if not src.exists():
        print(f'  · skipped matplotlibrc ({src.name} not found)')
        return None
    dest_dir = matplotlib_config_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / 'matplotlibrc'
    if dest.exists() and not yes:
        ans = input(f'  matplotlibrc exists at {dest}. Overwrite? [y/N] ').strip().lower()
        if ans not in ('y', 'yes'):
            print('  · skipped matplotlibrc')
            return None
    if backup := _backup(dest):
        print(f'  • backed up existing matplotlibrc → {backup.name}')
    shutil.copy2(src, dest)
    print(f'  ✓ matplotlibrc → {dest}')
    return dest


IPYTHON_SVG_SNIPPET = (
    "from IPython import get_ipython\n"
    "get_ipython().run_line_magic('config', \"InlineBackend.figure_format = 'svg'\")\n"
)


def install_ipython_svg() -> Path:
    dest_dir = ipython_startup_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / '00-inline-svg.py'
    if dest.exists():
        if "InlineBackend.figure_format = 'svg'" in dest.read_text():
            print(f'  · IPython SVG already configured ({dest.name})')
            return dest
        if backup := _backup(dest):
            print(f'  • backed up existing startup → {backup.name}')
    dest.write_text(IPYTHON_SVG_SNIPPET)
    print(f'  ✓ IPython SVG inline → {dest}')
    return dest


# ─── Uninstall steps ────────────────────────────────────────────────────────

def _restore_or_remove(path: Path, label: str) -> None:
    if not path.exists():
        print(f'  · no {label} found')
        return
    backup = path.with_name(path.name + '.backup')
    if backup.exists():
        shutil.copy2(backup, path)
        backup.unlink()
        print(f'  ✓ restored {label} from backup')
    else:
        path.unlink()
        print(f'  ✓ removed {label}')


def uninstall() -> None:
    print('\n🌸 Uninstalling Pink Jupyter Theme...\n')

    print('Jupyter CSS:')
    _restore_or_remove(jupyter_config_dir() / 'custom' / 'custom.css', 'custom.css')

    print('\nmatplotlibrc:')
    _restore_or_remove(matplotlib_config_dir() / 'matplotlibrc', 'matplotlibrc')

    print('\nIPython startup:')
    _restore_or_remove(ipython_startup_dir() / '00-inline-svg.py', '00-inline-svg.py')

    print('\n✨ Done. Restart Jupyter to see changes.\n')


# ─── CLI ────────────────────────────────────────────────────────────────────

def _print_themes() -> None:
    print('\nAvailable themes:')
    for i, t in enumerate(THEMES.values(), 1):
        marker = ' (recommended)' if t.key == DEFAULT_THEME else ''
        print(f'  {i}. {t.label}{marker}')
        print(f'     key: {t.key:<10}  · {t.description}')


def _prompt_choice() -> Theme:
    _print_themes()
    keys = list(THEMES.keys())
    while True:
        ans = input(f'\nChoose [1-{len(keys)}] (default 1): ').strip()
        if ans == '':
            return THEMES[DEFAULT_THEME]
        if ans.isdigit() and 1 <= int(ans) <= len(keys):
            return THEMES[keys[int(ans) - 1]]
        if ans in THEMES:
            return THEMES[ans]
        print('  invalid choice, try again')


def install(theme: Theme, *, yes: bool, no_mpl: bool, no_svg: bool) -> None:
    print(f'\n🌸 Installing: {theme.label}\n')

    print('Jupyter CSS:')
    install_jupyter_css(theme)

    if not no_mpl:
        print('\nmatplotlib:')
        install_matplotlibrc(theme, yes=yes)

    if not no_svg:
        print('\nIPython:')
        install_ipython_svg()

    is_lab = theme.key.startswith('lab-')
    launch = 'jupyter lab --custom-css' if is_lab else 'jupyter notebook'
    print(textwrap.dedent(f'''
        ✨ Installed!

        Next steps:
          1. Start Jupyter:  {launch}
          2. Open demo.ipynb to see the theme in action.
          3. Tweak ~/.jupyter/custom/custom.css to customize colors.

        To uninstall:  python install_theme.py uninstall
    '''))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog='install_theme.py',
        description='Install the Pink Jupyter theme (CSS + matplotlibrc + IPython SVG).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            Examples:
              python install_theme.py                      # interactive
              python install_theme.py --theme lab-light -y # non-interactive
              python install_theme.py uninstall            # remove everything
        '''),
    )
    p.add_argument('command', nargs='?', default='install',
                   choices=['install', 'uninstall', 'list'],
                   help='Action to perform (default: install)')
    p.add_argument('--theme', '-t', choices=list(THEMES.keys()),
                   help='Theme key (skips the interactive prompt)')
    p.add_argument('--yes', '-y', action='store_true',
                   help='Overwrite without asking (useful for CI)')
    p.add_argument('--no-mpl', action='store_true', help='Skip matplotlib config')
    p.add_argument('--no-svg', action='store_true', help='Skip IPython SVG inline backend')

    args = p.parse_args(argv)

    if args.command == 'uninstall':
        uninstall()
        return 0

    if args.command == 'list':
        _print_themes()
        return 0

    theme = THEMES[args.theme] if args.theme else _prompt_choice()
    install(theme, yes=args.yes, no_mpl=args.no_mpl, no_svg=args.no_svg)
    return 0


if __name__ == '__main__':
    sys.exit(main())
