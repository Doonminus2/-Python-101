import tkinter as tk

def set_message():
    text =text_input.get(())
    title_label.configure(text=text)

Windows = tk.Tk()
Windows.title('testpython')
Windows.minsize(width=400, height=400)

title_label = tk.Label(master=Windows, text='ตอนนี้มีความสุข')
title_label.pack()

text_input = tk.Entry(master=Windows)
title_label.pack()

ok_button = tk.Button(master=Windows, text='ดีมาก', command=set_message)
title_label.pack()

Windows.maninloop()