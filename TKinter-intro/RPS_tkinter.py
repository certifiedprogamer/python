from tkinter import *
from random import *


wins = 0
losses = 0
ties = 0


def update_label():
    choice = player_choice.get()
    if choice == "1":
        label_player.config(image=photo_rock)
    elif choice == "2":
        label_player.config(image=photo_paper)
    elif choice == "3":
        label_player.config(image=photo_scissors)
    label_computer.config(image=photo_unknown)


def start():
    p_choice = int(player_choice.get())
    computer_choice = randint(1, 3)
    if computer_choice == 1:
        label_computer.config(image=photo_rock)
    elif computer_choice == 2:
        label_computer.config(image=photo_paper)
    elif computer_choice == 3:
        label_computer.config(image=photo_scissors)
    outcome_check(p_choice, computer_choice)
    score = f"Wins: {wins} Losses: {losses} Ties: {ties}"
    label_score.config(text=score)


def outcome_check(player_choice, computer_choice):
    """Determines the outcome of the last round."""
    global wins
    global losses
    global ties
    if player_choice == 1 and computer_choice == 3:
        label_round.config(text="You win!")
        wins += 1
    elif player_choice == 2 and computer_choice == 1:
        label_round.config(text="You win!")
        wins += 1
    elif player_choice == 3 and computer_choice == 2:
        label_round.config(text="You win!")
        wins += 1
    elif computer_choice == 1 and player_choice == 3:
        label_round.config(text="You lost!")
        losses += 1
    elif computer_choice == 2 and player_choice == 1:
        label_round.config(text="You lost!")
        losses += 1
    elif computer_choice == 3 and player_choice == 2:
        label_round.config(text="You lost!")
        losses += 1
    else:
        label_round.config(text="It's a tie!")
        ties += 1


def reset():
    global wins
    global losses
    global ties
    wins = 0
    losses = 0
    ties = 0
    score = f"Wins: {wins} Losses: {losses} Ties: {ties}"
    label_score.config(text=score)
    label_computer.config(image=photo_unknown)


score = f"Wins: {wins} Losses: {losses} Ties: {ties}"

default_font = ("Arial", 15)
window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")

frame_radio = Frame(window, bg="green", width=400, height=30)
frame_radio.grid_propagate(False)
frame_radio.pack()
window.grid_columnconfigure(0, weight=1)

frame_vs = Frame(window, width=400, height=30)
frame_vs.grid_propagate(False)
frame_vs.pack()


frame_score = Frame(window, width=400, height=30)
frame_score.grid_propagate(False)
frame_score.pack()

frame_buttons = Frame(window, width=400, height=30)
frame_buttons.grid_propagate(False)
frame_buttons.pack()


player_choice = StringVar(value="1")

Radiobutton(frame_radio, text="Rock", font=default_font,
            variable=player_choice, value="1", command=update_label).pack(side=LEFT)
Radiobutton(frame_radio, text="Paper", font=default_font,
            variable=player_choice, value="2", command=update_label).pack(side=LEFT)
Radiobutton(frame_radio, text="Scissors", font=default_font,
            variable=player_choice, value="3", command=update_label).pack(side=LEFT)

photo_rock = PhotoImage(file=r".\rps_resources\rock100.png")
photo_paper = PhotoImage(file=r".\rps_resources\paper100.png")
photo_scissors = PhotoImage(file=r".\rps_resources\scissors100.png")
photo_unknown = PhotoImage(file=r".\rps_resources\tbd100.png")


label_player = Label(frame_vs,
                     image=photo_rock,
                     compound="top",
                     bd=20,
                     relief=RAISED,
                     pady=15,
                     padx=25)
label_player.pack(side=LEFT)

label_vs = Label(frame_vs,
                 font=("Arial", 20),
                 text="VS", padx=5, pady=5)
label_vs.pack(side=LEFT)

label_computer = Label(frame_vs,
                       image=photo_unknown,
                       compound="top",
                       bd=20,
                       relief=RAISED,
                       pady=15,
                       padx=25)
label_computer.pack(side=LEFT)

label_round = Label(frame_score,
                    font=("Arial", 20, "bold"),
                    text="Make your move!",
                    bd=20,
                    pady=5,
                    padx=5)
label_round.pack(side=TOP)

label_score = Label(frame_score,
                    font=default_font,
                    text=score)
label_score.pack(side=TOP)

play_button = Button(frame_buttons, command=start, text="Play",)
play_button.pack(side=LEFT, padx=5, pady=5)

reset_button = Button(frame_buttons, command=reset,
                      text="Reset scores",)
reset_button.pack(side=LEFT, padx=5, pady=5)

window.mainloop()
