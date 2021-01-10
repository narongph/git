import tkinter as tk

def show_output():
    nb = int(nb_input.get())
    if nb==0:
        output_label.configure(text='Wrong number')
        return

    output = ''
    for i in range(1,13):
        output += str(nb) + ' x '  + str(i)
        output += ' = ' + str(nb*i) + '\n'
    output_label.configure(text=output)
    
window = tk.Tk()
window.title('WindowPython')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)

nb_input = tk.Entry(master=window, width=15)
nb_input.pack()

go_button = tk.Button(
    master=window, text='go',
    command=show_output, width=15, height=2
    )
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()

#----------------------------------------------------------