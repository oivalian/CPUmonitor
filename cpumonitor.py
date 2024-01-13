import multiprocessing
import psutil as ps
import platform as pl
import cpuinfo
import GPUtil
import ttkbootstrap as ttk
import os


def cpu_core_list():
    return [f"Core #{core} Load: {perc}%{os.linesep}"
            for core, perc in enumerate(ps.cpu_percent(percpu=True, interval=1))]


def get_drive_list():
    drives = ps.disk_partitions()
    drive_info_list = []

    drive_string_var.get()
    for drive in drives:
        try:
            drive_usage = ps.disk_usage(drive.mountpoint)
        except PermissionError:
            continue
        drive_list = f"{drive.mountpoint} ({drive.fstype})"
        drive_total = drive_usage.total // (1024 ** 3)
        drive_used = drive_usage.used // (1024 ** 3)
        drive_free = drive_usage.free // (1024 ** 3)
        drive_info = (f"{drive_list}\nTotal Size: {drive_total} GB"
                      f"\nUsed: {drive_used} GB\nFree: {drive_free} GB")
        drive_info_list.append(drive_info)
        drive_string = "\n\n".join(drive_info_list)
        drive_string_var.set(drive_string)


def get_gpu_list(gpu_string):
    gpu_list = GPUtil.getGPUs()
    gpus = []
    for gpu in gpu_list:
        gpu_total = gpu.memoryTotal // 1024
        gpu_used = gpu.memoryUsed // 1024
        gpu_free = gpu.memoryFree // 1024
        gpu_name = f"{gpu.name} {gpu_total:.0f} GB"
        gpu_stats = (f"Current Load: {gpu.load*100:.0f}%"
                     f"\nCurrent Temp: {gpu.temperature:.0f}°C"
                     f"\nUsed: {gpu_used:.0f} GB\n"
                     f"Free: {gpu_free:.0f} GB")
        gpu_info = f"{gpu_name}\n{gpu_stats}\n"
        gpus.append(gpu_info)
        gpu_string = "\n\n".join(gpus)
    return gpu_string


def gui_updater():
    cpu_string = []
    cpu_coreInfo_var.set("".join(cpu_core_list()))
    cpu_perc_var.set(f"Current CPU usage: {ps.cpu_percent()}%")
    gpu_string_var.set(get_gpu_list("".join(cpu_string)))
    root.after(1500, gui_updater)


