from tkinter import *
from random import *
from tkinter import filedialog
from tkinter import ttk
import rps_player as Player
import csv
import os
import itertools


wins = 0
losses = 0
ties = 0


class RPSTournament:
    def __init__(self, window: Tk):
        self.root = window
        self.root.title("RPS tournament")
        self.root.geometry("500x500")

        frame_ = Frame(self.root,)
        frame_.grid_propagate(False)
        frame_.pack()
        file_button = Button(frame_, text="Select File",
                             width=10, command=self.open_file)
        file_button.pack(side=TOP, anchor=NW, padx=2, pady=2)
        folder_button = Button(frame_, text="Select Folder", width=10,
                               command=self.open_folder)
        folder_button.pack(side=LEFT, anchor=NW, padx=2, pady=2)
        run_button = Button(
            frame_, text="Run Tournament", command=self.tournamentloop)
        run_button.pack(anchor=NW)

        frame_speed = Frame(self.root,)
        frame_speed.grid_propagate(False)
        frame_speed.pack(pady=2)

        label_speed = Label(frame_speed, text="Speed").pack(
            side=LEFT,)
        scale = Scale(frame_speed,
                      from_=0,
                      to=1,
                      tickinterval=0,
                      resolution=0.01,
                      length=100,
                      orient="horizontal").pack(side=LEFT, anchor=S)

        self.add_image()

        self.add_info()

        self.scrollbar = ttk.Scrollbar(
            self.root, orient='vertical')
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_area = Text(self.root)
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
                         border=5, relief=RIDGE)
        frame_vs.grid_propagate(False)
        frame_vs.pack(pady=2)

        self.label_player1 = Label(frame_vs,
                                   image=self.photo_rock,
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
        frame_players = Frame(self.root, width=600, height=30,
                              border=5, relief=RIDGE)
        frame_players.pack(pady=2)

        self.label_playervsplayer = Label(frame_players,
                                          fg="red",
                                          text="                                                                     ")
        self.label_playervsplayer.pack(side=TOP)
        self.label_winner = Label(frame_players,
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
            for player in content:
                self.RPSPlayers.append(
                    Player.Player(player))
                print(player)
            self.text_area.delete(1.0, END)
            for i in self.RPSPlayers:
                self.text_area.insert(1.0, f"{i} \n")
            self.text_area.insert(1.0, f"Loaded the following Players \n")
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
            self.text_area.insert(1.0, f"Loaded the following Players \n")
            self.text_area.config(state=DISABLED)

    def tournament():
        win = Toplevel()
        other_win = RPSTournament(win)

    def tournamentloop(self):
        combination_length = 2
        for combination in itertools.combinations(self.RPSPlayers, combination_length):
            print(f"{combination[0].name} vs {combination[1].name}")
            for i in range(len(combination[0].plays)):
                print(combination[0].plays[i], combination[1].plays[i])


if __name__ == "__main__":
    window = Tk()
    RPSTournament.tournament()
    window.mainloop()
