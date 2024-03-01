import os
import sys
import subprocess
from colorama import init, Fore
from tqdm import tqdm

# Initialize colorama for colored text
init()

# ASCII art for SMAPI
ascii_art = """
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

# Path to the directory where the script resides
installer_dir = os.path.dirname(os.path.abspath(__file__))

# Check if running from within a zip folder
if 'TEMP' in installer_dir:
    print(Fore.RED + "Oops! It looks like you're running the installer from inside a zip file. "
                     "Please unzip the download first.")
    input()
    sys.exit()

# Check if necessary files exist
required_files = ["internal/windows/SMAPI.Installer.dll", "internal/windows/SMAPI.Installer.exe"]
missing_files = [file for file in required_files if not os.path.exists(os.path.join(installer_dir, file))]

if missing_files:
    print(Fore.RED + "Oops! SMAPI is missing some required files. Your antivirus might have deleted them.")
    for file in missing_files:
        print(Fore.RED + f"Missing file: {file}")
    input()
    sys.exit()

# Display ASCII art
print(Fore.MAGENTA + ascii_art)

# Start installer
print(Fore.MAGENTA + "Initializing SMAPI installation...")
with tqdm(total=100, desc="Progress", bar_format="{desc}: {percentage:.0f}% [{bar}]") as pbar:
    # Simulating installation progress
    for _ in range(100):
        pbar.update(1)

# Run installer
installer_exe_path = os.path.join(installer_dir, "internal/windows/SMAPI.Installer.exe")
try:
    subprocess.run([installer_exe_path], check=True)
    installation_success = True
except subprocess.CalledProcessError:
    installation_success = False

# Check installation success
if installation_success:
    print(Fore.GREEN + "SMAPI installed successfully!")
else:
    print(Fore.RED + "Oops! The SMAPI installer encountered an error. Please check the logs for details.")

input(Fore.YELLOW + "Press Enter to exit...")
