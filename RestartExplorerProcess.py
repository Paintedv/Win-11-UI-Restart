import subprocess


def restart_explorer():
    subprocess.run(['taskkill', '/f', '/im', 'explorer.exe'], shell=True)
    subprocess.run(['explorer.exe'], shell=True)


if __name__ == '__main__':
    restart_explorer()
