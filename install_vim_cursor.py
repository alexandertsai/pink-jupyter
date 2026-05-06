#!/usr/bin/env python3
"""Pink Jupyter — jupyterlab-vim cursor add-on.

Appends `theme/vim.css` to your installed `~/.jupyter/custom/custom.css`
so the vim block cursor turns pink instead of the default green.

Run *after* `install_theme.py` has installed a theme.
Tested with `jupyterlab-vim==4.1.4`.

Examples
--------
    python install_vim_cursor.py            # add (or refresh) the block
    python install_vim_cursor.py --remove   # remove just the vim block
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_DIR = Path(__file__).parent.resolve()
VIM_CSS = REPO_DIR / 'theme' / 'vim.css'

START = '/* >>> pink-jupyter vim cursor (managed) >>> */'
END   = '/* <<< pink-jupyter vim cursor (managed) <<< */'

# Match a previously-inserted block, including a leading newline if present.
BLOCK_RE = re.compile(
    rf'\n*{re.escape(START)}.*?{re.escape(END)}\n*',
    flags=re.DOTALL,
)


def jupyter_custom_css() -> Path:
    try:
        from jupyter_core.paths import jupyter_config_dir
        cfg = Path(jupyter_config_dir())
    except ImportError:
        cfg = Path.home() / '.jupyter'
    return cfg / 'custom' / 'custom.css'


def install() -> int:
    target = jupyter_custom_css()
    if not target.exists():
        print(f'✗ no custom.css at {target}')
        print('  run `python install_theme.py` first to install a theme.')
        return 1
    if not VIM_CSS.exists():
        print(f'✗ missing add-on source: {VIM_CSS}')
        return 1

    block = f'\n\n{START}\n{VIM_CSS.read_text().rstrip()}\n{END}\n'
    current = target.read_text()
    new = BLOCK_RE.sub('\n', current).rstrip() + block

    if new == current:
        print(f'· already up to date ({target})')
        return 0

    target.write_text(new)
    action = 'updated' if BLOCK_RE.search(current) else 'added'
    print(f'✓ {action} vim cursor block in {target}')
    print('  reload JupyterLab in your browser (⌘⇧R) to see the change.')
    return 0


def remove() -> int:
    target = jupyter_custom_css()
    if not target.exists():
        print(f'· nothing to do ({target} not found)')
        return 0
    current = target.read_text()
    if not BLOCK_RE.search(current):
        print(f'· no vim cursor block found in {target}')
        return 0
    target.write_text(BLOCK_RE.sub('\n', current).rstrip() + '\n')
    print(f'✓ removed vim cursor block from {target}')
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog='install_vim_cursor.py',
        description='Add (or remove) a pink vim cursor on top of an installed Pink Jupyter theme.',
    )
    p.add_argument('--remove', action='store_true', help='remove the add-on instead of installing it')
    args = p.parse_args(argv)
    return remove() if args.remove else install()


if __name__ == '__main__':
    sys.exit(main())
