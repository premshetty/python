import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk

def convert():
    input = entry_int.get()
    output_string.set( input * 1.61)
  

# window 
window = ttk.Window(themename='darkly')
window.title('Mile to KiloMeter Convertor')
window.geometry('300x150')


# title
title_label = ttk.Label(master=window , text='Miles to KM convertor' ,  font='calibri 24 bold')
title_label.pack()

# input field 


input_frame = ttk.Frame(master=window)
entry_int= tk.IntVar()
entry= ttk.Entry(master=input_frame , textvariable=entry_int)
button = ttk.Button(master=input_frame, text='convert' , command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output

output_string = tk.StringVar()
output_label = ttk.Label(master=window , text='output' , font='calbiri 24', textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()