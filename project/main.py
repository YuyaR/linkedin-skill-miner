import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from link_scraper import LinkScraper
from skill_mining import TextMiner
import skill_mining


class MainWindow(tk.Frame):

    def browse():
        filename = fd.askopenfilename()
        pathbar.insert(tk.END, filename)

    def run():
        progress.start()
        progresstext.insert('end', 'job started...')

        job = jobbar.get()
        loc = locbar.get()
        chp = pathbar.get()

        task = LinkScraper(job, loc, chp)
        task.scrape()  # stores finding in a dataframe in the current directory

        progresstext.insert('end', 'busy getting all them jobs...')

        progresstext.insert('end', 'almost there...')

        task2 = TextMiner(chp)
        task2.getText()  # return a barplot of frequency of occurrence for each key skill

        progress.stop()

    def Layout(self):
        msg = '''
        Welcome to Career Skill Miner!
        Just enter your dream career and location
         to see the skills in this field.
        '''
        welc = tk.Text(self.root, height=6, width=60, wrap='word')
        welc.grid(row=0, column=0, columnspan=2, sticky='n')
        welc.insert('end', msg)
        welc.config(state='disabled')

        joblb = tk.Label(text='Job name: ')
        joblb.grid(row=2, column=0, sticky='w')
        jobbar = tk.Entry(self.root, width=50)
        jobbar.grid(row=3, column=0, sticky='w')

        loclb = tk.Label(text='Location: ')
        loclb.grid(row=4, column=0, sticky='w')
        locbar = tk.Entry(self.root, width=50)
        locbar.grid(row=5, column=0, sticky='w')

        pathlb = tk.Label(text='Select your ChromeDriver: ')
        pathlb.grid(row=6, column=0, columnspan=2, sticky='w')
        pathbar = tk.Entry(self.root, width=40)
        pathbar.grid(row=7, column=0, sticky='w')

        browsebt = tk.Button(self.root, text='browse', command=self.browse)
        browsebt.grid(row=7, column=0, sticky='e')

        progresstext = tk.Text(self.root, height=1, width=60)
        progresstext.grid(row=9, column=0)
        progress = ttk.Progressbar(self.root, orient='horizontal',
                                   mode='indeterminate', length=400)
        progress.grid(row=10, column=0)

        runbutton = tk.Button(self.root, text='Start mining', command=self.run)
        runbutton.grid(row=11, column=0, sticky='e')

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        self.root.title('Career Skill Miner 1.0')
        self.root.config(bg='azure')

        self.Layout()


if __name__ == '__main__':
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()
