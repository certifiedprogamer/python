from tkinter import *
from random import *
from tkinter import filedialog
from tkinter import ttk
from utilities import *
import rps_player as Player
import csv
import os
import itertools
import time

wins = 0
losses = 0
ties = 0


class RPSTournament:
    def __init__(self, window: Tk):
        self.root = window
        self.root.title("RPS tournament")

        frame_ = Frame(self.root,)
        frame_.grid(row=0, column=0, pady=2)
        file_button = Button(frame_, text="Select File",
                             width=10, command=self.open_file)
        file_button.pack(side=TOP, anchor=NW, padx=2, pady=2)
        folder_button = Button(frame_, text="Select Folder", width=10,
                               command=self.open_folder)
        folder_button.pack(side=LEFT, anchor=NW, padx=2, pady=2)
        run_button = Button(
            frame_, text="Run Tournament", command=self.tournamentloop)
        run_button.pack(anchor=NW)

        frame_speed = Frame(
            self.root,)
        frame_speed.grid(row=1, column=0, pady=2)

        label_speed = Label(frame_speed, text="Speed").pack(
            side=LEFT,)
        self.scale = Scale(frame_speed,
                           from_=0.01,
                           to=1,
                           tickinterval=0,
                           resolution=0.01,
                           length=100,
                           orient="horizontal")
        self.scale.pack(side=LEFT, anchor=S)

        self.add_image()

        self.add_info()

        frame_text = Frame(self.root)
        frame_text.grid()
        self.scrollbar = ttk.Scrollbar(
            frame_text, orient='vertical')
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_area = Text(frame_text)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.text_area.config(state=DISABLED)
        self.text_area.pack()
        self.RPSPlayers = []

    def add_image(self):
        self.photo_rock = PhotoImage(file=r".\rps_resources\rock100.png")
        self.photo_paper = PhotoImage(file=r".\rps_resources\paper100.png")
        self.photo_scissors = PhotoImage(
            file=r".\rps_resources\scissors100.png")
        self.photo_unknown = PhotoImage(file=r".\rps_resources\tbd100.png")

        frame_vs = Frame(self.root, width=400, height=30,
                         highlightbackground="black", highlightthickness=3)
        frame_vs.grid_propagate(False)
        frame_vs.grid(row=2, column=0, pady=2)

        self.label_player1 = Label(frame_vs,
                                   image=self.photo_unknown,
                                   compound="top",
                                   pady=15,
                                   padx=25)
        self.label_player1.pack(side=LEFT)

        label_vs = Label(frame_vs,
                         font=("Arial", 20),
                         text="VS", padx=5, pady=5)
        label_vs.pack(side=LEFT)

        self.label_player2 = Label(frame_vs,
                                   image=self.photo_unknown,
                                   compound="top",
                                   pady=15,
                                   padx=25)
        self.label_player2.pack(side=LEFT)

    def add_info(self):
        frame_players = Frame(self.root, width=40, height=30,
                              highlightbackground="black", highlightthickness=3)
        frame_players.grid_propagate(True)
        frame_players.grid(row=3, column=0, pady=2)
        self.label_playervsplayer = Label(frame_players, width=30,
                                          fg="red",
                                          text="")
        self.label_playervsplayer.pack(side=TOP)
        self.label_winner = Label(frame_players, width=30,
                                  fg="blue",
                                  text="")
        self.label_winner.pack(side=TOP)

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".mrps", filetypes=[
            ("multi rock paper scissors", "*.mrps")])
        if file:
            self.text_area.config(state=NORMAL)
            content = csv.reader(file)
            self.RPSPlayers = []
            self.text_area.delete(1.0, END)
            for player in content:
                self.RPSPlayers.append(
                    Player.Player(player))
                self.text_area.insert(1.0, f"{player[0]} \n")
                print(player)
            for i in self.RPSPlayers:
                pass
            self.text_area.insert(1.0, f"Loaded the following Players: \n")
            self.text_area.config(state=DISABLED)

    def open_folder(self):
        directory = filedialog.askdirectory()
        if directory:
            files = os.listdir(directory)
            self.text_area.config(state=NORMAL)
            # Filter files if needed (e.g., open only text files)
            files = [f for f in files if f.endswith('.rps')]
            self.RPSPlayers = []
            self.text_area.delete(1.0, END)
            for file_name in files:
                file_path = os.path.join(directory, file_name)
                with open(file_path, 'r') as file:
                    content = csv.reader(file)
                    for player in content:
                        self.text_area.insert(1.0, f"{player[0]} \n")
                        self.RPSPlayers.append(
                            Player.Player(player))
                        print(player)
            self.text_area.insert(1.0, f"Loaded the following Players: \n")
            self.text_area.config(state=DISABLED)

    def tournament():
        win = Toplevel()
        other_win = RPSTournament(win)

    def image_changer(self, play1, play2):
        if play1 == "Rock":
            self.label_player1.config(image=self.photo_rock)
        elif play1 == "Paper":
            self.label_player1.config(image=self.photo_paper)
        elif play1 == "Scissors":
            self.label_player1.config(image=self.photo_scissors)
        if play2 == "Rock":
            self.label_player2.config(image=self.photo_rock)
        elif play2 == "Paper":
            self.label_player2.config(image=self.photo_paper)
        elif play2 == "Scissors":
            self.label_player2.config(image=self.photo_scissors)

    def tournamentloop(self):
        combination_length = 2
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        for combination in itertools.combinations(self.RPSPlayers, combination_length):
            p1_total_wins = 0
            p2_total_wins = 0
            self.label_playervsplayer.config(
                text=f"{combination[0].name} vs. {combination[1].name}")
            self.text_area.config(state=NORMAL)
            self.text_area.insert(
                1.0, f" ***** {combination[0].name} vs. {combination[1].name} ***** \n")
            self.text_area.config(state=DISABLED)
            Tk.update(self.root)
            time.sleep(self.scale.get())
            for i in range(len(combination[1].plays)):
                combination[0].plays[i] = Utilities.convert_to_play(
                    combination[0].plays[i])
                combination[1].plays[i] = Utilities.convert_to_play(
                    combination[1].plays[i])
                winner = Utilities.determine_winner(
                    combination[0].plays[i], combination[1].plays[i])
                print(winner)
                self.text_area.config(state=NORMAL)
                self.text_area.insert(
                    1.0, f"{combination[0].name} plays {combination[0].plays[i]}, {combination[1].name} plays {combination[1].plays[i]}\n")
                if winner == 1:
                    self.text_area.insert(
                        1.0, f"{combination[0].name} won!\n")
                    p1_total_wins += 1
                    combination[0].wins += 1
                    combination[1].losses += 1
                    self.label_winner.config(
                        text=f"{combination[0].name} won!")
                elif winner == 0:
                    self.text_area.insert(1.0, f"It's a tie!\n")
                    combination[0].ties += 1
                    combination[1].ties += 1
                    self.label_winner.config(text=f"It's a tie!")
                elif winner == -1:
                    p2_total_wins += 1
                    self.text_area.insert(
                        1.0, f"{combination[1].name} won!\n")
                    combination[1].wins += 1
                    combination[0].losses += 1
                    self.label_winner.config(
                        text=f"{combination[1].name} won!")
                self.text_area.config(state=DISABLED)
                self.image_changer(
                    combination[0].plays[i], combination[1].plays[i])
                Tk.update(self.root)
                time.sleep(self.scale.get())
            if p1_total_wins > p2_total_wins:
                combination[0].series_wins += 1
            elif p2_total_wins > p1_total_wins:
                combination[1].series_wins += 1
        for i in self.RPSPlayers:
            i.calculate_score()
            print(i)
        highest_win = [1, []]
        highest_score = [1.0, []]
        highest_series_wins = [1, []]
        for i in self.RPSPlayers:
            try:
                if i.wins > highest_win[0]:
                    highest_win[0] = i.wins
                    highest_win[1] = [i.name]
                elif i.wins == highest_win[0]:
                    highest_win[1].append(i.name)
            except:
                highest_win = [i]
        for i in self.RPSPlayers:
            try:
                if i.score > highest_score[0]:
                    highest_score[0] = i.score
                    highest_score[1] = [i.name]
                elif i.score == highest_score[0]:
                    highest_score[1].append(i.name)
            except:
                highest_score = [i]
        for i in self.RPSPlayers:
            try:
                if i.series_wins > highest_series_wins[0]:
                    highest_series_wins[0] = i.series_wins
                    highest_series_wins[1] = [i.name]
                elif i.series_wins == highest_series_wins[0]:
                    highest_series_wins[1].append(i.name)
            except:
                highest_series_wins = [i]
        self.text_area.config(state=NORMAL)
        for i in self.RPSPlayers:
            self.text_area.insert(
                1.0, f"{i}\n")
        highest_score[1] = "/".join(highest_score[1])
        highest_win[1] = "/".join(highest_win[1])
        highest_series_wins[1] = "/".join(highest_series_wins[1])
        self.text_area.insert(
            1.0, f"{highest_win[1]} had the most wins! ({highest_win[0]})\n")
        self.text_area.insert(
            1.0, f"{highest_score[1]} had the highest score! ({highest_score[0]})\n")
        self.text_area.insert(1.0, f"{highest_series_wins[1]} had the most series wins! ({
                              highest_series_wins[0]})\n")
        self.text_area.config(state=DISABLED)
        print(highest_score[1])

        # print(combination[0].plays[i])
        # print(combination[1].plays[i])


if __name__ == "__main__":
    window = Tk()
    RPSTournament.tournament()
    window.mainloop()
