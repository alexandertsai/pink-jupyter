#!/usr/bin/env python3
"""
Pink Jupyter Theme Installer
Installs the pink theme for Jupyter Notebook
"""

import shutil
import sys
import platform
from pathlib import Path


def get_jupyter_config_dir():
    """Get the Jupyter configuration directory."""
    try:
        from jupyter_core.paths import jupyter_config_dir
        return Path(jupyter_config_dir())
    except ImportError:
        return Path.home() / ".jupyter"


def setup_matplotlib_config(script_dir):
    """Setup matplotlib to use pink theme by default."""
    # Follow matplotlib's recommended user config locations
    if platform.system().lower() in ['linux', 'freebsd']:
        # Unix/Linux: ~/.config/matplotlib/matplotlibrc
        config_dir = Path.home() / ".config" / "matplotlib"
    else:
        # Other platforms: ~/.matplotlib/matplotlibrc  
        config_dir = Path.home() / ".matplotlib"
    
    config_dir.mkdir(parents=True, exist_ok=True)
    matplotlibrc_file = config_dir / "matplotlibrc"
    
    # Read pink.mplstyle contents
    pink_style_file = script_dir / "pink.mplstyle"
    if not pink_style_file.exists():
        print(f"Warning: pink.mplstyle not found at {pink_style_file}")
        return False
    
    # Read the pink style content
    with open(pink_style_file, 'r') as f:
        pink_content = f.read()
    
    # Check if matplotlibrc already exists
    if matplotlibrc_file.exists():
        # Read existing content
        with open(matplotlibrc_file, 'r') as f:
            existing_content = f.read()
        
        # Check if pink theme settings are already present
        if "# Pink Jupyter Theme - Matplotlib Style" in existing_content:
            print("Pink matplotlib configuration already present")
            return True
        
        # Backup existing matplotlibrc
        backup_file = config_dir / "matplotlibrc.backup"
        print(f"Backing up existing matplotlibrc to {backup_file}")
        shutil.copy2(matplotlibrc_file, backup_file)
        
        # Append pink configuration
        with open(matplotlibrc_file, 'a') as f:
            f.write("\n\n" + pink_content)
    else:
        # Create new matplotlibrc with pink configuration
        with open(matplotlibrc_file, 'w') as f:
            f.write(pink_content)
    
    print(f"Pink matplotlib configuration installed to {matplotlibrc_file}")
    return True


def setup_ipython_config():
    """Setup IPython to use SVG format for inline plots by default."""
    # Get IPython profile directory
    ipython_dir = Path.home() / ".ipython" / "profile_default" / "startup"
    ipython_dir.mkdir(parents=True, exist_ok=True)
    
    # Path to startup script
    startup_script = ipython_dir / "00-inline-svg.py"
    
    # SVG configuration script
    svg_script = """from IPython import get_ipython
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")"""
    
    # Check if script already exists
    if startup_script.exists():
        with open(startup_script, 'r') as f:
            existing_content = f.read()
        
        if "InlineBackend.figure_format = 'svg'" in existing_content:
            print("IPython SVG configuration already present")
            return True
        
        # Backup existing script
        backup_file = startup_script.with_suffix('.py.backup')
        print(f"Backing up existing startup script to {backup_file}")
        shutil.copy2(startup_script, backup_file)
    
    # Write SVG configuration
    with open(startup_script, 'w') as f:
        f.write(svg_script)
    
    print(f"IPython SVG configuration installed to {startup_script}")
    return True


