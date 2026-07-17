from tkinter import *
import pandas as pd
import random
from pathlib import Path

BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME = 3000

DATA_FOLDER = Path("data")
IMAGE_FOLDER = Path("images")

try:
    data = pd.read_csv(DATA_FOLDER / "words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(DATA_FOLDER / "french_words.csv")

cards = data.to_dict(orient="records")

current_card = {}
flip_timer = None


def save_progress():
    remaining = pd.DataFrame(cards)
    remaining.to_csv(DATA_FOLDER / "words_to_learn.csv", index=False)


def choose_card():
    global current_card
    current_card = random.choice(cards)


def show_front():
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word,
                      text=current_card["French"],
                      fill="black")


def show_back():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,
                      text=current_card["English"],
                      fill="white")


def next_card():
    global flip_timer

    if len(cards) == 0:
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(card_title,
                          text="Finished!",
                          fill="black")
        canvas.itemconfig(card_word,
                          text="You've learned every word!",
                          fill="black")
        return

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    choose_card()
    show_front()

    flip_timer = window.after(FLIP_TIME, flip_card)


def flip_card():
    show_back()


def known_word():
    if current_card in cards:
        cards.remove(current_card)

    save_progress()
    next_card()


def unknown_word():
    next_card()

window = Tk()
window.title("French Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=1000, height=800)

card_front = PhotoImage(file=IMAGE_FOLDER / "card_front.png")
card_back = PhotoImage(file=IMAGE_FOLDER / "card_back.png")

canvas = Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

card_image = canvas.create_image(
    400,
    263,
    image=card_front
)

card_title = canvas.create_text(
    400,
    150,
    text="French",
    font=("Arial", 40, "italic"),
    fill="black"
)

card_word = canvas.create_text(
    400,
    263,
    text="",
    font=("Arial", 60, "bold"),
    fill="black"
)

canvas.pack()

wrong_image = PhotoImage(file=IMAGE_FOLDER / "wrong.png")

wrong_button = Button(
    image=wrong_image,
    borderwidth=0,
    highlightthickness=0,
    command=unknown_word
)

wrong_button.place(x=200, y=560)

right_image = PhotoImage(file=IMAGE_FOLDER / "right.png")

right_button = Button(
    image=right_image,
    borderwidth=0,
    highlightthickness=0,
    command=known_word
)

right_button.place(x=575, y=560)

next_card()

window.mainloop()
