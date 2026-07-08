from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv(r"data\french_words.csv")
french_words = data["French"].tolist()
english_words = data["English"].tolist()
random_num = 0
french_word = french_words[random_num]
english_word = english_words[random_num]
flip_timer = None

#-----------------------------------------------------------------------------------------Card_Save-----------------------------------------------------------------------------------------#
def memorized():
    global random_num, english_word, french_word
    english_words.remove(english_word)
    french_words.remove(french_word)

    new_word()

#-----------------------------------------------------------------------------------------Word Bank-----------------------------------------------------------------------------------------#
def new_word():
    global french_word, random_num, flip_timer, english_word

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    random_num += 1
    french_word = french_words[random_num]
    english_word = english_words[random_num]

    canvas.itemconfig(word, text=french_word)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(image, image=card_front)

    flip_timer = window.after(3000, flip_card)

#------------------------------------------------------------------------------------------UI Setup-----------------------------------------------------------------------------------------#
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=1000, height=800)

card_back = PhotoImage(file=r"images\card_back.png")
card_front = PhotoImage(file=r"images\card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
canvas.pack()

right_image = PhotoImage(file=r"images\right.png")
right = Button(image=right_image, highlightthickness=0, command=memorized)
right.place(x=575, y=560)

wrong_image = PhotoImage(file=r"images\wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong.place(x=200, y=560)

#------------------------------------------------------------------------------------------Card Flip----------------------------------------------------------------------------------------#
def flip_card():
    global english_word
    
    canvas.itemconfig(word, text=english_word)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(image, image=card_back)

window.mainloop()

