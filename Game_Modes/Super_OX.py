from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
w1=0
w2=0
T="O"
Count=0

P1=askstring('Custom Input',"Name for player 1:")
C1=askstring('Preferences',"Colour for player 1:").lower()
P2=askstring('Custom Input',"Name for player 2:")
C2=askstring('Preferences',"Colour for player 2:").lower()

class Conditions:
    def __init__(self,Move):
        self.Move=Move
        
    def Win(self):
        global w1,w2
        if a["text"]==b["text"]==c["text"]==self.Move:
            a.config(bg="blue")
            b.config(bg="blue")
            c.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
            
        elif a["text"]==d["text"]==g["text"]==self.Move:
            a.config(bg="blue")
            d.config(bg="blue")
            g.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
                
        elif a["text"]==e["text"]==i["text"]==self.Move:
            a.config(bg="blue")
            e.config(bg="blue")
            i.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
            

        elif d["text"]==e["text"]==f["text"]==self.Move:
            d.config(bg="blue")
            e.config(bg="blue")
            f.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
                
        elif g["text"]==h["text"]==i["text"]==self.Move:
            g.config(bg="blue")
            h.config(bg="blue")
            i.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
        
        elif c["text"]==e["text"]==g["text"]==self.Move:
            c.config(bg="blue")
            e.config(bg="blue")
            g.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
                
        elif b["text"]==e["text"]==h["text"]==self.Move:
            b.config(bg="blue")
            e.config(bg="blue")
            h.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")
                
        elif c["text"]==f["text"]==i["text"]==self.Move:
            c.config(bg="blue")
            f.config(bg="blue")
            i.config(bg="blue")
            if self.Move=="O":
                w1+=1
                win0=str(w1)
                W1["text"]=win0
                W1.config(state="active")
                messagebox.showinfo("Super OX",P1+" Won")
            elif self.Move=="X":
                w2+=1
                win=str(w2)
                W2["text"]=win
                W2.config(state="active")
                messagebox.showinfo("Super OX",P2+" won")

        else:
            pass

            
    def win1(self):
        global a
        if a["text"]=="":
            if a1["text"]==a2["text"]==a3["text"]==self.Move:
                a1.config(bg="blue")
                a2.config(bg="blue")
                a3.config(bg="blue")
                a["text"]=self.Move
                return True
            elif b1["text"]==b2["text"]==b3["text"]==self.Move:
                b1.config(bg="blue")
                b2.config(bg="blue")
                b3.config(bg="blue")
                a["text"]=self.Move
                return True
            elif c1["text"]==c2["text"]==c3["text"]==self.Move:
                c1.config(bg="blue")
                c2.config(bg="blue")
                c3.config(bg="blue")
                a["text"]=self.Move
                return True
            elif a1["text"]==b2["text"]==c3["text"]==self.Move:
                a1.config(bg="blue")
                b2.config(bg="blue")
                c3.config(bg="blue")
                a["text"]=self.Move
                return True
            elif a3["text"]==b2["text"]==c1["text"]==self.Move:
                a3.config(bg="blue")
                b2.config(bg="blue")
                c1.config(bg="blue")
                a["text"]=self.Move
                return True
            elif a1["text"]==b1["text"]==c1["text"]==self.Move:
                a1.config(bg="blue")
                b1.config(bg="blue")
                c1.config(bg="blue")
                a["text"]=self.Move
                return True
            elif a2["text"]==b2["text"]==c2["text"]==self.Move:
                a2.config(bg="blue")
                b2.config(bg="blue")
                c2.config(bg="blue")
                a["text"]=self.Move
                return True
            elif a3["text"]==b3["text"]==c3["text"]==self.Move:
                a3.config(bg="blue")
                b3.config(bg="blue")
                c3.config(bg="blue")
                a["text"]=self.Move
                return True
            else:
                return False

    def win2(self):
        global b
        if b["text"]=="":
            if a4["text"]==a5["text"]==a6["text"]==self.Move:
                a4.config(bg="blue")
                a5.config(bg="blue")
                a6.config(bg="blue")
                b["text"]=self.Move
                return True
            elif b4["text"]==b5["text"]==b6["text"]==self.Move:
                b4.config(bg="blue")
                b5.config(bg="blue")
                b6.config(bg="blue")
                b["text"]=self.Move
                return True
            elif c4["text"]==c5["text"]==c6["text"]==self.Move:
                c4.config(bg="blue")
                c5.config(bg="blue")
                c6.config(bg="blue")
                b["text"]=self.Move
                return True
            elif a4["text"]==b5["text"]==c6["text"]==self.Move:
                a4.config(bg="blue")
                b5.config(bg="blue")
                c6.config(bg="blue")
                b["text"]=self.Move
                return True
            elif a6["text"]==b5["text"]==c4["text"]==self.Move:
                a6.config(bg="blue")
                b5.config(bg="blue")
                c4.config(bg="blue")
                b["text"]=self.Move
                return True
            elif a4["text"]==b4["text"]==c4["text"]==self.Move:
                a4.config(bg="blue")
                b4.config(bg="blue")
                c4.config(bg="blue")
                b["text"]=self.Move
                return True
            elif a5["text"]==b5["text"]==c5["text"]==self.Move:
                a5.config(bg="blue")
                b5.config(bg="blue")
                c5.config(bg="blue")
                b["text"]=self.Move
                return True
            elif a6["text"]==b6["text"]==c6["text"]==self.Move:
                a6.config(bg="blue")
                b6.config(bg="blue")
                c6.config(bg="blue")
                b["text"]=self.Move
                return True
            else:
                return False

    def win3(self):
        global c
        if c["text"]=="":
            if a7["text"]==a8["text"]==a9["text"]==self.Move:
                a7.config(bg="blue")
                a8.config(bg="blue")
                a9.config(bg="blue")
                c["text"]=self.Move
                return True
            elif b7["text"]==b8["text"]==b9["text"]==self.Move:
                b7.config(bg="blue")
                b8.config(bg="blue")
                b9.config(bg="blue")
                c["text"]=self.Move
                return True
            elif c7["text"]==c8["text"]==c9["text"]==self.Move:
                c7.config(bg="blue")
                c8.config(bg="blue")
                c9.config(bg="blue")
                c["text"]=self.Move
                return True
            elif a7["text"]==b8["text"]==c9["text"]==self.Move:
                a7.config(bg="blue")
                b8.config(bg="blue")
                c9.config(bg="blue")
                c["text"]=self.Move
                return True
            elif a9["text"]==b8["text"]==c7["text"]==self.Move:
                a9.config(bg="blue")
                b8.config(bg="blue")
                c7.config(bg="blue")
                c["text"]=self.Move
                return True
            elif a7["text"]==b7["text"]==c7["text"]==self.Move:
                a7.config(bg="blue")
                b7.config(bg="blue")
                c7.config(bg="blue")
                c["text"]=self.Move
                return True
            elif a8["text"]==b8["text"]==c8["text"]==self.Move:
                a8.config(bg="blue")
                b8.config(bg="blue")
                c8.config(bg="blue")
                c["text"]=self.Move
                return True
            elif a9["text"]==b9["text"]==c9["text"]==self.Move:
                a9.config(bg="blue")
                b9.config(bg="blue")
                c9.config(bg="blue")
                c["text"]=self.Move
                return True
            else:
                return False

    def win4(self):
        global d
        if d["text"]=="":
            if d1["text"]==d2["text"]==d3["text"]==self.Move:
                d1.config(bg="blue")
                d2.config(bg="blue")
                d3.config(bg="blue")
                d["text"]=self.Move
                return True
            elif e1["text"]==e2["text"]==e3["text"]==self.Move:
                e1.config(bg="blue")
                e2.config(bg="blue")
                e3.config(bg="blue")
                d["text"]=self.Move
                return True
            elif f1["text"]==f2["text"]==f3["text"]==self.Move:
                f1.config(bg="blue")
                f2.config(bg="blue")
                f3.config(bg="blue")
                d["text"]=self.Move
                return True
            elif d1["text"]==e2["text"]==f3["text"]==self.Move:
                d1.config(bg="blue")
                e2.config(bg="blue")
                f3.config(bg="blue")
                d["text"]=self.Move
                return True
            elif d3["text"]==e2["text"]==f1["text"]==self.Move:
                d3.config(bg="blue")
                e2.config(bg="blue")
                f1.config(bg="blue")
                d["text"]=self.Move
                return True
            elif d1["text"]==e1["text"]==f1["text"]==self.Move:
                d1.config(bg="blue")
                e1.config(bg="blue")
                f1.config(bg="blue")
                d["text"]=self.Move
                return True
            elif d2["text"]==e2["text"]==f2["text"]==self.Move:
                d2.config(bg="blue")
                e2.config(bg="blue")
                f2.config(bg="blue")
                d["text"]=self.Move
                return True
            elif d3["text"]==e3["text"]==f3["text"]==self.Move:
                d3.config(bg="blue")
                e3.config(bg="blue")
                f3.config(bg="blue")
                d["text"]=self.Move
                return True
            else:
                return False

    def win5(self):
        global e
        if e["text"]=="":
            if d4["text"]==d5["text"]==d6["text"]==self.Move:
                d4.config(bg="blue")
                d5.config(bg="blue")
                d6.config(bg="blue")
                e["text"]=self.Move
                return True
            elif e4["text"]==e5["text"]==e6["text"]==self.Move:
                e4.config(bg="blue")
                e5.config(bg="blue")
                e6.config(bg="blue")
                e["text"]=self.Move
                return True
            elif f4["text"]==f5["text"]==f6["text"]==self.Move:
                f4.config(bg="blue")
                f5.config(bg="blue")
                f6.config(bg="blue")
                e["text"]=self.Move
                return True
            elif d4["text"]==e5["text"]==f6["text"]==self.Move:
                d4.config(bg="blue")
                e5.config(bg="blue")
                f6.config(bg="blue")
                e["text"]=self.Move
                return True
            elif d6["text"]==e5["text"]==f4["text"]==self.Move:
                d6.config(bg="blue")
                e5.config(bg="blue")
                f4.config(bg="blue")
                e["text"]=self.Move
                return True
            elif d4["text"]==e4["text"]==f4["text"]==self.Move:
                d4.config(bg="blue")
                e4.config(bg="blue")
                f4.config(bg="blue")
                e["text"]=self.Move
                return True
            elif d5["text"]==e5["text"]==f5["text"]==self.Move:
                d5.config(bg="blue")
                e5.config(bg="blue")
                f5.config(bg="blue")
                e["text"]=self.Move
                return True
            elif d6["text"]==e6["text"]==f6["text"]==self.Move:
                d6.config(bg="blue")
                e6.config(bg="blue")
                f6.config(bg="blue")
                e["text"]=self.Move
                return True
            else:
                return False

    def win6(self):
        global f
        if f["text"]=="":
            if d7["text"]==d8["text"]==d9["text"]==self.Move:
                d7.config(bg="blue")
                d8.config(bg="blue")
                d9.config(bg="blue")
                f["text"]=self.Move
                return True
            elif e7["text"]==e8["text"]==e9["text"]==self.Move:
                e7.config(bg="blue")
                e8.config(bg="blue")
                e9.config(bg="blue")
                f["text"]=self.Move
                return True
            elif f7["text"]==f8["text"]==f9["text"]==self.Move:
                f7.config(bg="blue")
                f8.config(bg="blue")
                f9.config(bg="blue")
                f["text"]=self.Move
                return True
            elif d7["text"]==e8["text"]==f9["text"]==self.Move:
                d7.config(bg="blue")
                e8.config(bg="blue")
                f9.config(bg="blue")
                f["text"]=self.Move
                return True
            elif d9["text"]==e8["text"]==f7["text"]==self.Move:
                d9.config(bg="blue")
                e8.config(bg="blue")
                f7.config(bg="blue")
                f["text"]=self.Move
                return True
            elif d7["text"]==e7["text"]==f7["text"]==self.Move:
                d7.config(bg="blue")
                e7.config(bg="blue")
                f7.config(bg="blue")
                f["text"]=self.Move
                return True
            elif d8["text"]==e8["text"]==f8["text"]==self.Move:
                d8.config(bg="blue")
                e8.config(bg="blue")
                f8.config(bg="blue")
                f["text"]=self.Move
                return True
            elif d9["text"]==e9["text"]==f9["text"]==self.Move:
                d9.config(bg="blue")
                e9.config(bg="blue")
                f9.config(bg="blue")
                f["text"]=self.Move
                return True
            else:
                return False

    def win7(self):
        global g
        if g["text"]=="":
            if g1["text"]==g2["text"]==g3["text"]==self.Move:
                g1.config(bg="blue")
                g2.config(bg="blue")
                g3.config(bg="blue")
                g["text"]=self.Move
                return True
            elif h1["text"]==h2["text"]==h3["text"]==self.Move:
                h1.config(bg="blue")
                h2.config(bg="blue")
                h3.config(bg="blue")
                g["text"]=self.Move
                return True
            elif i1["text"]==i2["text"]==i3["text"]==self.Move:
                i1.config(bg="blue")
                i2.config(bg="blue")
                i3.config(bg="blue")
                g["text"]=self.Move
                return True
            elif g1["text"]==h2["text"]==i3["text"]==self.Move:
                g1.config(bg="blue")
                h2.config(bg="blue")
                i3.config(bg="blue")
                g["text"]=self.Move
                return True
            elif g3["text"]==h2["text"]==i1["text"]==self.Move:
                g3.config(bg="blue")
                h2.config(bg="blue")
                i1.config(bg="blue")
                g["text"]=self.Move
                return True
            elif g1["text"]==h1["text"]==i1["text"]==self.Move:
                g1.config(bg="blue")
                h1.config(bg="blue")
                i1.config(bg="blue")
                g["text"]=self.Move
                return True
            elif g2["text"]==h2["text"]==i2["text"]==self.Move:
                g2.config(bg="blue")
                h2.config(bg="blue")
                i2.config(bg="blue")
                g["text"]=self.Move
                return True
            elif g3["text"]==h3["text"]==i3["text"]==self.Move:
                g3.config(bg="blue")
                h3.config(bg="blue")
                i3.config(bg="blue")
                g["text"]=self.Move
                return True
            else:
                return False

    def win8(self):
        global h
        if h["text"]=="":
            if g4["text"]==g5["text"]==g6["text"]==self.Move:
                g4.config(bg="blue")
                g5.config(bg="blue")
                g6.config(bg="blue")
                h["text"]=self.Move
                return True
            elif h4["text"]==h5["text"]==h6["text"]==self.Move:
                h4.config(bg="blue")
                h5.config(bg="blue")
                h6.config(bg="blue")
                h["text"]=self.Move
                return True
            elif i4["text"]==i5["text"]==i6["text"]==self.Move:
                i4.config(bg="blue")
                i5.config(bg="blue")
                i6.config(bg="blue")
                h["text"]=self.Move
                return True
            elif g4["text"]==h5["text"]==i6["text"]==self.Move:
                g4.config(bg="blue")
                h5.config(bg="blue")
                i6.config(bg="blue")
                h["text"]=self.Move
                return True
            elif g6["text"]==h5["text"]==i4["text"]==self.Move:
                g6.config(bg="blue")
                h5.config(bg="blue")
                i4.config(bg="blue")
                h["text"]=self.Move
                return True
            elif g4["text"]==h4["text"]==i4["text"]==self.Move:
                g4.config(bg="blue")
                h4.config(bg="blue")
                i4.config(bg="blue")
                h["text"]=self.Move
                return True
            elif g5["text"]==h5["text"]==i5["text"]==self.Move:
                g5.config(bg="blue")
                h5.config(bg="blue")
                i5.config(bg="blue")
                h["text"]=self.Move
                return True
            elif g6["text"]==h6["text"]==i6["text"]==self.Move:
                g6.config(bg="blue")
                h6.config(bg="blue")
                i6.config(bg="blue")
                h["text"]=self.Move
                return True
            else:
                return False

    def win9(self):
        global i
        if i["text"]=="":
            if g7["text"]==g8["text"]==g9["text"]==self.Move:
                g7.config(bg="blue")
                g8.config(bg="blue")
                g9.config(bg="blue")
                i["text"]=self.Move
                return True
            elif h7["text"]==h8["text"]==h9["text"]==self.Move:
                h7.config(bg="blue")
                h8.config(bg="blue")
                h9.config(bg="blue")
                i["text"]=self.Move
                return True
            elif i7["text"]==i8["text"]==i9["text"]==self.Move:
                i7.config(bg="blue")
                i8.config(bg="blue")
                i9.config(bg="blue")
                i["text"]=self.Move
                return True
            elif g7["text"]==h8["text"]==i9["text"]==self.Move:
                g7.config(bg="blue")
                h8.config(bg="blue")
                i9.config(bg="blue")
                i["text"]=self.Move
                return True
            elif g9["text"]==h8["text"]==i7["text"]==self.Move:
                g9.config(bg="blue")
                h8.config(bg="blue")
                i7.config(bg="blue")
                i["text"]=self.Move
                return True
            elif g7["text"]==h7["text"]==i7["text"]==self.Move:
                g7.config(bg="blue")
                h7.config(bg="blue")
                i7.config(bg="blue")
                i["text"]=self.Move
                return True
            elif g8["text"]==h8["text"]==i8["text"]==self.Move:
                g8.config(bg="blue")
                h8.config(bg="blue")
                i8.config(bg="blue")
                i["text"]=self.Move
                return True
            elif g9["text"]==h9["text"]==i9["text"]==self.Move:
                g9.config(bg="blue")
                h9.config(bg="blue")
                i9.config(bg="blue")
                i["text"]=self.Move
                return True
            else:
                return False
            
