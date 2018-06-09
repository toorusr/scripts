from tkinter import *
from random import randint

def center(root):
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    size = size + (x, y)
    root.geometry("%dx%d+%d+%d" % size)


class CustomRoot:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x200")
        one_more_x = Button(self.root, text="x++").pack()
        one_more_y = Button(self.root, text="y++").pack()
        self.all_winxels = []

    def create_winxel(self, x, y, color):
        self.color = color
        winxel = Toplevel(self.root)
        winxel.group(self.root)
        winxel.overrideredirect(1)
        winxel.geometry("1x1+%i+%i" % (x, y))
        # center(winxel)
        winxel.configure(bg=self.color)
        winxel.protocol("WM_DELETE_WINDOW", lambda: self.destroy())
        winxel.bind("<Enter>", lambda e: winxel.configure(bg="red"))
        winxel.bind("<Leave>", lambda e: winxel.configure(bg=self.color))
        global state
        self.state = 1
        def bswitch(e):
            if self.state == 0:
                print("visible")
                winxel.attributes("-alpha", 1.0)
                self.state = 1
            elif self.state == 1:
                print("invincible")
                winxel.attributes("-alpha", 0.0)
                self.state = 0

        # winxel.bind("<Button-1>", bswitch)

        self.all_winxels.append(winxel)

    def onePixel(self):
        self.create_winxel(1920, 700, "blue")

    def curoWIndow(self):
        psco = "x1" # "x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1-x50-y1-xm50-y1"
        print(psco)
        self.shape(psco, (900, 500))

    def destroy(self):
        for i in self.all_winxels:
            i.geometry("20x20+%i+%i" % (randint(0, 1920), randint(0, 1080)))
        for i in self.all_winxels:
            i.config(bg="#%i" % randint(100000, 999999))
            # i.destroy()

    def shape(self, pseudocode, startpoint):
        # y100-x3-y345
        self.create_winxel(startpoint[0], startpoint[1], "white")
        self.lastpoint = (startpoint[0], startpoint[1])
        psco = pseudocode.split("-")
        for i in psco:
            if i[0] == "y":
                if i[1] == "m":
                    for i in range(int(i[2:])):
                        y = self.lastpoint[1] - 5
                        self.create_winxel(self.lastpoint[0], y, "white")
                        self.lastpoint = (self.lastpoint[0], y)
                else:
                    for i in range(int(i[1:])):
                        y = self.lastpoint[1] + 5
                        self.create_winxel(self.lastpoint[0], y, "white")
                        self.lastpoint = (self.lastpoint[0], y)
            elif i[0] == "x":  # diagonal
                if i[1] == "m":
                    for i in range(int(i[2:])):
                        x = self.lastpoint[0] - 5
                        self.create_winxel(x, self.lastpoint[1], "white")
                        self.lastpoint = (x, self.lastpoint[1])
                else:
                    for i in range(int(i[1:])):
                        x = self.lastpoint[0] + 5
                        self.create_winxel(x, self.lastpoint[1], "white")
                        self.lastpoint = (x, self.lastpoint[1])
            elif i[0] == "e" and i[1] == "x":
                if i[2] == "m":
                    print(i[3:])
                    for i in range(int(i[3:])):
                        x = self.lastpoint[0] - 5
                        self.lastpoint = (x, self.lastpoint[1])
                else:
                    for i in range(int(i[2:])):
                        x = self.lastpoint[0] + 5
                        self.lastpoint = (x, self.lastpoint[1])
            elif i[0] == "e" and i[1] == "y":
                if i[2] == "m":
                    for i in range(int(i[3:])):
                        y = self.lastpoint[1] - 5
                        self.lastpoint = (self.lastpoint[0], y)
                else:
                    for i in range(int(i[2:])):
                        y = self.lastpoint[1] + 5
                        self.lastpoint = (self.lastpoint[0], y)
            else:
                print("PsCo FormatWrong :" + i)





root = CustomRoot()
root.shape("y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50-y50-x1-ym50", (900, 500))
root.curoWIndow()
root.root.mainloop()
