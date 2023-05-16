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

Previous=tk.PhotoImage(file="prev_img.png")
stop_image=tk.PhotoImage(file="stop_img.png")
Play=tk.PhotoImage(file="play_img.png")
Pause=tk.PhotoImage(file="pause_img.png")
Next=tk.PhotoImage(file="next_img.png")

#Function for Selecting music from given list

def Select():
    label.config(text=List.get("anchor"))
    mixer.music.load(rootpath+"\\"+List.get("anchor"))
    mixer.music.play()

#Function for creating stop Button to stop music

def Stop():
    mixer.music.stop()
    List.select_clear('active')

#Function for creating next Button to skip to next song

def PlayNext():
    next_song=List.curselection()
    next_song= next_song[0]+1
    next_song_name= List.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    List.select_clear(0,'end')
    List.activate(next_song)
    List.select_set(next_song)

#Function for creating play Button to play music
def PreviousSong():
    next_song=List.curselection()
    next_song= next_song[0]-1
    next_song_name= List.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    List.select_clear(0,'end')
    List.activate(next_song)
    List.select_set(next_song)

#Function for creating pause Button to pause the current song
    
def PauseMusic():
    if PauseButton["text"]=="Pause":
        mixer.music.pause()
        PauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        PauseButton["text"]="Pause"

List=tk.Listbox(player,fg="purple",bg="pink",width=100,font=('Bhineka',18))
List.pack(padx=15,pady=15)

label= tk.Label(player,text='',bg='black',fg='yellow',font=('ds_digital',18))
label.pack(pady=15)

Top=tk.Frame(player,bg="dark blue")
Top.pack(padx=10,pady=5,anchor='center')

PreviousButton=tk.Button(player,text="prev",image=Previous,bg='dark blue',borderwidth=0,command=PreviousSong)
PreviousButton.pack(pady=15,in_=Top,side='left')

stopButton=tk.Button(player,text="stop",image=stop_image,bg='brown',borderwidth=0,command=Stop)
stopButton.pack(pady=15,in_=Top,side='left')


PlayButton=tk.Button(player,text="prev",image=Play,bg='dark green',borderwidth=0,command=Select)
PlayButton.pack(pady=15,in_=Top,side='left')

PauseButton=tk.Button(player,text="prev",image=Pause,bg='orange',borderwidth=0,command=PauseMusic)
PauseButton.pack(pady=15,in_=Top,side='left')

NextButton=tk.Button(player,text="prev",image=Next,bg='dark blue',borderwidth=0,command=PlayNext)
NextButton.pack(pady=15,in_=Top,side='left')

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        List.insert('end',filename)


player.mainloop()
