import tkinter as tk
from tkinter import ttk
from link_scraper import *
from skill_mining import *

root = tk.Tk()
print('im here')

root.title('Career Skill Miner 1.0')
root.config(bg='yellow')
root.geometry('500x300')

msg = '''Welcome to Career Skill Miner!
Just enter your dream career and location and 
we can show you the top 10 wanted skills in this field.
You can also highlight specific skills to see their individual outcome.'''
welc = tk.Text(root, height=6, width=60, wrap='word')
welc.grid(row=0, column=0, columnspan=2, sticky='n')
welc.insert('end', msg)
welc.config(state='disabled')

joblb = tk.Label(text='Job name: ')
joblb.grid(row=2, column=0, sticky='w')
jobbar = tk.Entry(root, width=50)
jobbar.grid(row=3, column=0, sticky='w')

loclb = tk.Label(text='Location: ')
loclb.grid(row=4, column=0, sticky='w')
locbar = tk.Entry(root, width=50)
locbar.grid(row=5, column=0, sticky='w')


progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=400)
progress.grid(row=7, column=0)

def run():
    progress.start()

    job = jobbar.get()
    loc = locbar.get()

    scrape(job, loc)
    mine()

    progress.stop()


run = tk.Button(root, text='Start mining', command=run)
run.grid(row=6, column=0, sticky='e')


root.mainloop()
print('i got to the end')
