import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('WindowPython')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text='Hi new window')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='Okay', command=set_message)
ok_button.pack()

window.mainloop()