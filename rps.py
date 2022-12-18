import tkinter as tk              # Tkinter: For creating interactive game
from PIL import Image, ImageTk    # Pillow Module or PIL: To add image in tkinter window
import random                     # Random Module: To randomize Computer's choice


# Window setup
root = tk.Tk()                         # Game Window
root.configure(bg="#92b4ec")           # Window's Background Colour
root.minsize(width=900, height=500)    # MInimum Window Size
root.wm_title("Rock Paper Scissor")


# Scores
score_u = 0    # User's Score
score_c = 0    # Computer's Score


# Frames
you_tframe = tk.Frame(root)      # You Title Frame
comp_tframe = tk.Frame(root)     # Computer Title Frame
title_frame = tk.Frame(root)     # Main Title Frame
user_oframe = tk.Frame(root)     # User Output Frame
comp_oframe = tk.Frame(root)     # Computer Title Frame
result_frame = tk.Frame(root)    # Result Frame


# Images
qmark = ImageTk.PhotoImage(Image.open(
    fr"resources\que_mark.png"))         # Question Mark Image
you_img = ImageTk.PhotoImage(Image.open(
    fr"resources\you.png"))              # You Word Image
comp_img = ImageTk.PhotoImage(Image.open(
    fr"resources\computer.png"))         # Computer Word Image
title = ImageTk.PhotoImage(Image.open(
    fr"resources\rps_title.png"))        # Title Image
rock_ = ImageTk.PhotoImage(Image.open(
    fr"resources\rock.png"))             # Rock Hand Sign
paper_ = ImageTk.PhotoImage(Image.open(
    fr"resources\paper.png"))            # Paper Hand Sign
scissor_ = ImageTk.PhotoImage(Image.open(
    fr"resources\scissor.png"))          # Scissor Hand Sign


# Labels
you_label = tk.Label(you_tframe, image=you_img, bg="#92b4ec")
comp_label = tk.Label(comp_tframe, image=comp_img, bg="#92b4ec", fg="white")
title_label = tk.Label(title_frame, image=title, bg="#92b4ec")
user_olabel = tk.Label(user_oframe, image=qmark, bg="#92b4ec")
comp_olabel = tk.Label(comp_oframe, image=qmark, bg="#92b4ec")
score = tk.Label(
    root,
    text=f'Score\nYou:{score_u}\nComputer:{score_c}',
    font=("consolas", 12, "bold"),
    bg="#92b4ec",
    fg="white"
)
kb = tk.Label(root,
                text='   Key Bindings   \nr     - Rock\np     - Paper\ns     - Scissor\nspace - Change  \n        Difficulty\ne     - Exit',
                font=("consolas", 11, "bold"),
                borderwidth=2, relief="solid",
                bg="#92b4ec",
                fg="white",
                justify="left"
                )
result_label = tk.Label(result_frame, bg="#92b4ec")


# Keyboard Input
def r_key(event):
    r()
root.bind("<r>", r_key)


def p_key(event):
    p()
root.bind("<p>", p_key)


def s_key(event):
    s()
root.bind("<s>", s_key)


def _diff(event):
    difficulty()
root.bind("<space>", _diff)


def exit(event):
    root.destroy()
root.bind("<e>", exit)


# Functions
# Difficulty of the Session
def difficulty():
    global diff
    diff.pack_forget()
    if diff["text"] == "Easy":
        diff["text"] = "Medium"
    elif diff["text"] == "Medium":
        diff["text"] = "Hard"
    elif diff["text"] == "Hard":
        diff["text"] = "Easy"


# Computer's Choice
def choice_(a):
    opt = ["rock", "paper", "scissor"]
    if diff["text"] == "Easy":
        x = opt[random.randint(0, 2)]
        return x
    if diff["text"] == "Medium":
        opt += [a, a]
        x = opt[random.randint(0, 4)]
        return x
    if diff["text"] == "Hard":
        opt += [a, a, a, a]
        x = opt[random.randint(0, 6)]
        return x


