import subprocess
import configparser

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    qres = config.get('Paths', 'QRes')
    palw = config.get('Paths', 'Palworld')
    resolution_x = config.get('Resolution', 'ResXOrig')
    resolution_y = config.get('Resolution', 'ResYOrig')
    return qres, palw, resolution_x, resolution_y

if __name__ == "__main__":
    qres, palw, resolution_x, resolution_y = read_config('config.ini')
    subprocess.run([qres, f"/x:{resolution_x}", f"/y:{resolution_y}"])