def exit():
    root1.destroy()

#Defining the function to change text on buttonns
def Change(b):
    global T,w1,w2
    global Count
    if b["text"]==" ":
        b["text"]=T
        Rings=Conditions("O")
        Cross=Conditions("X")
        z1,y1,x1,w1,v1,u1,t1,s1,r1=Rings.win1(),Rings.win2(),Rings.win3(),Rings.win4(),Rings.win5(),Rings.win6(),Rings.win7(),Rings.win8(),Rings.win9()
        z2,y2,x2,w2,v2,u2,t2,s2,r2=Cross.win1(),Cross.win2(),Cross.win3(),Cross.win4(),Cross.win5(),Cross.win6(),Cross.win7(),Cross.win8(),Cross.win9()
        if (z1==True or z2==True):
            a1.config(state="disabled")
            a2.config(state="disabled")
            a3.config(state="disabled")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            c1.config(state="disabled")
            c2.config(state="disabled")
            c3.config(state="disabled")
        elif (y1==True or y2==True):
            a4.config(state="disabled")
            a5.config(state="disabled")
            a6.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            c4.config(state="disabled")
            c5.config(state="disabled")
            c6.config(state="disabled")
        elif (x1==True or x2==True):
            a7.config(state="disabled")
            a8.config(state="disabled")
            a9.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
            c7.config(state="disabled")
            c8.config(state="disabled")
            c9.config(state="disabled")
        elif (w1==True or w2==True):
            d1.config(state="disabled")
            d2.config(state="disabled")
            d3.config(state="disabled")
            e1.config(state="disabled")
            e2.config(state="disabled")
            e3.config(state="disabled")
            f1.config(state="disabled")
            f2.config(state="disabled")
            f3.config(state="disabled")
        elif (v1==True or v2==True):
            d4.config(state="disabled")
            d5.config(state="disabled")
            d6.config(state="disabled")
            e4.config(state="disabled")
            e5.config(state="disabled")
            e6.config(state="disabled")
            f4.config(state="disabled")
            f5.config(state="disabled")
            f6.config(state="disabled")
        elif (u1==True or u2==True):
            d7.config(state="disabled")
            d8.config(state="disabled")
            d9.config(state="disabled")
            e7.config(state="disabled")
            e8.config(state="disabled")
            e9.config(state="disabled")
            f7.config(state="disabled")
            f8.config(state="disabled")
            f9.config(state="disabled")
        elif (t1==True or t2==True):
            g1.config(state="disabled")
            g2.config(state="disabled")
            g3.config(state="disabled")
            h1.config(state="disabled")
            h2.config(state="disabled")
            h3.config(state="disabled")
            i1.config(state="disabled")
            i2.config(state="disabled")
            i3.config(state="disabled")
        elif (s1==True or s2==True):
            g4.config(state="disabled")
            g5.config(state="disabled")
            g6.config(state="disabled")
            h4.config(state="disabled")
            h5.config(state="disabled")
            h6.config(state="disabled")
            i4.config(state="disabled")
            i5.config(state="disabled")
            i6.config(state="disabled")
        elif (r1==True or r2==True):
            g7.config(state="disabled")
            g8.config(state="disabled")
            g9.config(state="disabled")
            h7.config(state="disabled")
            h8.config(state="disabled")
            h9.config(state="disabled")
            i7.config(state="disabled")
            i8.config(state="disabled")
            i9.config(state="disabled")
        else:
            pass

    
    Rings.Win()
    Cross.Win()
        
    if Count%2==0:
        T="X"
    else:
        T="O"
    Count+=1
        
