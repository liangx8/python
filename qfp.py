import tkinter as tk
# for pcb
toInch = 0.0393700787
class SizeEntry(tk.Frame):
    def __init__(self,defVal, master=None):
        super().__init__(master)
        x=tk.Entry(self)
        self.__mm=tk.DoubleVar(self,round(defVal / toInch,2))
        self.__mmOrg=self.__mm.get()
        x["textvariable"]=self.__mm
        x.bind('<Key-Return>',self.__update_inch)
        x.pack(side="left")
        x=tk.Entry(self)
        x.bind('<Key-Return>',self.__update_mm)
        self.__inch=tk.DoubleVar(self,defVal)
        self.__inchOrg=self.__inch.get()
        x["textvariable"]=self.__inch
        x.pack(side="right")
        self.__tri_func=None
    def __update_inch(self,event):

        try:
            x=float(event.widget.get())
            self.__mmOrg=x
            self.__inch.set(round(x * toInch,3))
            if self.__tri_func:
                self.__tri_func()
        except ValueError:
            self.__mm.set(self.__mmOrg)
            return "break"
            
    def __update_mm(self,event):
        try:
            x=float(event.widget.get())
            self.__inchOrg=x
            self.__mm.set(round(x / toInch,2))
            if self.__tri_func:
                self.__tri_func()
        except ValueError:
            self.__inch.set(self.inchOrg)
            return "break"
    def __set_inch(self,_):
        pass
    def __get_inch(self):
        return self.__inch.get()
    def trigger(self,func=None):
        self.__tri_func=func
    inch = property(__get_inch,__set_inch)
    
class QFPWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def draw(self):
        print("X length:{}".format(self.xlen.inch))
        print("Y length:{}".format(self.ylen.inch))
    def draw_event(self,event):
        self.draw()
    def create_widgets(self):
        
        x = tk.Label(self,text="Pitch")
        x.grid(column =0,row=1,columnspan=2)
        self.pitch = SizeEntry(0.031,self)
        self.pitch.grid(column=2,row=1)
        self.pitch.trigger(self.draw)

        x = tk.Label(self,text="Pad Width")
        x.grid(column =0,row=2,columnspan=2)
        self.padw = SizeEntry(.02,self)
        self.padw.grid(column=2,row=2)
        self.padw.trigger(self.draw)
        
        x = tk.Label(self,text="Pad Length")
        x.grid(column =0,row=3,columnspan=2)
        self.padl = SizeEntry(.025,self)
        self.padl.grid(column=2,row=3)
        self.padl.trigger(self.draw)

        
        self.rx = tk.Entry(self)
        self.rx["textvariable"]=tk.IntVar(self,8)
        self.rx.grid(column=0,row=4)
        x=tk.Label(self,text="X Length")
        x.grid(column=1,row=4)
        self.xlen = SizeEntry(.2,self)
        self.xlen.grid(column=2,row=4)
        self.xlen.trigger(self.draw)
        self.rx.bind("<Key-Return>",self.draw_event)

        self.ry = tk.Entry(self)
        self.ry["textvariable"]=tk.IntVar(self,8)
        self.ry.grid(column=0,row=5)
        self.ry.bind("<Key-Return>",self.draw_event)
        x=tk.Label(self,text="Y Length")
        x.grid(column=1,row=5)
        self.ylen = SizeEntry(.2,self)
        self.ylen.grid(column=2,row=5)
        self.ylen.trigger(self.draw)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(column=0,row=6,columnspan=2)
        self.gen = tk.Button(self,text="Generate")
        self.gen.grid(column=2,row=6)
        cv = tk.Canvas(self,width=300,height=300)
        cv.grid(column=0,columnspan=3,row=7)
        cv.create_rectangle(0,0,300,300,fill="white")
        self.draw()

if __name__=="__main__":
    root = tk.Tk()
    app = QFPWindow(master=root)
    app.master.title("QFP package generator")
    app.mainloop()
