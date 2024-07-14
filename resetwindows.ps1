# PowerShell script to automate the reset process with the "Remove everything" option

# Run the reset command and automatically select the "Remove everything" option
# Note: This script will work only on systems with Windows 10 or later

# Ensure we have administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Warning "You do not have Administrator rights to run this script!`nPlease re-run this script as an Administrator!"
    exit
}

# Start the reset process
Start-Process -FilePath "systemreset.exe" -ArgumentList "/factoryreset" -Wait

# Allow some time for the reset window to open
Start-Sleep -Seconds 5

# Automate the UI interaction to select "Remove everything"
# This part uses the SendKeys method to automate key presses
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("{TAB}")
Start-Sleep -Seconds 1
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

# This script will continue the process; you may need to add additional SendKeys commands
# to fully automate the reset process depending on additional prompts and confirmations.
