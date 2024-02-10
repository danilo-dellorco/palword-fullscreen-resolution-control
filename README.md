# Palworld Full Screen Resolution Control

## Introduction
Palworld currently does not support playing at resolutions lower than the default resolution of the monitor. This means that to play Palworld in full screen on high DPI displays, users often have to manually change the Windows resolution, launch Palworld, and then manually restore the original resolution afterward. This process can be cumbersome and time-consuming.

This script automates the process, allowing you to start Palworld and automatically set the desired resolution, and then restoring the original resolution when the game is closed. It provides a seamless experience by handling the resolution changes automatically, eliminating the need for manual intervention.

## Overview
This script enables playing Palworld in full screen at lower resolutions and automatically restores the original screen resolution after the game is closed. It also includes instructions to overwrite the Palworld shortcut with the one that changes the resolution, making it convenient to launch Palworld with the desired settings directly from the Start Menu.

## Components

### `config.ini`
The `config.ini` file is used to configure the behavior of the script. It allows you to specify the paths to the QRes and Palworld executables, as well as the desired resolutions for Palworld.

### `restore_res.bat` and `restore_res.py`
These scripts are responsible for restoring the original screen resolution after Palworld is closed. They are invoked automatically by `run_pal.py` to ensure that the screen resolution is reverted back to its original state.

### `run_pal.py` and `run_pal.bat`
These scripts are the main components of the resolution control system. `run_pal.py` is a Python script that automates the process of changing the screen resolution, launching Palworld, and monitoring Palworld's process until it is closed. `run_pal.bat` is a batch script that serves as a wrapper for `run_pal.py`, making it easier to execute the Python script.

## Prerequisites
- Python 3.x
- `psutil` library (install via `pip install psutil`)
- QRes utility (download and install from [QRes website](https://www.technipages.com/download-qres))

## Installation
1. Clone this repository to your local machine.
2. Install the required `psutil` library using pip: `pip install psutil`.
3. Download and install the QRes utility from the [QRes website](https://www.technipages.com/download-qres).
4. Customize the `config.ini` file to specify the paths to QRes and Palworld executables, as well as the desired resolution for Palworld.

## Usage
1. Customize the `config.ini` file with the appropriate paths and resolution settings.
2. Run the script by executing `python run_pal.py` in the command line.
3. The script will change the screen resolution, launch Palworld in full screen mode, and monitor Palworld's process until it is closed. Once Palworld is closed, the script will restore the original screen resolution.

## Overwriting Palworld Shortcut
You can overwrite the existing Palworld shortcut in the Start Menu with the one provided by this script to launch Palworld with the desired resolution settings directly from the Start Menu. Follow these steps:

1. Create a shortcut to `run_pal.bat`.
2. Copy the shortcut to `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam`.
3. Rename the shortcut to `Palworld` and change the icon via `Properties > Change Icon` in Windows.

## Recommended Location for ResolutionWrapper
While the cloned repository can be located anywhere, it is recommended to copy the `ResolutionWrapper` directory to `C:\Program Files (x86)\Steam\steamapps\common\Palworld\ResolutionWrapper` for easy access.

## Configuration
You can customize the behavior of the script by editing the `config.ini` file. Here's what each parameter represents:
- `QRes`: Path to the QRes executable.
- `Palw`: Path to the Palworld executable.
- `ResXOrig`: The original horizontal resolution of your screen.
- `ResYOrig`: The original vertical resolution of your screen.
- `ResXGame`: The horizontal resolution for Palworld.
- `ResYGame`: The vertical resolution for Palworld.

### Example `config.ini`
```ini
[Paths]
QRes = C:\Program Files\Qres\QRes.exe
Palw = steam://rungameid/1623730

[Resolution]
ResXOrig = 3840
ResYOrig = 2400
ResXGame = 1280
ResYGame = 800