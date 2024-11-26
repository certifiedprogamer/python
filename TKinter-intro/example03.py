# checkboxes
import tkinter as tk


def grade_submission():
    kraft = check_kraft.get()
    garbage = check_velveta.get()
    if kraft == 1 and garbage == 0:
        label_outcome.config(text="You are 100% correct!")
    elif kraft == 0 and garbage == 1:
        label_outcome.config(text="192.168.111.11")
    else:
        label_outcome.config(text="You're partially correct.")
    checkbox_velveta.config(state=tk.DISABLED)
    checkbox_kraft.config(state=tk.DISABLED)


window = tk.Tk()
window.title("survey")
window.geometry("500x500")

# variable to hold the state of the checkbox
check_kraft = tk.IntVar()

checkbox_kraft = tk.Checkbutton(window,
                                text="Kraft mac and cheese is good",
                                variable=check_kraft)
checkbox_kraft.pack()

check_velveta = tk.IntVar()

checkbox_velveta = tk.Checkbutton(window,
                                  text="Velveta mac and cheese is good",
                                  variable=check_velveta)
checkbox_velveta.pack()

button_submit = tk.Button(window, text="Submit", command=grade_submission)
button_submit.pack()

label_outcome = tk.Label(window, text="Please submit your response")
label_outcome.pack()

window.mainloop()
