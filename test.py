from gtts import gTTS
import os
import tkinter as tk
from io import BytesIO 
import pygame
import time
import customtkinter as ctk

pygame.init()
pygame.mixer.init()

root = ctk.CTk()
root.geometry("400x400+500+100")
root.title("Rupesh Text to Speech App")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

title_font = ("Sans Serif", 16, "bold")
label_font = ("Sans Serif", 12)
entry_font = ("Sans Serif", 10)
btn_font = ("Sans Serif", 10, "bold")

def wait():
    while pygame.mixer.get_busy():
        time.sleep(0.1)

def speak():
    global text, lan
    mp3_fo = BytesIO()
    tts = gTTS(text.get("1.0", tk.END), lang=lan.get())
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()

def create_mp3(lang="en"):
    if lan.get() != None:
        lang = str(lan.get())
    s = gTTS(text.get("1.0", tk.END), lang=lang)
    s.save(f"{str(mp3.get())}.mp3")
    filename = mp3.get() + ".mp3"
    os.system("start " + filename)

def toggle_theme():
    if ctk.get_appearance_mode() == "dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

title = ctk.CTkLabel(root, text="TEXT TO SPEECH", font=title_font)
title.pack(pady=10)

l2 = ctk.CTkLabel(root, text="Choose language (default is English)", font=label_font)
l2.pack()

lan = ctk.StringVar()
lan.set("en")
language = ctk.CTkEntry(root, textvariable=lan, width=100, font=entry_font)
language.pack(pady=5)
language.focus()

l3 = ctk.CTkLabel(root, text="Insert the MP3 name, without the filetype .mp3", font=label_font)
l3.pack()

mp3 = ctk.StringVar()
mp3title = ctk.CTkEntry(root, textvariable=mp3, width=200, font=entry_font)
mp3title.pack(pady=5)
mp3.set("myfile")

speak_but = ctk.CTkButton(root,
    text="Listen Audio without saving the MP3 file",
    font=btn_font,
    command=speak)
speak_but.pack(pady=10)

text = ctk.CTkTextbox(root, font=entry_font, height=100, width=300)
text.pack(pady=10)
text.insert("1.0", "Hello")

mp3_but = ctk.CTkButton(root,
    text="Save the Audio",
    font=btn_font,
    command=create_mp3)
mp3_but.pack(pady=10)

theme_but = ctk.CTkButton(root,
    text="Toggle Theme",
    font=btn_font,
    command=toggle_theme)
theme_but.pack(pady=10)

root.mainloop()
