import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from pygame import mixer
root = Tk()
songlist = []
#realnames = []
index = 0
v = StringVar()
p = StringVar()
songlabel = Label(root, width=35, textvariable=v, bg='red')
pplabel = Label(root, width=35, textvariable=p, font='Jokerman 10', bg='red')
vlabel = Label(root, width = 35, text = "Volume", font = 'Jokerman 10', bg='red')
ppi = 0
def pp():
    global ppi
    if ppi == 0:
        pause()
        p.set("Paused")
        ppi = ppi + 1
    elif ppi == 1:
        play()
        p.set("Now Playing: ")
        ppi = ppi - 1

def choosedir():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            # realdir = os.path.realpath(files)
            # audio = ID3(realdir)
            # realnames.append(audio['TIT2'].text[0])
            songlist.append(files)
    p.set("Now Playing: ")
    pygame.mixer.init()
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    updatelabel()


def updatelabel():
    v.set(songlist[index])


def play():
    pygame.mixer.music.unpause()

def next():
    global index
    index = index + 1
    pygame.mixer.init()
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    p.set("Now Playing: ")
    updatelabel()

def previous():
    global index
    index = index - 1
    p.set("Now Playing: ")
    pygame.mixer.init()
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    updatelabel()

def stop():
    global index
    pygame.mixer.music.stop()
    index = 0
    v.set("")
    p.set("")

def pause():
    pygame.mixer.music.pause()

choosedir()

mimage = PhotoImage(file='C:\\Users\\Himank Jerolia\\Desktop\\mlogo.PNG')
ilabel = Label(root, image=mimage, bg='red')
ilabel.grid(row='0', columnspan=2)

listb = Listbox(root, font='Broadway 10')
listb.grid(column='0', rowspan=4)
for songs in songlist:
    listb.insert(END, songs)

button4 = Button(text="Play/Pause", command=pp)
button4.grid(column='1', row='1')

button1 = Button(text="Next", command=next)
button1.grid(column='1', row='2')

button2 = Button(text="Previous", command=previous)
button2.grid(column='1', row='3')

button3 = Button(text="Stop", command=stop)
button3.grid(column='1', row='4')

def setvol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


scale = Scale(root, from_=0, to = 100, orient = HORIZONTAL, command = setvol, bg='red')
scale.set(70)
scale.grid(row = 6, columnspan =2)

vlabel.grid(row = '5', columnspan = 2)

songlabel.grid(row='8', columnspan=2)
pplabel.grid(row='7', columnspan=2)

root.title("Music Player")
root.config(bg='Red')
root.mainloop()