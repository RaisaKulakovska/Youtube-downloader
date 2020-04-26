from subprocess import call
import os
import youtube_dl as ydl
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

    

  
