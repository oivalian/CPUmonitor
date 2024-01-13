# CPUmonitor

## What is CPUmonitor?
CPUmonitor displays basic system information through tkinker GUI such as:

1) Device Details (Name, OS and version)
2) CPU information (Brand, load, speed, cores/core breakdown)
3) Memory (installed, available and used)
4) Mounted Drives (Mounted letter, Type, Size)
5) Nvidia GPU Information (Brand, memory, load, temp)

## Required libraries
CPUmonitor uses the following libraries:
`psutil`
`py-cpuinfo`
`GPUtil`
`tkinter`
`ttkbootstrap`
`platform`
`multiprocessing`
`os`

## Planned addons

- Live graphs for CPU and GPU temps and loads
- CPU temp and core additions
- Connected peripherals
- More hardware information

> [!NOTE]
> There are probably much better ways of presenting this, but as it evolves and my skills improve, CPUmonitor will also.

### Creating the executable
1) Ensure you have the prerequisite libraries imported
2) `import sys`
3) Access the ```MEIPASS.py``` file. Replace the lines in the original .py file
4) Ensure the .ico file is saved in the root dir
5) Run the following command:
   
``` pyinstaller -w --onefile --icon=icon.ico --add-data=icon.ico:. cpumonitor.py ```

6) Your executable will be saved under the ```./dist``` dir
   
> [!NOTE]
> Below is a helpful 'what does' on each argument

```-w``` launches program without terminal

```--onefile``` makes a single .exe file

```--icon-key=FILE``` sets the window icon

```--add-data=FILE:LOCATION``` compiles key.ico into program
