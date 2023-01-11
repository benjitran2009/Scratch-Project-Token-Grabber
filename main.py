import scratchattach as scratch3 # login and grab project token
import getpass # hide password
import time # for sleeping

print("""
███████╗ ██████╗██████╗  █████╗ ████████╗ ██████╗██╗  ██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║
███████╗██║     ██████╔╝███████║   ██║   ██║     ███████║
╚════██║██║     ██╔══██╗██╔══██║   ██║   ██║     ██╔══██║
███████║╚██████╗██║  ██║██║  ██║   ██║   ╚██████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
                                                         Grabber
                Made by @benjitran2009
                Replit: @Ben3Coder
    Github: https://github.com/benjitran2009/ScratchGrabber/
""")

# Input Project ID
pid = int(input('Project ID: '))
# Input Username
u = input('Username: ')
# Input Password
p = getpass.getpass('Password: ')

# Login to Session
session = scratch3.login(u,p)

# Connect To Project
project = session.connect_project(pid)

while True:
    project.update()
    time.sleep(5)
    try:
        print(f"Project Token: "+str(project.project_token)+" || Load using turbowarp: https://turbowarp.org/"+str(pid)+"#?token="+str(project.project_token))
    except:
        print(f'Error ocurred while attempting to fetch project token')
