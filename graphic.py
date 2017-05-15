import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        self.tree = ttk.Treeview(self,text="a")
        self.tree.pack(side="bottom")
        

    def say_hi(self):
        print("hi there, everyone!")
        print("root children:{}".format(self.tree.get_children()))
if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
