
from tkinter import *
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master

root = Tk()
app = Frame(root)

root.wm_title("Tkinter Window")
root.mainloop()