import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from link_scraper import LinkScraper
from skill_mining import TextMiner
import skill_mining


root = tk.Tk()

root.title('Career Skill Miner 1.0')
root.config(bg='azure')
root.geometry('500x350')

msg = '''Welcome to Career Skill Miner!
Just enter your dream career and location and 
we can show you the top 10 wanted skills in this field.
'''
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

pathlb = tk.Label(text='Select your ChromeDriver: ')
pathlb.grid(row=6, column=0, columnspan=2, sticky='w')
pathbar = tk.Entry(root, width=40)
pathbar.grid(row=7, column=0, sticky='w')

def browse():
    filename = fd.askopenfilename()
    pathbar.insert(tk.END, filename)

browsebt = tk.Button(root, text='browse', command=browse)
browsebt.grid(row=7, column=0, sticky='e')

progresstext = tk.Text(root, height=1, width=60)
progresstext.grid(row=9, column=0)
progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=400)
progress.grid(row=10, column=0)

def run():
    progress.start()
    progresstext.insert('end', 'job started...')


    job = jobbar.get()
    loc = locbar.get()
    chp = pathbar.get()

    task = LinkScraper(job, loc, chp)
    task.scrape()

    progresstext.insert('end', 'busy getting all them jobs...')

    progresstext.insert('end', 'almost there...')
    
    task2 = TextMiner(chp)
    task2.getText()

    progress.stop()
    k = skill_mining.keywords
    plot(k)

runbutton = tk.Button(root, text='Start mining', command=run)
runbutton.grid(row=11, column=0, sticky='e')

root.mainloop()
