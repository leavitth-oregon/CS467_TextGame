# Fugue Jukebox
# Hayley Leavitt 2023
# Version 2.0
#     
# References:
# https://docs.python.org/3/library/subprocess.html 
# https://docs.python.org/3/library/threading.html 
# https://python.plainenglish.io/play-music-using-python-subprocess-8c7a1bde2271 
# https://www.bogotobogo.com/python/python_subprocess_module.php 
# https://stackoverflow.com/questions/307305/play-a-sound-with-python

# libraries
import subprocess 
from threading import Thread
import time

# global variables
mediaplayer = ["afplay ", "mpg123 "]
song_files = ["shopkeepers_tune.mp3", "fugue_combat.mp3", "fugue_credits.mp3", "fugue_ending.mp3", "fugue_memories.mp3", "fugue_paths_and_roads.mp3", "fugue_throne_room.mp3", "fugue_tower_bedroom.mp3"]

# classes 
class Jukebox(): 

    def __init__(self) -> None:
        self.musicplayer = "mpg123"
        self.operating_system = "Linux"
        self._p = None

    def set_os(self) -> None: 
        user_os = input("What OS are you running? \n 1.) Windows \n 2.) MacOS \n 3.) Linux \n")

        if (user_os == "1") or (user_os.lower() == "windows"):
            self.operating_system = "Windows"

        return 

    def play_song(self, song_file: str) -> None:
        if self.operating_system != "Windows":
            # create the player process 
            self._p = subprocess.Popen([self.musicplayer,     # the music player, in this case, mpg123
                                    '-C',                     # Enable commands to be read from stdin
                                    '-q',                     # Use quiet mode, which has less terminal alerts
                                    song_file],               # the song we want to play
                                    stdin = subprocess.PIPE,  # pipe the subprocess
                                    stderr = None)            # no error

            # handle exit procedures of the subprocess
            self._p.stdin.write(b'')
            self._p.stdin.flush()
        
        else: 
            import winsound
            self._p = subprocess.Popen(winsound.PlaySound(song_file, winsound.SND_FILENAME),   # the music player, in this case, winsound
                                       stdin = subprocess.PIPE,                                # pipe the subprocess
                                       stderr = None)                                          # no error

            # handle exit procedures of the subprocress
            self._p.stdin.write(b'')
            self._p.stdin.flush()

        return

    def stop_song(self) -> None: 
        # handle exit procedures
        self._p.stdin.write(b'q')
        self._p.stdin.flush()

        # kill the process
        self._p.kill()
        return


def main():
    juke = Jukebox()
    juke.set_os() 
    for song in song_files:
        print("Now playing " + song + " for 30 seconds.")
        juke.play_song(song)

        # let the song play for 30 seconds
        time.sleep(30)

        # stop the song and move on to the next
        juke.stop_song()
        print("Song stopped.\n")
    
    return


if __name__ == "__main__":
    main()
