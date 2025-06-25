#!/usr/bin/env python3
"""
Pink Jupyter Theme Installer
Installs the pink theme for Jupyter Notebook
"""

import os
import shutil
import sys
from pathlib import Path


def get_jupyter_config_dir():
    """Get the Jupyter configuration directory."""
    try:
        from jupyter_core.paths import jupyter_config_dir
        return Path(jupyter_config_dir())
    except ImportError:
        # Fallback to default locations
        if sys.platform == "win32":
            return Path.home() / ".jupyter"
        else:
            return Path.home() / ".jupyter"


def install_theme():
    """Install the pink theme to Jupyter's custom CSS directory."""
    # Get paths
    script_dir = Path(__file__).parent
    theme_file = script_dir / "theme" / "custom.css"  # change this to custom_less.css if you only want nbclassic support (both versions include collapsible functionality)
    
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
    
    print("\n✨ Pink theme installed successfully!")
    print("\nTo use the theme:")
    print("1. Start or restart Jupyter Notebook")
    print("2. The pink theme will be applied automatically")
    print("\nTo uninstall:")
    print(f"- Delete {target_file}")
    print(f"- Or restore from backup: {custom_dir / 'custom.css.backup'}")
    
    return True


def uninstall_theme():
    """Uninstall the pink theme."""
    jupyter_dir = get_jupyter_config_dir()
    custom_dir = jupyter_dir / "custom"
    target_file = custom_dir / "custom.css"
    backup_file = custom_dir / "custom.css.backup"
    
    if not target_file.exists():
        print("No custom theme is currently installed.")
        return
    
    if backup_file.exists():
        print(f"Restoring original theme from {backup_file}")
        shutil.copy2(backup_file, target_file)
        backup_file.unlink()
    else:
        print(f"Removing theme file {target_file}")
        target_file.unlink()
    
    print("✨ Theme uninstalled successfully!")


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall_theme()
    else:
        install_theme()


if __name__ == "__main__":
    main()