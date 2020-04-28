from subprocess import call
import os
import youtube_dl as ydl
import tkinter as tk
from tkinter import *

if __name__ == "__main__":
    start

def start():
    exit = False
    while not exit:
        choice = int(
            input("1. Download movie\n2. Download playlist\n0. Exit\n===> "))
        if choice == 1:
            url = input("Enter movie URL ===> ")
            get_movie(url)
        elif choice == 2:
            url = input("Enter playlist URL ===> ")
            get_playlist(url)
        elif choice == 0:
            exit = True
        else:
            print("Use -h --help ")

def get_movie(url):          
    movie_info = "youtube-dl " + url + " -F"
    call(movie_info.split(), shell=False)
    hq_format = input("Enter video format: ")
    command = "youtube-dl -f " + hq_format + " " + url + " -cit"
    try:
        os.chdir("Dnlded-video")
    except:
        os.makedirs("Dnlded-video")
        os.chdir("Dnlded-video")
    call(command.split(), shell=False)
    os.chdir("..")

def get_playlist(url):       
    command = "youtube-dl -f bestaudio " + " " + url + " -cit"
    try:
        os.chdir("Dnlded-audio")
    except:
        os.makedirs("Dnlded-audio")
        os.chdir("Dnlded-audio")
    call(command.split(), shell=False)
    os.chdir("..")

# root = tk.Tk()
# root.geometry('600x200')
# root.title('Youtube Downloader')
# root['bg'] = '#F9E3E1'
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='C:\Рая_новий_к\ШАГ\Python\Python_homeworks/youtube_icon.png'))

    # label_video = Label(root, text="Video_url:", fg="#900C3F", bg="#F9E3E1")
    # label_playlist = Label(root, text="Playlist_url:", fg="#900C3F", bg="#F9E3E1")   

    # entry_video = Entry(root)
    # entry_playlist = Entry(root)

    # btn_dnl_video = Button(root, text="Download video", background="#AD5294", foreground="#ccc")
    # btn_dnl_playlist = Button(root, text="Download playlist", background="#AD5294", foreground="#ccc") \

    # label_video.grid(row=0, column=0, sticky=E, pady=15, padx=5)
    # label_playlist.grid(row=1, column=0, sticky=E, padx=5)

    # entry_video.grid(row=0, column=1,columnspan=4, pady=5, padx=5)
    # entry_playlist.grid(row=1, column=1,columnspan=4, pady=5, padx=5)

    # btn_dnl_video.grid(row=0, column=5, padx=5, command=get_movie())
    # btn_dnl_playlist.grid(row=1, column=5, padx=5, command=get_playlist())

    # if entry_video:
    #     try:
    #         btn_dnl_video.bind('<Button-1>', get_movie())
    #     except:
    #         btn_dnl_video["text"]="Doesn't work with this url!"
    # elif entry_playlist:
    #     try:
    #         btn_dnl_playlist.bind('<Button-1>', get_playlist())
    #     except:
    #         btn_dnl_playlist["text"]="Doesn't work with this url!"


    # root.mainloop()


    

  
