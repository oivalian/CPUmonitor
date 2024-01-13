def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    # root
    multiprocessing.freeze_support()
    root = ttk.Window(themename='darkly')
    iconPath = resource_path('icon.ico')
    root.iconbitmap(iconPath)
    root.title("CPUMonitor")
    root.geometry("1200x1200")
    root.minsize(1200, 1200)

    '''
    replace lines 63-70 in cpumonitor.py with the above code

    run command:
    pyinstaller -w --onefile --icon=icon.ico --add-data=icon.ico:. cpumonitor.py
    '''