# Result Displaying Frame Editor
def result(a, b):
    global result_label, score_u, score_c
    result_label.pack_forget()
    score.pack_forget()
    score_u += 1
    if a == b:
        resimg = "tie"
    elif a == "paper" and b == "rock":
        resimg = "you_won"
        score["text"] = f'Score\nYou:{score_u}\nComputer:{score_c}'
    elif a == "scissor" and b == "paper":
        resimg = "you_won"
        score["text"] = f'Score\nYou:{score_u}\nComputer:{score_c}'
    elif a == "rock" and b == "scissor":
        resimg = "you_won"
        score["text"] = f'Score\nYou:{score_u}\nComputer:{score_c}'
    else:
        resimg = "you_lost"
        score_u -= 1
        score_c += 1
        score["text"] = f'Score\nYou:{score_u}\nComputer:{score_c}'
    rimg = ImageTk.PhotoImage(Image.open(fr"resources\{resimg}.png"))
    result_label.configure(image=rimg)
    result_label.image = rimg


# Command For Rock Button
def r():
    global user_olabel, comp_olabel
    user_olabel.pack_forget()
    comp_olabel.pack_forget()
    choice = choice_("paper")
    cimg = ImageTk.PhotoImage(Image.open(fr"resources\{choice}.png"))
    user_olabel.configure(image=rock_)
    user_olabel.image = rock_
    comp_olabel.configure(image=cimg)
    comp_olabel.image = cimg
    result("rock", choice)
    return


# Command For Paper Button
def p():
    global user_olabel, comp_olabel
    user_olabel.pack_forget()
    comp_olabel.pack_forget()
    choice = choice_("scissor")
    cimg = ImageTk.PhotoImage(Image.open(fr"resources\{choice}.png"))
    user_olabel.configure(image=paper_)
    user_olabel.image = paper_
    comp_olabel.configure(image=cimg)
    comp_olabel.image = cimg
    result("paper", choice)
    return


# Command For Scissor Button
def s():
    global user_olabel, comp_olabel
    user_olabel.pack_forget()
    comp_olabel.pack_forget()
    choice = choice_("rock")
    cimg = ImageTk.PhotoImage(Image.open(fr"resources\{choice}.png"))
    user_olabel.configure(image=scissor_)
    user_olabel.image = scissor_
    comp_olabel.configure(image=cimg)
    comp_olabel.image = cimg
    result("scissor", choice)
    return


# Buttons
rock = tk.Button(root, text='Rock', font=("consolas", 10, "bold"),
                    command=r, width=8, height=2, bg="#ffe69a", fg="blue", borderwidth=0.1)
paper = tk.Button(root, text='Paper', font=("consolas", 10, "bold"),
                    command=p, width=8, height=2, bg="#ffe69a", fg="blue", borderwidth=0.1)
scissor = tk.Button(root, text='Scissor', font=("consolas", 10, "bold"),
                    command=s, width=8, height=2, bg="#ffe69a", fg="blue", borderwidth=0.1)
diff = tk.Button(root, text='Easy', font=("consolas", 10, "bold"), command=difficulty,
                    width=12, height=2, bg="#ffe69a", fg="blue", borderwidth=0.1)


# Pack of Frames
you_tframe.pack()
comp_tframe.pack()
you_label.pack()
comp_label.pack()
title_frame.pack()
title_label.pack()
user_oframe.pack()
comp_oframe.pack()
user_olabel.pack()
comp_olabel.pack()
result_frame.pack()
result_label.pack()


# Placements
you_tframe.place(anchor="center", relx=0.275, rely=0.85)
comp_tframe.place(anchor="center", relx=0.725, rely=0.85)
title_frame.place(anchor="center", relx=0.5, rely=0.2)
result_frame.place(anchor="center", relx=0.5, rely=0.5)
user_oframe.place(anchor="center", relx=0.275, rely=0.6)
comp_oframe.place(anchor="center", relx=0.725, rely=0.6)
score.place(anchor="center", relx=0.5, rely=0.4)
kb.place(anchor="center", relx=0.085, rely=0.864)
rock.place(anchor="center", relx=0.5, rely=0.6)
paper.place(anchor="center", relx=0.5, rely=0.68)
scissor.place(anchor="center", relx=0.5, rely=0.76)
diff.place(anchor="center", relx=0.5, rely=0.9)
user_olabel.grid()
comp_olabel.grid()
result_label.grid()


root.mainloop()