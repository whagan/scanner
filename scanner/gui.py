import os
import sys

from tkinter import * 
from tkinter import filedialog


class Gui(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Statement Scanner")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        select = Button(self, text="Select PDF File", command=self.browse)
        select.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky=E+W+S+N)
        close = Button(self, text="Close", command=sys.exit)
        close.grid(row=5, column=3)
    
    def browse(self, *args):
        filename = filedialog.askopenfilename(initialdir='C:/Users/', title='Select a PDF file', filetypes=[('PDF Files', '*.pdf')])
        print(filename)
