import os
def create_music_names():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    with open("file_names.txt","w+") as file1:
        for f in files:
            #dot=f.find(".")
            if f.endswith("mp3"):
                file1.write(f+"\n")
    return "file_names.txt"