def install_theme():
    """Install the pink theme to Jupyter's custom CSS directory."""
    # Get paths
    script_dir = Path(__file__).parent
    
    print("🌸 Pink Jupyter Theme Installation 🌸")
    
    # Use notebook.css as the default theme
    theme_file = script_dir / "theme" / "notebook.css"
    
    if not theme_file.exists():
        print(f"Error: Theme file not found at {theme_file}")
        return False
    
    # Get Jupyter config directory
    jupyter_dir = get_jupyter_config_dir()
    custom_dir = jupyter_dir / "custom"
    
    # Create custom directory if it doesn't exist
    custom_dir.mkdir(parents=True, exist_ok=True)
    
    # Backup existing custom.css if it exists
    target_file = custom_dir / "custom.css"
    if target_file.exists():
        backup_file = custom_dir / "custom.css.backup"
        print(f"Backing up existing custom.css to {backup_file}")
        shutil.copy2(target_file, backup_file)
    
    # Copy the theme file
    print(f"Installing pink theme to {target_file}")
    shutil.copy2(theme_file, target_file)
    
    print("\n✨ Pink theme CSS installed successfully!")
    
    # Setup matplotlib configuration
    print("\nSetting up matplotlib configuration...")
    matplotlib_success = setup_matplotlib_config(script_dir)
    
    # Setup IPython configuration
    print("\nSetting up IPython configuration...")
    ipython_success = setup_ipython_config()
    
    print("\n🌸 Complete Pink theme installation finished!")
    print("\nFeatures installed:")
    print("✓ Pink Jupyter notebook theme")
    if matplotlib_success:
        print("✓ Pink matplotlib plots by default")
    if ipython_success:
        print("✓ SVG figure format for crisp plots")
    
    print("\nTo use the theme:")
    print("1. Refresh or start Jupyter Notebook")
    print("2. The pink theme will be applied automatically")
    print("3. Matplotlib plots will use pink colors by default")
    print("4. Plots will render as crisp SVG images")
    
    print("\nTo uninstall:")
    print(f"- Run: python {Path(__file__).name} uninstall")
    
    return True


def uninstall_theme():
    """Uninstall the pink theme and related configurations."""
    print("🌸 Uninstalling Pink Jupyter Theme...")
    
    # Uninstall Jupyter CSS theme
    jupyter_dir = get_jupyter_config_dir()
    custom_dir = jupyter_dir / "custom"
    target_file = custom_dir / "custom.css"
    backup_file = custom_dir / "custom.css.backup"
    
    if target_file.exists():
        if backup_file.exists():
            print(f"Restoring original Jupyter theme from {backup_file}")
            shutil.copy2(backup_file, target_file)
            backup_file.unlink()
        else:
            print(f"Removing Jupyter theme file {target_file}")
            target_file.unlink()
        print("✓ Jupyter theme uninstalled")
    else:
        print("No Jupyter custom theme found to uninstall")
    
    # Uninstall matplotlib configuration from user config directories
    config_locations = []
    
    # Add platform-specific user config locations
    if platform.system().lower() in ['linux', 'freebsd']:
        config_locations.append(Path.home() / ".config" / "matplotlib")
    else:
        config_locations.append(Path.home() / ".matplotlib")
    
    matplotlib_uninstalled = False
    for config_dir in config_locations:
        matplotlibrc_file = config_dir / "matplotlibrc"
        if matplotlibrc_file.exists():
            # Check if it contains pink theme content
            with open(matplotlibrc_file, 'r') as f:
                content = f.read()
            
            if "# Pink Jupyter Theme - Matplotlib Style" in content:
                matplotlib_backup = config_dir / "matplotlibrc.backup"
                if matplotlib_backup.exists():
                    print(f"Restoring original matplotlib config from {matplotlib_backup}")
                    shutil.copy2(matplotlib_backup, matplotlibrc_file)
                    matplotlib_backup.unlink()
                else:
                    print(f"Removing matplotlib config {matplotlibrc_file}")
                    matplotlibrc_file.unlink()
                print("✓ Matplotlib configuration uninstalled")
                matplotlib_uninstalled = True
                break
    
    if not matplotlib_uninstalled:
        print("No pink matplotlib configuration found to uninstall")
    
    # Uninstall IPython startup script
    ipython_startup_script = Path.home() / ".ipython" / "profile_default" / "startup" / "00-inline-svg.py"
    ipython_backup = ipython_startup_script.with_suffix('.py.backup')
    
    if ipython_startup_script.exists():
        if ipython_backup.exists():
            print(f"Restoring original IPython startup script from {ipython_backup}")
            shutil.copy2(ipython_backup, ipython_startup_script)
            ipython_backup.unlink()
        else:
            print(f"Removing IPython startup script {ipython_startup_script}")
            ipython_startup_script.unlink()
        print("✓ IPython SVG configuration uninstalled")
    else:
        print("No IPython startup script found to uninstall")
    
    print("\n✨ Pink theme completely uninstalled!")
    print("Restart Jupyter and IPython to see changes take effect.")


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall_theme()
    else:
        install_theme()


if __name__ == "__main__":
    main()