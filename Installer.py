import os
import subprocess
from colorama import init, Fore
from tqdm import tqdm

# Initialize colorama for colored text
init()

# ASCII art for SMAPI
SMAPi_ASCII = """
.-------.  ____     __  .-'''-. ,---.    ,---.   ____    .-------. .-./`)  
\  _(`)_ \ \   \   /  // _     \|    \  /    | .'  __ `. \  _(`)_ \\ .-.') 
| (_ o._)|  \  _. /  '(`' )/`--'|  ,  \/  ,  |/   '  \  \| (_ o._)|/ `-' \ 
|  (_,_) /   _( )_ .'(_ o _).   |  |\_   /|  ||___|  /  ||  (_,_) / `-'`"` 
|   '-.-'___(_ o _)'  (_,_). '. |  _( )_/ |  |   _.-`   ||   '-.-'  .---.  
|   |   |   |(_,_)'  .---.  \  :| (_ o _) |  |.'   _    ||   |      |   |  
|   |   |   `-'  /   \    `-'  ||  (_,_)  |  ||  _( )_  ||   |      |   |  
/   )    \      /     \       / |  |      |  |\ (_ o _) //   )      |   |  
`---'     `-..-'       `-...-'  '--'      '--' '.(_,_).' `---'      '---'  
"""

def print_error(message):
    """Print error message in red color"""
    print(Fore.RED + message)

def print_success(message):
    """Print success message in green color"""
    print(Fore.GREEN + message)

def print_warning(message):
    """Print warning message in yellow color"""
    print(Fore.YELLOW + message)

def print_menu():
    """Print menu text"""
    print(Fore.MAGENTA + "=" * 55)
    print(Fore.MAGENTA + "| {:^51} |".format("V1.0.1"))
    print(Fore.MAGENTA + "| {:^51} |".format("Change Log:"))
    print(Fore.MAGENTA + "| {:^51} |".format("Better Terminal UI"))
    print(Fore.MAGENTA + "| {:^51} |".format(""))
    print(Fore.MAGENTA + "=" * 55)

def run_installer(installer_exe_path):
    """Run SMAPI installer"""
    try:
        subprocess.run([installer_exe_path], check=True)
        print_success("SMAPI installed successfully!")
    except subprocess.CalledProcessError:
        print_error("Oops! The SMAPI installer encountered an error. Please check the logs for details.")

def main():
    print_menu()
    print(Fore.MAGENTA + SMAPi_ASCII)
    print(Fore.MAGENTA + "Initializing SMAPI installation...")
    
    # Prompt user to press Enter to continue
    input("Press Enter to begin the installation...")

    # Simulate installation progress
    with tqdm(total=100, desc="Progress", bar_format="{desc}: {percentage:.0f}% [{bar}]") as pbar:
        for _ in range(100):
            pbar.update(1)

    # Path to the directory where the script resides
    installer_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the SMAPI installer
    installer_exe_path = os.path.join(installer_dir, "internal/windows/SMAPI.Installer.exe")

    # Check if installer exists
    if not os.path.exists(installer_exe_path):
        print_error("Oops! SMAPI installer is missing. Please check your installation files.")
        return

    run_installer(installer_exe_path)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_warning("\nInstallation interrupted. Press Enter to exit...")
        input()
