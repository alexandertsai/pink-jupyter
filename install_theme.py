#!/usr/bin/env python3
"""
Pink Jupyter Theme Installer
Installs the pink theme for Jupyter Notebook
"""

import shutil
import sys
from pathlib import Path


def get_jupyter_config_dir():
    """Get the Jupyter configuration directory."""
    try:
        from jupyter_core.paths import jupyter_config_dir
        return Path(jupyter_config_dir())
    except ImportError:
        return Path.home() / ".jupyter"


def install_theme():
    """Install the pink theme to Jupyter's custom CSS directory."""
    # Get paths
    script_dir = Path(__file__).parent
    
    # Present theme options to user
    print("🌸 Pink Jupyter Theme Installation 🌸")
    print("\nChoose your theme version:")
    print("1. Nbclassic (Recommended!) - works with jupyter nbclassic")
    print("2. No nbclassic - works with jupyter notebook")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice == "1":
            theme_file = script_dir / "theme" / "custom.css"
            break
        elif choice == "2":
            theme_file = script_dir / "theme" / "custom_no_nbclassic.css"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
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