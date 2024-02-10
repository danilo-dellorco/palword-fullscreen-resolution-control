import subprocess
import time
import psutil
import configparser

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over all the running processes
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Read parameters from config.ini
def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    qres = config.get('Paths', 'QRes')
    palw = config.get('Paths', 'Palw')
    resolution_x = config.get('Resolution', 'ResXGame')
    resolution_y = config.get('Resolution', 'ResYGame')

    return qres, palw, resolution_x, resolution_y

if __name__ == "__main__":
    # Read parameters from config.ini
    qres, palw, resolution_x, resolution_y = read_config('config.ini')

    # Change resolution
    subprocess.run([qres, f"/x:{resolution_x}", f"/y:{resolution_y}"])

    # Start Palworld
    subprocess.run(["start", "/WAIT", "", palw], shell=True)

    # Wait for Palworld to start
    while not checkIfProcessRunning("Palworld-Win64-Shipping"):
        print("Waiting for Palworld to launch")
        time.sleep(2)

    # Wait for Palworld to close
    while checkIfProcessRunning("Palworld-Win64-Shipping"):
        print("Palworld Still Running")
        time.sleep(2)

    # Restore original resolution
    subprocess.run([qres, "/x:3840", "/y:2400"])
