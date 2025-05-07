# Player Launcher

A Python class for launching video URLs in VLC or PotPlayer using custom URI schemes.

## Features

- Supports VLC and PotPlayer media players
- Simple API with direct player methods
- Cross-platform compatibility:
  - Windows (os.startfile)
  - macOS (open command)
  - Linux (xdg-open)

## Example Usage
```py
from app import Player

player = Player()

player.potplayer('https://example.com/video.mp4')
```
