from tkinter import Button, Label, Entry, Frame

def create_entry(root, x, y, show=None, height=25):
    entry = Entry(root, show=show)
    entry.place(x=x, y=y, height=height)
    return entry

def create_label(root, text, x, y, fg="White", bg="Brown", font="Times"):
    label = Label(root, text=text, fg=fg, bg=bg, font=font)
    label.place(x=x, y=y)
    return label

def create_button(frame, x, y, text, bcolor, fcolor, command, width=42, height=4):
    def on_enter(e):
        button['background'] = bcolor
        button['foreground'] = fcolor

    def on_leave(e):
        button['background'] = fcolor
        button['foreground'] = bcolor

    button = Button(frame, width=width, height=height, text=text, fg=bcolor, bg=fcolor, border=0,
                    activeforeground=fcolor, activebackground=bcolor, command=command)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.place(x=x, y=y)
    return button
