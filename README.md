# chatding!

_A simple chat notifier for Twitch streamers without viewers_

## Preamble

**chatding** is a utility designed for streamers with low or no audience alerting the user with an audible alarm when someone writes in the twitch chat.

### Set-up

_Edit file config.py_

```
# Get your oauth token at https://www.twitchapps.com/tmi/
TOKEN = 'oauth:your_oauth_token'
NAME = 'your_twitch_name'
CHANNEL = '#your_twitch_channel'

# Wait x seconds to play alert again on new chat message
DELAY = 120
```

### Behavior

**chatding** plays the alert when it detects a new message in the chat and waits the number of seconds specified in the DELAY variable for a new alert. If the chatding window is in foreground no sound will be played.

This script uses Windows specific libraries, it will not work on Mac or Linux.