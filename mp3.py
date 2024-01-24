import os
import pygame
import tkinter as tk
from tkinter import filedialog

def play_music():
    selected_song = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def load_music():
    folder = filedialog.askdirectory()
    os.chdir(folder)
    songs = [file for file in os.listdir(folder)if file.endswith(".mp3")]
    for song in songs:
        listbox.insert(tk.END,song)

root= tk.Tk()
root.title("MP3 PLAYER")

pygame.init()
pygame.mixer.init()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

play_button = tk.Button(root, text='play',command= play_music)
play_button.pack(pady=5)

stop_button = tk.Button(root, text='stop',command= stop_music)
stop_button.pack(pady=5)

load_button = tk.Button(root, text='load music',command= load_music)
load_button.pack(pady=10)

root.mainloop()