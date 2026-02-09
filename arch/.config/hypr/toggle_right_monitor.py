with open('hyprland.conf', 'r') as file:
    filedata = file.read()

if "HDMI-A-1, disable" in filedata:
    filedata = filedata.replace('monitor = HDMI-A-1, disable', 'monitor = HDMI-A-1, 2560x1440@144, 2560x0, auto')
else:
    filedata = filedata.replace('monitor = HDMI-A-1, 2560x1440@144, 2560x0, auto', 'monitor = HDMI-A-1, disable')

with open('hyprland.conf', 'w') as file:
    file.write(filedata)
