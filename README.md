#  Windows Wi-Fi Password Recovery

This Python utility allows you to find saved Wi-Fi passwords on your local Windows machine. If you have forgotten your Wi-Fi password, this script can retrieve it for you instantly.

##  Description
To find passwords for previously connected Wi-Fi networks manually, you usually need to execute two separate commands in the terminal. This program automates that process by running those commands using a Python script and displaying the results in a clean format.

> **Note:** This script only shows passwords for Wi-Fi networks that were **previously connected** to the system. This script **cannot** find Wi-Fi passwords for unknown networks or other nearby Wi-Fi networks you have never joined.

##  How it Works
The program utilizes the Python `subprocess` module to bridge the script with the Windows operating system. It executes two specific network shell (`netsh`) commands to extract data:

1. `netsh wlan show profiles`: This command is used to query the Windows registry for a list of all saved Wi-Fi profile names.
2. `netsh wlan show profile "NAME" key=clear`: Once a profile name is identified, this command retrieves the security settings. By including the `key=clear` parameter, the script forces Windows to display the password in plain text under the "Key Content" field.
