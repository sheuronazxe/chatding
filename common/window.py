from sys import platform

def foreground():

    if "linux" in platform:
        return False

    elif "darwin" in platform:
        return False

    elif "win" in platform:
        import os, ctypes
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        pid = ctypes.c_ulong()
        ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        return True if os.getppid() == pid.value else False

    else:
        return False
