# chatding!

_A simple chat notifier for Twitch streamers without viewers_

## Preamble

**chatding** is a utility designed for streamers with low or no audience alerting the user with an audible alarm when someone writes in the twitch chat.

### Set-up

_Edit file config.py_

```
# Your twitch channel preceded by a hash
CHANNEL = '#sheuronazxe'

# Wait x seconds to play alert again on new chat message
DELAY = 120

### Enable (True) / Disable (False) alert modules
# ALERT_SOUND plays audible alarm on default sound device
# ALERT_RUMBLE activate rumble on XBOX compatible controller, more settings in rumble.py
ALERT_SOUND = True
ALERT_RUMBLE = False

# Alert sound file in WAV format
SOUND_FILE = 'sounds/alert.wav'
```

### Behavior

**chatding** plays the alert when it detects a new message in the chat and waits the number of seconds specified in the DELAY variable for a new alert.

If the chatding window is in foreground no sound will be played (this feature only works on Windows platform).