def retry():
    global Count,T,a,b,c,d,e,f,g,h,i
    a1["text"]=" "
    a2["text"]=" "
    a3["text"]=" "
    a4["text"]=" "
    a5["text"]=" "
    a6["text"]=" "
    a7["text"]=" "
    a8["text"]=" "
    a9["text"]=" "
    b1["text"]=" "
    b2["text"]=" "
    b3["text"]=" "
    b4["text"]=" "
    b5["text"]=" "
    b6["text"]=" "
    b7["text"]=" "
    b8["text"]=" "
    b9["text"]=" "
    c1["text"]=" "
    c2["text"]=" "
    c3["text"]=" "
    c4["text"]=" "
    c5["text"]=" "
    c6["text"]=" "
    c7["text"]=" "
    c8["text"]=" "
    c9["text"]=" "
    d1["text"]=" "
    d2["text"]=" "
    d3["text"]=" "
    d4["text"]=" "
    d5["text"]=" "
    d6["text"]=" "
    d7["text"]=" "
    d8["text"]=" "
    d9["text"]=" "
    e1["text"]=" "
    e2["text"]=" "
    e3["text"]=" "
    e4["text"]=" "
    e5["text"]=" "
    e6["text"]=" "
    e7["text"]=" "
    e8["text"]=" "
    e9["text"]=" "
    f1["text"]=" "
    f2["text"]=" "
    f3["text"]=" "
    f4["text"]=" "
    f5["text"]=" "
    f6["text"]=" "
    f7["text"]=" "
    f8["text"]=" "
    f9["text"]=" "
    g1["text"]=" "
    g2["text"]=" "
    g3["text"]=" "
    g4["text"]=" "
    g5["text"]=" "
    g6["text"]=" "
    g7["text"]=" "
    g8["text"]=" "
    g9["text"]=" "
    h1["text"]=" "
    h2["text"]=" "
    h3["text"]=" "
    h4["text"]=" "
    h5["text"]=" "
    h6["text"]=" "
    h7["text"]=" "
    h8["text"]=" "
    h9["text"]=" "
    i1["text"]=" "
    i2["text"]=" "
    i3["text"]=" "
    i4["text"]=" "
    i5["text"]=" "
    i6["text"]=" "
    i7["text"]=" "
    i8["text"]=" "
    i9["text"]=" "

    a1.config(bg="white")
    a2.config(bg="white")
    a3.config(bg="white")
    a4.config(bg="white")
    a5.config(bg="white")
    a6.config(bg="white")
    a7.config(bg="white")
    a8.config(bg="white")
    a9.config(bg="white")
    b1.config(bg="white")
    b2.config(bg="white")
    b3.config(bg="white")
    b4.config(bg="white")
    b5.config(bg="white")
    b6.config(bg="white")
    b7.config(bg="white")
    b8.config(bg="white")
    b9.config(bg="white")
    c1.config(bg="white")
    c2.config(bg="white")
    c3.config(bg="white")
    c4.config(bg="white")
    c5.config(bg="white")
    c6.config(bg="white")
    c7.config(bg="white")
    c8.config(bg="white")
    c9.config(bg="white")
    d1.config(bg="white")
    d2.config(bg="white")
    d3.config(bg="white")
    d4.config(bg="white")
    d5.config(bg="white")
    d6.config(bg="white")
    d7.config(bg="white")
    d8.config(bg="white")
    d9.config(bg="white")
    e1.config(bg="white")
    e2.config(bg="white")
    e3.config(bg="white")
    e4.config(bg="white")
    e5.config(bg="white")
    e6.config(bg="white")
    e7.config(bg="white")
    e8.config(bg="white")
    e9.config(bg="white")
    f1.config(bg="white")
    f2.config(bg="white")
    f3.config(bg="white")
    f4.config(bg="white")
    f5.config(bg="white")
    f6.config(bg="white")
    f7.config(bg="white")
    f8.config(bg="white")
    f9.config(bg="white")
    g1.config(bg="white")
    g2.config(bg="white")
    g3.config(bg="white")
    g4.config(bg="white")
    g5.config(bg="white")
    g6.config(bg="white")
    g7.config(bg="white")
    g8.config(bg="white")
    g9.config(bg="white")
    h1.config(bg="white")
    h2.config(bg="white")
    h3.config(bg="white")
    h4.config(bg="white")
    h5.config(bg="white")
    h6.config(bg="white")
    h7.config(bg="white")
    h8.config(bg="white")
    h9.config(bg="white")
    i1.config(bg="white")
    i2.config(bg="white")
    i3.config(bg="white")
    i4.config(bg="white")
    i5.config(bg="white")
    i6.config(bg="white")
    i7.config(bg="white")
    i8.config(bg="white")
    i9.config(bg="white")

    Count=0
    T="O"
    
    a1.config(state="normal")
    a2.config(state="normal")
    a3.config(state="normal")
    a4.config(state="normal")
    a5.config(state="normal")
    a6.config(state="normal")
    a7.config(state="normal")
    a8.config(state="normal")
    a9.config(state="normal")
    b1.config(state="normal")
    b2.config(state="normal")
    b3.config(state="normal")
    b4.config(state="normal")
    b5.config(state="normal")
    b6.config(state="normal")
    b7.config(state="normal")
    b8.config(state="normal")
    b9.config(state="normal")
    c1.config(state="normal")
    c2.config(state="normal")
    c3.config(state="normal")
    c4.config(state="normal")
    c5.config(state="normal")
    c6.config(state="normal")
    c7.config(state="normal")
    c8.config(state="normal")
    c9.config(state="normal")
    d1.config(state="normal")
    d2.config(state="normal")
    d3.config(state="normal")
    d4.config(state="normal")
    d5.config(state="normal")
    d6.config(state="normal")
    d7.config(state="normal")
    d8.config(state="normal")
    d9.config(state="normal")
    e1.config(state="normal")
    e2.config(state="normal")
    e3.config(state="normal")
    e4.config(state="normal")
    e5.config(state="normal")
    e6.config(state="normal")
    e7.config(state="normal")
    e8.config(state="normal")
    e9.config(state="normal")
    f1.config(state="normal")
    f2.config(state="normal")
    f3.config(state="normal")
    f4.config(state="normal")
    f5.config(state="normal")
    f6.config(state="normal")
    f7.config(state="normal")
    f8.config(state="normal")
    f9.config(state="normal")
    g1.config(state="normal")
    g2.config(state="normal")
    g3.config(state="normal")
    g4.config(state="normal")
    g5.config(state="normal")
    g6.config(state="normal")
    g7.config(state="normal")
    g8.config(state="normal")
    g9.config(state="normal")
    h1.config(state="normal")
    h2.config(state="normal")
    h3.config(state="normal")
    h4.config(state="normal")
    h5.config(state="normal")
    h6.config(state="normal")
    h7.config(state="normal")
    h8.config(state="normal")
    h9.config(state="normal")
    i1.config(state="normal")
    i2.config(state="normal")
    i3.config(state="normal")
    i4.config(state="normal")
    i5.config(state="normal")
    i6.config(state="normal")
    i7.config(state="normal")
    i8.config(state="normal")
    i9.config(state="normal")

    a.config(bg="white")
    b.config(bg="white")
    c.config(bg="white")
    d.config(bg="white")
    e.config(bg="white")
    f.config(bg="white")
    g.config(bg="white")
    h.config(bg="white")
    i.config(bg="white")

    a["text"]=""
    b["text"]=""
    c["text"]=""
    d["text"]=""
    e["text"]=""
    f["text"]=""
    g["text"]=""
    h["text"]=""
    i["text"]=""

    W1.config(state="normal")
    W2.config(state="normal")

        
