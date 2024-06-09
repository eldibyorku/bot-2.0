import subprocess


def focus():
    app_name = "PathOfExileClient"
    cmd = f'osascript -e \'activate application "{app_name}"\''
    subprocess.call(cmd, shell=True)

# # not working
# def minimize():
#     app_name = "PathOfExileClient"
#     cmd = f'osascript -e \'tell application "{app_name}" to set miniaturized of window 1 to true\''
#     subprocess.call(cmd, shell=True)
