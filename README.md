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
```

### Behavior

**chatding** plays the alert when it detects a new message in the chat and waits the number of seconds specified in the DELAY variable for a new alert. If the chatding window is in foreground no sound will be played.

This script uses Windows specific libraries, it will not work on Mac or Linux.