root1=Tk()

root1.title("Super O-X")
root1.iconbitmap(r'Icons\tic-tac-toe_39453.ico')
root1.minsize(height=500,width=755)

Exit = Button(root1,command=exit,text="Back",height=1,width=6)
Exit.grid(row=0,column=1)
Retry=Button(root1,command=retry,text="Retry",height=1,width=6)
Retry.grid(row=0, column=5)


a1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a1))
a2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a2))
a3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a3))
a4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a4))
a5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a5))
a6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a6))
a7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a7))
a8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a8))
a9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(a9))

b1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b1))
b2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b2))
b3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b3))
b4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b4))
b5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b5))
b6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b6))
b7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b7))
b8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b8))
b9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(b9))

c1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c1))
c2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c2))
c3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c3))
c4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c4))
c5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c5))
c6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c6))
c7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c7))
c8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c8))
c9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(c9))

d1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d1))
d2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d2))
d3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d3))
d4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d4))
d5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d5))
d6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d6))
d7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d7))
d8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d8))
d9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(d9))

e1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e1))
e2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e2))
e3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e3))
e4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e4))
e5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e5))
e6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e6))
e7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e7))
e8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e8))
e9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(e9))

f1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f1))
f2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f2))
f3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f3))
f4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f4))
f5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f5))
f6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f6))
f7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f7))
f8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f8))
f9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(f9))