if __name__=="__main__":
    # root
    multiprocessing.freeze_support()
    root = ttk.Window(themename="darkly")
    root.title("CPUmonitor")
    root.iconbitmap("icon.ico")
    root.geometry("1200x1200")
    root.minsize(1200, 1200)
    
    
    # content
    # -- System Information Box --
    sys_frame = ttk.Frame(root)
    
    # System Title
    sys_title = ttk.Label(sys_frame, text="System Information", font="Verdana 12 bold")
    
    # System
    sysinfo = pl.uname()
    
    # Device Name
    sys_name = f"Device name: {sysinfo.node}"
    sys_name_var = ttk.StringVar()
    sys_name_var.set(sys_name)
    sys_name_label = ttk.Label(sys_frame, textvariable=sys_name_var, font="Verdana 8")
    
    # OS
    sys_osinfo = f"Operating System: {sysinfo.system} {sysinfo.release}"
    sys_osinfo_var = ttk.StringVar()
    sys_osinfo_var.set(sys_osinfo)
    sys_osinfo_label = ttk.Label(sys_frame, textvariable=sys_osinfo_var, font="Verdana 8")
    
    # Version Number
    sys_vers = f"Version: {sysinfo.version}"
    sys_vers_var = ttk.StringVar()
    sys_vers_var.set(sys_vers)
    sys_vers_label = ttk.Label(sys_frame, textvariable=sys_vers_var, font="Verdana 8")
    
    
    # -- Memory Box --
    mem_frame = ttk.Frame(root)
    
    # Memory Title
    mem_title = ttk.Label(mem_frame, text="Memory", font="Verdana 12 bold")
    
    # Total Memory
    mem_total = round(ps.virtual_memory().total / (1024. ** 3))
    mem_total_string = f"Installed memory: {mem_total} GB"
    mem_total_var = ttk.StringVar()
    mem_total_var.set(mem_total_string)
    mem_total_label = ttk.Label(mem_frame, textvariable=mem_total_var, font="Verdana 8")
    
    # Available Memory
    mem_avail = round(ps.virtual_memory().available / (1024. ** 3))
    mem_avail_string = f"Available memory: {mem_avail} GB"
    mem_avail_var = ttk.StringVar()
    mem_avail_var.set(mem_avail_string)
    mem_avail_label = ttk.Label(mem_frame, textvariable=mem_avail_var, font="Verdana 8")
    
    # Used Memory
    mem_used = round(ps.virtual_memory().used / (1024. ** 3))
    mem_used_string = f"Used memory: {mem_used} GB"
    mem_used_var = ttk.StringVar()
    mem_used_var.set(mem_used_string)
    mem_used_label = ttk.Label(mem_frame, textvariable=mem_used_var, font="Verdana 8")
    
    
    # -- Drive Box --
    drive_frame = ttk.Frame(root)
    
    # Drive Title
    drive_title = ttk.Label(drive_frame, text="Available Drives", font="Verdana 12 bold")
    
    # Drives
    drive_string_var = ttk.StringVar()
    drive_label = ttk.Label(drive_frame, textvariable=drive_string_var, font="Verdana 8")
    
    
    # -- CPU Information Box --
    cpu_frame = ttk.Frame(root)
    
    # CPU Title
    cpu_title = ttk.Label(cpu_frame, text="CPU Information", font="Verdana 12 bold")
    
    # CPU Model
    cpu_model = cpuinfo.get_cpu_info()["brand_raw"]
    cpu_model_var = ttk.StringVar()
    cpu_model_var.set(cpu_model)
    cpu_model_label = ttk.Label(cpu_frame, textvariable=cpu_model_var, font="Verdana 8")
    
    # CPU Speeds
    cpu_max = cpuinfo.get_cpu_info()["hz_advertised_friendly"]
    cpu_actual = cpuinfo.get_cpu_info()["hz_actual_friendly"]
    cpu_speeds = f"CPU speed: {cpu_actual} ({cpu_max})"
    cpu_speeds_var = ttk.StringVar()
    cpu_speeds_var.set(cpu_speeds)
    cpu_speeds_label = ttk.Label(cpu_frame, textvariable=cpu_speeds_var, font="Verdana 8")
    
    # CPU Percentage
    cpu_perc_var = ttk.StringVar()
    cpu_perc_label = ttk.Label(cpu_frame, textvariable=cpu_perc_var, font="Verdana 8")
    
    # CPU Core Count
    cpu_avail = ps.cpu_count(False)
    cpu_avail_string = f"Total CPU cores: {cpu_avail}"
    cpu_avail_var = ttk.StringVar()
    cpu_avail_var.set(cpu_avail_string)
    cpu_avail_label = ttk.Label(cpu_frame, textvariable=cpu_avail_var, font="Verdana 8")
    
    # CPU Cores List
    cpu_cores_frame = ttk.Frame(root)
    
    # CPU cores list title
    cpu_cores_title = ttk.Label(cpu_cores_frame, text="CPU Cores", font="Verdana 12 bold")
    
    # CPU Cores Usage
    cpu_coreInfo_var = ttk.StringVar()
    cpu_coreInfo_label = ttk.Label(cpu_cores_frame, textvariable=cpu_coreInfo_var, font="Verdana 8")
    
    
    # -- GPU Information Box --
    gpu_frame = ttk.Frame(root)
    
    # GPU title
    gpu_title = ttk.Label(gpu_frame, text="GPU Information", font="Verdana 12 bold")
    
    #GPU List
    gpu_string_var = ttk.StringVar()
    gpu_label = ttk.Label(gpu_frame, textvariable=gpu_string_var, font="Verdana 8")
    
    
    # -- PACKAGE --
    # System Information Package
    sys_frame.grid(row=1, column=1, sticky="nsew")
    sys_title.pack(pady=10, anchor="w")
    sys_name_label.pack(anchor="w")
    sys_osinfo_label.pack(anchor="w")
    sys_vers_label.pack(anchor="w")
    
    
    # CPU Package
    cpu_frame.grid(row=1, column=2, sticky="nsew")
    cpu_title.pack(pady=10, anchor="w")
    cpu_model_label.pack(anchor="w")
    cpu_speeds_label.pack(anchor="w")
    cpu_perc_label.pack(anchor="w")
    cpu_avail_label.pack(anchor="w")
    
    
    # CPU Cores Package
    cpu_cores_frame.grid(row=2, column=2, sticky="nsew")
    cpu_cores_title.pack(pady=10, anchor="w")
    cpu_coreInfo_label.pack(anchor="w")
    
    
    # Memory Package
    mem_frame.grid(row=1, column=3, sticky="nsew")
    mem_title.pack(pady=10, anchor="w")
    mem_total_label.pack(anchor="w")
    mem_avail_label.pack(anchor="w")
    mem_used_label.pack(anchor="w")
    
    
    # Drive Package
    drive_frame.grid(row=2, column=1, sticky="nsew")
    drive_title.pack(pady=10, anchor="w")
    drive_label.pack(anchor="w")
    
    
    # GPU Frame
    gpu_frame.grid(row=2, column=3, sticky="nsew")
    gpu_title.pack(pady=10, anchor="w")
    gpu_label.pack(anchor="w")
    
    
    # Grid configuration
    for _ in range(3):
        root.rowconfigure(_, weight=2)
    for _ in range(4):
        root.columnconfigure(_, weight=2)


    # loop
    gui_updater()
    get_drive_list()
    root.mainloop()
