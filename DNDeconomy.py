import tkinter
import sys
import tkinter.messagebox
class App:

    def __init__(self, master):

        frame = tkinter.Frame(master)
        frame.pack()

        self.button = tkinter.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=tkinter.LEFT)

        self.hi_there = tkinter.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)
        
        self.iLikeOnions = tkinter.Button(frame, text = "onions?", command = self.onions)
        self.iLikeOnions.pack(side=tkinter.LEFT)

    def say_hi(self):
        print("hi there, everyone!")
        
    def onions(self):
        tkinter.messagebox.showwarning("I Like Onions!!!!", "DO you LIKE onions?")

root = tkinter.Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below

