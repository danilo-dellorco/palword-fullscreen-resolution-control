import win32api
import win32con
import configparser
import psutil
import subprocess
import time

RESOLUTION_MAP = {
    "4K": (3840, 2160),
    "2K": (2560, 1440),
    "1080p": (1920, 1080),
    "720p": (1280, 720)
}

def get_physical_primary_monitor_dimensions():
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    screen_width = dm.PelsWidth
    screen_height = dm.PelsHeight
    return screen_width, screen_height

def get_screen_ratio():
    screen_width, screen_height = get_physical_primary_monitor_dimensions()
    screen_ratio = screen_width / screen_height
    return screen_ratio

def map_screen_ratio_to_format(screen_ratio):
    ratio_map = {
        16 / 10: "16:10",
        16 / 9: "16:9",
        4 / 3: "4:3",
        5 / 4: "5:4",
        21 / 9: "21:9"
        # Aggiungi altri rapporti e formati se necessario
    }
    return ratio_map.get(screen_ratio, "Formato sconosciuto")

def calculate_resolutions():
    resolutions = {}
    
    for resolution_name, resolution in RESOLUTION_MAP.items():
        initial_width, initial_height = resolution
        
        # Calcola risoluzione per 16:9
        resolutions_169 = (initial_width, initial_height)
        
        # Calcola risoluzione per 16:10
        resolutions_1610 = (initial_width, initial_width / (16 / 10))
        
        # Calcola risoluzione per 4:3
        resolutions_43 = (initial_width, initial_width / (4 / 3))
        
        # Calcola risoluzione per 5:4
        resolutions_54 = (initial_width, initial_width / (5 / 4))
        
        # Calcola risoluzione per 21:9
        resolutions_219 = (initial_width, initial_width / (21 / 9))
        
        # Aggiungi le risoluzioni alla mappa
        resolutions[f"{resolution_name}_16:9"] = resolutions_169
        resolutions[f"{resolution_name}_16:10"] = resolutions_1610
        resolutions[f"{resolution_name}_4:3"] = resolutions_43
        resolutions[f"{resolution_name}_5:4"] = resolutions_54
        resolutions[f"{resolution_name}_21:9"] = resolutions_219
    
    return resolutions

# Read parameters from config.ini
def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    qres = config.get('Paths', 'QRes')
    palw = config.get('Paths', 'Palw')
    res = config.get("Resolution", "GameRes")
    
    return qres, palw, res

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

if __name__ == "__main__":
    qres, palw, res = read_config('config.ini')
    resolutions_map = calculate_resolutions()
    
    screen_ratio = get_screen_ratio()
    screen_format = map_screen_ratio_to_format(screen_ratio)
    
    target_res = resolutions_map[f'{res}_{screen_format}']
    
    origin_w, origin_h = get_physical_primary_monitor_dimensions()
    target_w, target_h = target_res[0], target_res[1]
    
    # Change resolution
    subprocess.run([qres, f"/x:{target_w}", f"/y:{target_h}"])
    
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
    subprocess.run([qres, f"/x:{origin_w}", f"/y:{origin_h}"])
