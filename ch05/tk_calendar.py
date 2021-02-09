import calendar
import tkinter as tk

c = calendar.TextCalendar()
m = c.formatmonth(2021, 3)

root = tk.Tk()
t = tk.Text(root, height=7, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
