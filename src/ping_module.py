import subprocess 

hostIP = "192.168.1.252"

def pingPC (hostIP):
    response = subprocess.run(['ping', '-c', '1', hostIP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0