g1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g1))
g2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g2))
g3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g3))
g4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g4))
g5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g5))
g6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g6))
g7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g7))
g8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g8))
g9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(g9))

h1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h1))
h2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h2))
h3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h3))
h4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h4))
h5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h5))
h6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h6))
h7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h7))
h8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h8))
h9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(h9))

i1=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i1))
i2=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i2))
i3=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i3))
i4=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i4))
i5=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i5))
i6=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i6))
i7=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i7))
i8=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i8))
i9=Button(root1,padx=20,pady=10,bg="white",fg="blue",text=" ",font=("Bahaus 93",10),command=lambda:Change(i9))


a=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
b=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
c=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
d=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
e=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
f=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
g=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
h=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")
i=Button(root1,padx=20,pady=10,bg="white",fg="green",text="",state="disabled")

Usel1=Label(root1,width=5,text=" ")
Usel2=Label(root1,width=5,text="==>")
Usel3=Label(root1,width=5,text=" ")

Usel1.grid(row=9,column=12)
Usel2.grid(row=10,column=12)
Usel3.grid(row=11,column=12)

a.grid(row=9,column=13)
b.grid(row=9,column=14)
c.grid(row=9,column=15)
d.grid(row=10,column=13)
e.grid(row=10,column=14)
f.grid(row=10,column=15)
g.grid(row=11,column=13)
h.grid(row=11,column=14)
i.grid(row=11,column=15)


