from pygame import mixer
import glob
#import file_names as fn

#fn.create_music_names()

def choose_song(num):
    num=int(num)-1
    mixer.init()
    mixer.music.load(song_list[num])
    mixer.music.play()
    print("Now Playing: "+song_list[num])
    return num

def choose_name(check):
    choose=input("\nWhich song to play? Choose its number: ")
    track_no=choose_song(choose)
    return track_no

def skip_song(num):
    num=num+1
    if num<len(song_list):
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing: "+song_list[num])
    else:
        num=0
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing: "+song_list[num])
    return num

def prev_song(num):
    num=num-1
    if num>=0:
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing: "+song_list[num])
    else:
        num=len(song_list)-1
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing: "+song_list[num])
    return num

# Creating a list of songs in the current folder

song_list=glob.glob("*.mp3")
print("\nSongs available to play:")
for i in range(len(song_list)):
    print(str(i+1)+"."+song_list[i])

check="Start"
number=choose_name(check)

i=0
while i<1:
    check=input("\nWhat to do? Type QUIT to quit: ")
    check=check.upper()
    '''if check=="END":
        mixer.music.stop()
        print("Music Ended")'''
    if check=="PAUSE" or check=="||":
        mixer.music.pause()
        print("Music paused")
    elif check=="RESUME" or check==">|":
        mixer.music.unpause()
        print("Music resumed")
    elif check=="CHANGE":
        number=choose_name(check)
    elif check=="SKIP" or check==">>":
        number=skip_song(number)
    elif check=="REWIND" or check=="<":
        mixer.music.rewind()
        print("Now Playing:"+song_list[number])
    elif check=="PREV" or check=="<<":
        number=prev_song(number)
    elif check=="QUIT":
        mixer.music.stop()
        i=1
    else:
        print("Invalid Input.Please try again.")
