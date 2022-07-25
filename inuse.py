import os
from tkinter import Y

os.chdir("/")

link = "never gonna give u up"
yt = "/home/ian/SeagateSSD/Youtube"
dl = "youtube-dl -f 'bestvideo[ext=mp3]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 '" + link + "'"
ls = "ls"
nm = ""
dlvideodl = input("do you want to download the video downloader folder(y/n)? ")
dllink = input("do you want to download a link(y/n)? ")
dlplaylists = input("do you want to download your playlists(y/n)? ")

#############################// Functions //################################################################

#------------// Link Downloader Function//------------------------------
def rlink(rlink):
    dl = "youtube-dl -f 'bestvideo[ext=mp3]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 '" + rlink + "'"
    os.system(dl)
    
#-------------------------------------------------------

#------------// Main Function //------------------------------
def play(link, nm):
    os.chdir(nm)
    #os.system(ls)
    dl = "youtube-dlc -i --playlist-reverse " + link
    os.system(dl)
    os.chdir(yt)
    #--max-downloads 10
#-------------------------------------------------------

##########################################################################################################



#---------// Video Downloader folder//------------------

if dlvideodl == "y":
    os.chdir("/home/ian/SeagateSSD/VideoDownloader")
    rlink("https://www.youtube.com/playlist?list=PL8JfnviJLyi7ChGyV_tNo2hsz06SKerKj")
    os.chdir("/")

#-------------------------------------------------------


#--------// Link Dowloader //----------------------
if dllink == "y":
    wh = input("Where Bro?? ")
    os.chdir(wh)
    rlink(input("Gimme the link my man: "))
    os.chdir("/")
#-------------------------------------------------



#------------// Playlis //--------------------------
if dlplaylists == "y":
    os.chdir("/home/ian/SeagateSSD/Youtube")
    #play("", "")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi77ewod8elf_Nqnk7k51pJa", "Metaphysics")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi6ZKxYDckDcS8T9ZaYAL27e", "Classic_a")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi68hnELjGtmZyvtKArlAwbr", "Phylosophy and world")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7frCVJGzxGaEu46ErMG4Mz", "Thoughts")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7l1FrBaKiWdPF4qvRVpFLT", "Math and Physics")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi453FgNs0Rpl9l0Kaq6dL1x", "Legendary Moments")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi4KoYRciRtMBxOwBINDjrYt", "Lectures")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi5mYG_oYfMctyqwBONJiwGk", "Social Sciences")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7gVkn4_OsxhUqdG0pr_CaO", "Clips")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi43SIF85HGHIG4uwSZXyxsD", "Mation")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi7ZCJIKD_oMMPnKOE6pmfJL", "Self")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi5b231OHjWowGy9lTzDzCdN", "Violin Moments")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi5ldU-fXmKRLLiv05IfoObW", "Water")

    play("https://www.youtube.com/playlist?list=PL8JfnviJLyi520tBU-XwjJvdEfnC8aYnN", "New Classic")

    os.chdir("/")

#--------------------------------------------------
