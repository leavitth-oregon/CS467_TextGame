# Fugue Jukebox
# Hayley Leavitt 2023
# Version 0.0
# 
# Jukebox is a microservice that runs alongside the Fugue Game to play the music for the game. 
# Jukebox will receive location names from Fugue Map and play the corresponding music.
#     
# References:
# https://docs.python.org/3/library/subprocess.html 
# https://docs.python.org/3/library/threading.html 
# https://python.plainenglish.io/play-music-using-python-subprocess-8c7a1bde2271 
# https://www.bogotobogo.com/python/python_subprocess_module.php 

# libraries
import subprocess 
from threading import Thread
import time

# global variables
mediaplayer = ["afplay ", "mpg123 "]
song_files = ['fugue_song_1.mp3', 'fugue_memories.mp3', 'fugue_combat.mp3']

# classes 
class Jukebox(): 

    def __init__(self) -> None:
        self.musicplayer = "mpg123"
        self._p = None

    def play_song(self, song_file) -> None:
        # create the player process
        self._p = subprocess.Popen([self.musicplayer,    # the music player, in this case mpg123
                                '-C',                  # Enable commands to be read from stdin
                                '-q',                  # Use quiet mode, which has less terminal alerts
                                song_file],            # the song we want to play
                                stdin = subprocess.PIPE, 
                                stderr = None) 

        # stop mpg123 from complainging when we exit
        self._p.stdin.write(b'')
        self._p.stdin.flush()
        return

    def stop_song(self) -> None: 
        self._p.stdin.write(b'q')
        self._p.stdin.flush()

        # kill the process
        self._p.kill()
        return


# main code
def main():
    jukebox = Jukebox()

    jukebox.play_song(song_files[1])
    print()
    print("playing: " + song_files[1])
    print("play for 2 seconds")
    time.sleep(2)

    print()
    print("stopping music")
    jukebox.stop_song()
    print(f'Return code: {jukebox._return_code}')

    return


if __name__ == "__main__":
    main()