a1.grid(row=1,column=1)
a2.grid(row=1,column=2)
a3.grid(row=1,column=3)
a4.grid(row=1,column=5)
a5.grid(row=1,column=6)
a6.grid(row=1,column=7)
a7.grid(row=1,column=9)
a8.grid(row=1,column=10)
a9.grid(row=1,column=11)

b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
b4.grid(row=2,column=5)
b5.grid(row=2,column=6)
b6.grid(row=2,column=7)
b7.grid(row=2,column=9)
b8.grid(row=2,column=10)
b9.grid(row=2,column=11)

c1.grid(row=3,column=1)
c2.grid(row=3,column=2)
c3.grid(row=3,column=3)
c4.grid(row=3,column=5)
c5.grid(row=3,column=6)
c6.grid(row=3,column=7)
c7.grid(row=3,column=9)
c8.grid(row=3,column=10)
c9.grid(row=3,column=11)

d1.grid(row=5,column=1)
d2.grid(row=5,column=2)
d3.grid(row=5,column=3)
d4.grid(row=5,column=5)
d5.grid(row=5,column=6)
d6.grid(row=5,column=7)
d7.grid(row=5,column=9)
d8.grid(row=5,column=10)
d9.grid(row=5,column=11)

e1.grid(row=6,column=1)
e2.grid(row=6,column=2)
e3.grid(row=6,column=3)
e4.grid(row=6,column=5)
e5.grid(row=6,column=6)
e6.grid(row=6,column=7)
e7.grid(row=6,column=9)
e8.grid(row=6,column=10)
e9.grid(row=6,column=11)

