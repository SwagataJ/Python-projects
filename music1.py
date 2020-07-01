from pygame import mixer
import file_names as fn

fn.create_music_names()

def choose_song(num):
    num=int(num)-1
    mixer.init()
    mixer.music.load(song_list[num])
    mixer.music.play()
    print("Now Playing:"+song_list[num])
    return num

def choose_name(check):
    choose=input("\nWhich song to play? Choose its number: ")
    track_no=choose_song(choose)
    return track_no

def skip_song(num):
    num=num+1
    if num<len(song_list)-1:
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing:"+song_list[num])
    else:
        num=0
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing:"+song_list[num])
    return num

def prev_song(num):
    num=num-1
    if num>=0:
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing:"+song_list[num])
    else:
        num=len(song_list)-2
        mixer.music.load(song_list[num])
        mixer.music.play()
        print("Now Playing:"+song_list[num])
    return num

'''print("Type END to end track")
print("Type PAUSE to pause track")
print("Type RESUME to resume track")
print("Type ADD to add new track")
print("Type SKIP to skip track")
print("Type REPLAY to replay track")
print("Type QUIT to quit")'''
song_list=[]
with open("file_names.txt") as file:
    #song_list.append(file.readline())
    file=file.read()
    song_list=file.split("\n")
#file="My Blood - Westlife.mp3"
#print(song_list)
print("\nSongs available to play:")
for i in range(len(song_list)-1):
    print(str(i+1)+"."+song_list[i])
#print("\n")
#mixer.init()
#mixer.music.load(song_list[0])
#mixer.music.play()
#del song_list[0]

check="Start"
number=choose_name(check)

i=0
while i<1:
    #mixer.music.queue(song_list[number+1])
    #mixer.music.get_queue(song_list[number+1])
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
        #print("Song added successfully")
        #mixer.music.queue(song)
    elif check=="SKIP" or check==">>":
        number=skip_song(number)
        #print("Now Playing:"+song_list[0])
        #del song_list[0]
    elif check=="REWIND" or check=="<":
        mixer.music.rewind()
        print("Now Playing:"+song_list[number])
    elif check=="PREV" or check=="<<":
        number=prev_song(number)
    elif check=="QUIT":
        i=1
    else:
        print("Invalid Input.Please try again.")
