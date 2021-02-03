from tkinter import * 
from scanner.gui import Gui


def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Gui()
    root.mainloop()
    