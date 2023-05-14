import tkinter as tk
import fnmatch
import os
from pygame import mixer

player= tk.Tk()
player.title("Music Player")
player.geometry("800x800")
player.config(bg='purple')

rootpath="C:\\SONGS"
pattern= "*.mp3"

mixer.init()

prev_image=tk.PhotoImage(file="prev_img.png")
stop_image=tk.PhotoImage(file="stop_img.png")
play_image=tk.PhotoImage(file="play_img.png")
pause_image=tk.PhotoImage(file="pause_img.png")
next_image=tk.PhotoImage(file="next_img.png")

#Function for Selecting music from given list

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listBox.get("anchor"))
    mixer.music.play()

#Function for creating stop Button to stop music

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

#Function for creating next Button to skip to next song

def play_next():
    next_song=listBox.curselection()
    next_song= next_song[0]+1
    next_song_name= listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

#Function for creating play Button to play music
def play_prev():
    next_song=listBox.curselection()
    next_song= next_song[0]-1
    next_song_name= listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

#Function for creating pause Button to pause the current song
    
def pause_song():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"

listBox=tk.Listbox(player,fg="purple",bg="pink",width=100,font=('Bhineka',18))
listBox.pack(padx=15,pady=15)

label= tk.Label(player,text='',bg='black',fg='yellow',font=('ds_digital',18))
label.pack(pady=15)

top=tk.Frame(player,bg="dark blue")
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(player,text="prev",image=prev_image,bg='dark blue',borderwidth=0,command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(player,text="stop",image=stop_image,bg='brown',borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(player,text="prev",image=play_image,bg='dark green',borderwidth=0,command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(player,text="prev",image=pause_image,bg='orange',borderwidth=0,command=pause_song)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(player,text="prev",image=next_image,bg='dark blue',borderwidth=0,command=play_next)
nextButton.pack(pady=15,in_=top,side='left')

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)


player.mainloop()