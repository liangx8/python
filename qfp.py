import tkinter as tk
# for pcb
toInch = 0.0393700787
cv_xmax = 500
cv_ymax = 500
cv_xmid = int(cv_xmax/2)
cv_ymid = int(cv_ymax/2)

class IntEntry(tk.Entry):
    def __init__(self,val,master=None):
        super().__init__(master)
        self.__val=tk.IntVar(self,val)
        self["textvariable"]=self.__val
        super().bind('<Key-Return>',self.__event_tri)
        self.__valOrg=val
    def trigger(self,func=None):
        self.__tri_func=func
    def __event_tri(self,event):
        try:
            val=self.__val.get()
            self.__valOrg=val
        except:
            self.__val.set(self.__valOrg)
            return "break"
        if self.__tri_func:
            return self.__tri_func()
    def __get_val(self):
        return self.__val.get()
    val=property(fget=__get_val)
        
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
    def __get_inch(self):
        return self.__inch.get()
    def trigger(self,func=None):
        self.__tri_func=func
    inch = property(fget=__get_inch)
    
class QFPWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def draw(self):
        width=int(self.xlen.inch * 1000)
        height=int(self.ylen.inch * 1000)
        self.cv.create_rectangle(0,0,cv_xmax,cv_ymax,fill="grey")
        padl=int(self.padl.inch * 1000)
        
        row = self.ry.val
        col = self.rx.val
        xmargin = 2
        ymargin = 2
        if col ==0 : ymargin=0
        if row ==0 : xmargin=0
        xlayout=width - padl*xmargin - 10
        x0 = int((cv_xmax - xlayout)/2)
        x1 = x0 + xlayout
        ylayout = height - padl*ymargin - 10
        y0 = int((cv_ymax - ylayout)/2)
        y1 = y0 + ylayout
        #layout
        self.cv.create_rectangle(x0,y0,x1,y1,outline="yellow")

        # pin1 mark
        xoffset=int(xlayout * .1)
        yoffset=int(ylayout *.1)
        r = int(xlayout *.05)
        if r == 0 : r=2
        if r > 10 : r=10
        if row == 0:
            x0 = x0 + xoffset
            y0 = y1 - yoffset
        else:
            x0 = x0 + xoffset
            y0 = y0 + yoffset
        self.cv.create_oval(x0-r,y0-r,x0+r,y0+r,fill="white")
            
        # 垂直 pads
        
        x0=int((cv_xmax-width)/2)
        x1=x0+padl
        ex1=int((cv_xmax-width)/2)+width
        ex0=ex1-padl
        pitch=int(self.pitch.inch*1000)
        padw = int(self.padw.inch * 1000)
        padlyt=pitch * (row -1) + padw
        y0=int((cv_ymax-padlyt)/2)
        
        for i in range(row):
            y1=y0+padw
            self.cv.create_rectangle(x0,y0,x1,y1,fill="green")
            self.cv.create_rectangle(ex0,y0,ex1,y1,fill="green")
            y0=y0+pitch
        # 水平 pads
        
        y0=int((cv_ymax-height)/2)
        y1=y0+padl
        ey1=int((cv_ymax-height)/2)+height
        ey0=ey1-padl
        padlyt=pitch * (col -1) + padw
        x0=int((cv_xmax-padlyt)/2)
        for i in range(col):
            x1=x0+padw
            self.cv.create_rectangle(x0,y0,x1,y1,fill="green")
            self.cv.create_rectangle(x0,ey0,x1,ey1,fill="green")
            x0=x0+pitch
        
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
        self.padl = SizeEntry(.047,self)
        self.padl.grid(column=2,row=3)
        self.padl.trigger(self.draw)

        
        self.rx = IntEntry(8,self)
        self.rx.trigger(self.draw)
        
        self.rx.grid(column=0,row=4)
        x=tk.Label(self,text="X Length")
        x.grid(column=1,row=4)
        self.xlen = SizeEntry(.382,self)
        self.xlen.grid(column=2,row=4)
        self.xlen.trigger(self.draw)
        

        self.ry = IntEntry(8,self)
        self.ry.trigger(self.draw)
        self.ry.grid(column=0,row=5)
        
        x=tk.Label(self,text="Y Length")
        x.grid(column=1,row=5)
        self.ylen = SizeEntry(.382,self)
        self.ylen.grid(column=2,row=5)
        self.ylen.trigger(self.draw)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(column=0,row=6,columnspan=2)
        self.gen = tk.Button(self,text="Generate")
        self.gen.grid(column=2,row=6)
        self.cv = tk.Canvas(self,width=cv_xmax,height=cv_ymax)
        self.cv.grid(column=0,columnspan=3,row=7)
        
        self.draw()

if __name__=="__main__":
    root = tk.Tk()
    app = QFPWindow(master=root)
    app.master.title("QFP package generator")
    app.mainloop()
