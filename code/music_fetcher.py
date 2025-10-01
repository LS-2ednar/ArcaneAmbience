from __future__ import unicode_literals
import yt_dlp as ytdlp


class MyLogger(object):
    def debug(self, msg):
        pass  # or print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d.get('status') == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    # Grab best audio; yt-dlp handles format selection better
    'format': 'bestaudio/best',

    # Convert to mp3 @ 192 kbps via ffmpeg
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

    # Nice-to-haves
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'quiet': False,            # set to True to silence
    'no_warnings': False,
    'verbose': False,          # set True if debugging

    # Work around occasional player-client issues on YouTube
    'extractor_args': {
        'youtube': {
            'player_client': ['android', 'web']
        }
    },

    # If the video is age/region restricted, uncomment one of the following:
    # (A) load cookies from your browser automatically:
    # 'cookiesfrombrowser': ('chrome',),  # or ('edge',) / ('firefox',)
    #
    # (B) or point to an exported cookies.txt:
    # 'cookiefile': '/path/to/cookies.txt',
}

url = "https://www.youtube.com/watch?v=kxY72gzq4TE&list=PLxbIk89I7mKuYQcurk0mK-h2Fo_aR1ss7&index=6"

with ytdlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
