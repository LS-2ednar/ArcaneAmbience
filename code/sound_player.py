from pydub import AudioSegment
from pydub.playback import play

# Load audio
song = AudioSegment.from_file("Ori and the Blind Forest - First Steps Into Sunken Glades - OST.mp3", format="mp3")

# Slice from 30s to 45s
segment = song[30_000:45_000]   # times in milliseconds

# Play once
print("Playing Intro")
play(song[0:30_000])


# Loop 3 times
print("Repeating segement 3 times")
looped = segment * 3
play(looped)

print("Playing outro")
play(song[45_000::])