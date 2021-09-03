import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from careerskills.link_scraper import LinkScraper
from careerskills.skill_mining import TextMiner
import sys


class MainWindow(tk.Frame):

    '''
    This class creates a tkinter window that allows users to search for a job title and location on Linkedin
    and discover the frequency of appearance of 10 most common transferable skills in the search. It also allows
    the user to put in their chrome driver's path easily via file browse.

    '''

    def browse(self):
        '''
        This function is used for users to click on browse button and look for their chrome driver in their
        file depository, and then input the absolute path in the entry field which is used for selenium
        webscraping later
        '''
        filename = fd.askopenfilename()
        self.pathbar.insert(tk.END, filename)

    def run(self):
        '''
        This function is run after the user's input on all required fields ('job', 'location', 'chrome path')
        and clicks 'start mining' button. It gathers these inputs and scrapes Linkedin for the links and job
        description texts for the search, and generates a plot at the end for display of result.
        '''
        self.progress.start()
        self.progresstext.insert(tk.END, 'job started...')

        job = self.jobbar.get()
        loc = self.locbar.get()
        chp = self.pathbar.get()

        task = LinkScraper(job, loc, chp)
        self.progresstext.insert('end', 'busy getting all them jobs...')
        task.scrape()  # stores finding in a dataframe in the current directory

        self.progresstext.insert('end', 'almost there...')

        task2 = TextMiner(job, loc, chp)
        task2.getText()  # returns a barplot of frequency of occurrence for each key skill

        self.progress.stop()

    def Layout(self):
        '''
        This function creates the layout of the tkinter window
        '''
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
        self.jobbar = tk.Entry(self.root, width=50)
        self.jobbar.grid(row=3, column=0, sticky='w')

        loclb = tk.Label(text='Location: ')
        loclb.grid(row=4, column=0, sticky='w')
        self.locbar = tk.Entry(self.root, width=50)
        self.locbar.grid(row=5, column=0, sticky='w')

        pathlb = tk.Label(text='Select your ChromeDriver: ')
        pathlb.grid(row=6, column=0, columnspan=2, sticky='w')
        self.pathbar = tk.Entry(self.root, width=40)
        self.pathbar.grid(row=7, column=0, sticky='w')

        browsebt = tk.Button(self.root, text='browse', command=self.browse)
        browsebt.grid(row=7, column=0, sticky='e')

        self.progresstext = tk.Text(self.root, height=1, width=60)
        self.progresstext.grid(row=9, column=0)
        # redirect system error msg to the tkinter text box
        sys.stderr = StderrPrint(self.progresstext)

        self.progress = ttk.Progressbar(self.root, orient='horizontal',
                                        mode='indeterminate', length=400)
        self.progress.grid(row=10, column=0)

        runbutton = tk.Button(self.root, text='Start mining', command=self.run)
        runbutton.grid(row=11, column=0, sticky='e')

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        self.root.title('Career Skill Miner 1.0')
        self.root.config(bg='RoyalBlue1')

        self.Layout()


class StderrPrint:
    '''
    This class prints the standard error output in the text box on the main window
    Attributes:
        text_widget: the text box to show the error msgs
    '''

    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, errmsg):
        '''
        this function whenever called will clear the textbox first then print the msg
        Arg:
            errmsg: the msg to be printed; in this case stderr msgs
        '''
        self.text_widget.insert('1.0', errmsg)


if __name__ == '__main__':
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()