f1.grid(row=7,column=1)
f2.grid(row=7,column=2)
f3.grid(row=7,column=3)
f4.grid(row=7,column=5)
f5.grid(row=7,column=6)
f6.grid(row=7,column=7)
f7.grid(row=7,column=9)
f8.grid(row=7,column=10)
f9.grid(row=7,column=11)

g1.grid(row=9,column=1)
g2.grid(row=9,column=2)
g3.grid(row=9,column=3)
g4.grid(row=9,column=5)
g5.grid(row=9,column=6)
g6.grid(row=9,column=7)
g7.grid(row=9,column=9)
g8.grid(row=9,column=10)
g9.grid(row=9,column=11)

h1.grid(row=10,column=1)
h2.grid(row=10,column=2)
h3.grid(row=10,column=3)
h4.grid(row=10,column=5)
h5.grid(row=10,column=6)
h6.grid(row=10,column=7)
h7.grid(row=10,column=9)
h8.grid(row=10,column=10)
h9.grid(row=10,column=11)

i1.grid(row=11,column=1)
i2.grid(row=11,column=2)
i3.grid(row=11,column=3)
i4.grid(row=11,column=5)
i5.grid(row=11,column=6)
i6.grid(row=11,column=7)
i7.grid(row=11,column=9)
i8.grid(row=11,column=10)
i9.grid(row=11,column=11)


