import tkinter as tki
import pandas as p
import random as r
# Constants and other Global Variables #
watch = None
NAVY = "#070821"
YELLOW = "#F0A500"
BLUE = "#082032"
WHITE = "#FFFFFF"
current = {}
# Data-jutsu #
try:
    data = p.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = p.read_csv("data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Random Word Picker #
def pick():
    global watch, current
    window.after_cancel(watch)
    canvas.itemconfig(image, image=flash2)
    current = r.choice(to_learn)
    canvas.itemconfig(word, text=current['de'])
    canvas.itemconfig(lang, text="Deutsch")
    watch = window.after(3000, flip)

# Flip to show correct translation #


def flip():
    global current
    element = current
    canvas.itemconfig(image, image=flash1)
    canvas.itemconfig(word, text=element['en'])
    canvas.itemconfig(lang, text="English")

# Function to take a word whose meaning is already known to user #


def is_known():
    global current
    to_learn.remove(current)
    updated_data = p.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    pick()


# UI - tkInter #
window = tki.Tk()
window.title("Flash Card App")
window.minsize(width=600, height=400)
window.config(padx=50, pady=50, bg=BLUE)
watch = window.after(3000, flip)

# Canvas
flash1 = tki.PhotoImage(file='img/flash1.png')
flash2 = tki.PhotoImage(file='img/flash2.png')
canvas = tki.Canvas(width=600, height=400, highlightthickness=0, bg=BLUE)
image = canvas.create_image(300, 150, image=flash2)
word = canvas.create_text(300, 135, text="", font=("Ariel", 40, "bold"), fill=WHITE)
lang = canvas.create_text(300, 175, text="", font=("Ariel", 20, "italic"), fill=WHITE)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

cross_image = tki.PhotoImage(file='img/cross.png')
cross = tki.Button(image=cross_image, command=pick, highlightthickness=0, bg='white')
cross.grid(column=0, row=1)

tick_image = tki.PhotoImage(file='img/tick.png')
tick = tki.Button(image=tick_image, command=is_known, highlightthickness=0, bg='white')
tick.grid(column=1, row=1)

# Program begins execution
pick()
window.mainloop()
