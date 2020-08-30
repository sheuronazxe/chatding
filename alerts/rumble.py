import ctypes, time
from config import ALERT_RUMBLE

# Rumble intensity, number between 0 and 65535.
FORCE = 32768

# Rumble duration in seconds.
TIME = 1

# Connected controller number, 0 is first controller
CONTROLLER = 0

if ALERT_RUMBLE:

    class XINPUT_VIBRATION(ctypes.Structure):
        _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                    ("wRightMotorSpeed", ctypes.c_ushort)]

    try:
        xinput = ctypes.windll.xinput1_1
    except:
        try:
            xinput = ctypes.windll.xinput1_3
        except:
            try:
                xinput = ctypes.windll.XInput9_1_0
            except:
                raise Exception('ERROR: No xinput DLL found, edit config.py and disable rumble function.')

    XInputSetState = xinput.XInputSetState
    XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
    XInputSetState.restype = ctypes.c_uint


def alert():
    XInputSetState(CONTROLLER, ctypes.byref(XINPUT_VIBRATION(FORCE, FORCE)))
    time.sleep(TIME)
    XInputSetState(CONTROLLER, ctypes.byref(XINPUT_VIBRATION(0, 0)))