L1=Label(root1,text=" ",height=1,width=1)
L2=Label(root1,text=" ",height=1,width=1)
L3=Label(root1,text=" ",height=1,width=1)
L4=Label(root1,text=" ",height=1,width=1)
L5=Label(root1,text=" ",height=1,width=1)
L6=Label(root1,text=" ",height=1,width=1)
L7=Label(root1,text=" ",height=1,width=1)
L8=Label(root1,text=" ",height=1,width=1)
L9=Label(root1,text=" ",height=1,width=1)
L10=Label(root1,text=" ",height=1,width=1)
L11=Label(root1,text=" ",height=1,width=1)
L12=Label(root1,text=" ",height=1,width=1)

L13=Label(root1,text=" ",height=1,width=1)


L1.grid(row=2,column=4)
L2.grid(row=2,column=8)
L3.grid(row=4,column=2)
L4.grid(row=4,column=6)
L5.grid(row=4,column=10)
L6.grid(row=6,column=4)
L7.grid(row=6,column=8)
L8.grid(row=8,column=2)
L9.grid(row=8,column=6)
L10.grid(row=8,column=10)
L11.grid(row=10,column=4)
L12.grid(row=10,column=8)
L13.grid(row=0,column=0)

O=Button(root1,bg=C1,text=P1,bd=2,height=2,width=5)
X=Button(root1,bg=C2,fg="white",bd=2,text=P2,height=2,width=5,activebackground="black",activeforeground="white")
W1=Button(root1,text=w1,bg="white",bd=2,height=2,width=5,activebackground=C1)
W2=Button(root1,text=w2,bg="white",bd=2,height=2,width=5,activebackground=C2)

O.grid(row=1,column=13)
X.grid(row=1,column=14)
W1.grid(row=2,column=13)
W2.grid(row=2,column=14)

Res=Label(root1,text="| RESULT |")
Res.grid(row=8,column=14)

root1.mainloop()
