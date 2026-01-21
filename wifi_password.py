import subprocess
command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
profiles = [i.split(":")[1].strip() for i in command if "All User Profile" in i]

print("{:<30}|  {:<}".format("Wi-Fi Name", "Password"))
print("-" * 45)

for i in profiles:
    try:
        results = subprocess.check_output(f'netsh wlan show profile "{i}" key=clear', shell=True).decode('utf-8', errors='ignore').split('\n')
        
        results = [b.split(":")[1].strip() for b in results if "Key Content" in b]
        
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
            
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(i, "Error: Could not read profile"))

input("\nFinished! Press Enter to close...")
