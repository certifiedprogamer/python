import tkinter as tk

window = tk.Tk()
window.title("Mario")
window.geometry("400x400")


def add_character():
    item = entry.get().strip()
    if item and not item in listbox.get(0, tk.END):
        listbox.insert(tk.END, item)


def remove_selected():
    for_del = listbox.get(tk.ACTIVE)
    if for_del:
        listbox.delete(tk.ACTIVE)
        print(f"Deleted {for_del}")
        print(f"Current active: {listbox.get(tk.ACTIVE)}")


listbox = tk.Listbox(window, width=25, height=8,)

listbox.insert(1, "mario")
listbox.insert(2, "luigi")
listbox.select_set(0)

label = tk.Label(text="Enter a character to add: ")
entry = tk.Entry(window)

button = tk.Button(window,
                   text="add character",
                   command=add_character)

button_del = tk.Button(window,
                       text="Remove Selected",
                       command=remove_selected)
listbox.pack()
label.pack()
entry.pack()
button.pack()
button_del.pack()

window.mainloop()
