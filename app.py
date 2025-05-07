
import subprocess
import sys
import os

class Player:

    def vlc(self, video_url):
        self.open(video_url, 'vlc')

    def potplayer(self, video_url):
        self.open(video_url, 'potplayer')

    def open(self, video_url, player='vlc'):
        if player.lower() == 'vlc':
            scheme = 'vlc'
        elif player.lower() == 'potplayer':
            scheme = 'potplayer'
        else:
            raise ValueError("Unsupported player. Use 'vlc' or 'potplayer'.")

        url = f"{scheme}://{video_url}"

        if sys.platform.startswith('win'):
            os.startfile(url)
        elif sys.platform.startswith('darwin'):
            subprocess.run(['open', url])
        else:
            subprocess.run(['xdg-open', url])


