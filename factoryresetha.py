import os
import shutil
import subprocess

# Define the path to the OneDrive folder
onedrive_path = os.path.expanduser('~/OneDrive')
backup_folder_name = 'Backups'  # Name of the folder where backups are stored
backup_folder_path = os.path.join(onedrive_path, backup_folder_name)

# Function to check and remove backups from OneDrive
def remove_onedrive_backups():
    if os.path.exists(backup_folder_path):
        print(f"Found backup folder at: {backup_folder_path}")
        try:
            shutil.rmtree(backup_folder_path)
            print("Backups removed successfully.")
        except Exception as e:
            print(f"Failed to remove backups: {e}")
    else:
        print("No backup folder found in OneDrive.")

# Function to reset Windows
def reset_windows():
    try:
        # Run the command to open the Reset this PC option in Windows
        subprocess.run('systemreset -factoryreset', check=True, shell=True)
        print("Reset process initiated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to initiate reset process: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to remove OneDrive backups
remove_onedrive_backups()

# Call the function to reset Windows
reset_windows()
