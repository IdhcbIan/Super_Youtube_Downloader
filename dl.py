import os
from tkinter import Y

os.chdir("/")

link = "never gonna give u up"
yt = "/home/ian/SeagateSSD/Youtube"
dl = "youtube-dl -f 'bestvideo[ext=mp3]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 '" + link + "'"
ls = "ls"
nm = ""
os.chdir("/home/ian/SeagateSSD/Youtube")

#------------// Main Function //------------------------------
def play(link, nm):
    os.chdir(nm)
    #os.system(ls)
    dl = "youtube-dl --max-downloads 10 --playlist-reverse -f 'bestvideo[ext=mp3]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 '" + link + "'"
    os.system(dl)
    os.chdir(yt)

#-------------------------------------------------------


#------------// Playlis //--------------------------
#play("", "")

play("https://www.youtube.com/playlist?list=PL8JfnviJLyi6ZKxYDckDcS8T9ZaYAL27e", "Classic")

play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7frCVJGzxGaEu46ErMG4Mz", "Thoughts")

play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7l1FrBaKiWdPF4qvRVpFLT", "Math and Physics")

play("https://www.youtube.com/playlist?list=PL8JfnviJLyi453FgNs0Rpl9l0Kaq6dL1x", "Legendary Moments")

play("https://www.youtube.com/playlist?list=PL8JfnviJLyi4KoYRciRtMBxOwBINDjrYt", "Lectures")
#--------------------------------------------------
