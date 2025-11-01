from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import os

P1=askstring('Preferences',"Name for player 1:",initialvalue='Player 1')
C1=askstring('Preferences',"Colour for player 1:",initialvalue='black').lower()
P2=askstring('Preferences',"Name for player 2:",initialvalue='Player 2')
C2=askstring('Preferences',"Colour for player 2:",initialvalue='black').lower()
root1=Tk()
root1.title(P1+" Vs "+P2)
root1.iconbitmap(r'Icons\tic-tac-toe_39453.ico')

w1=0
w2=0
T="O"
Count=0

#Defining the function to change text on buttonns
def Change(b):
    global T,w1,w2
    global Count
    if b["text"]==" ":
        b["text"]=T
        if Count%2==0:
            T="X"
        else:
            T="O"
        Count+=1
    w=Conditions("O",P1)
    l=Conditions("X",P2)
    W1=w.win()
    if W1!=True:
        if l.win()==True:
            w2+=1
            L=str(w2)
            Wins2["text"]=L
        elif Count==9:
            messagebox.showerror("Tic Tac Toe","Game Draw")
    elif W1==True:
        w1+=1
        W=str(w1)
        Wins1["text"]=W

#defining buttons   
B1=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B1))
B2=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B2))
B3=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B3))
B4=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B4))
B5=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B5))
B6=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B6))
B7=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B7))
B8=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B8))
B9=Button(root1,text=" ",font=("calibri",10),bg="white",padx=30,pady=30,command=lambda:Change(B9))

#Checking All Conditions statements
class Conditions:
    def __init__(self,Move,Player):
        self.Move=Move
        self.Player=Player

    def win(self):
        if B1["text"]==B2["text"]==B3["text"]==self.Move:
            B1.config(bg="blue")
            B2.config(bg="blue")
            B3.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B4["text"]==B5["text"]==B6["text"]==self.Move:
            B4.config(bg="blue")
            B5.config(bg="blue")
            B6.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B7["text"]==B8["text"]==B9["text"]==self.Move:
            B7.config(bg="blue")
            B8.config(bg="blue")
            B9.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B1["text"]==B5["text"]==B9["text"]==self.Move:
            B1.config(bg="blue")
            B5.config(bg="blue")
            B9.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B3["text"]==B5["text"]==B7["text"]==self.Move:
            B3.config(bg="blue")
            B5.config(bg="blue")
            B7.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B1["text"]==B4["text"]==B7["text"]==self.Move:
            B1.config(bg="blue")
            B4.config(bg="blue")
            B7.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B2["text"]==B5["text"]==B8["text"]==self.Move:
            B2.config(bg="blue")
            B5.config(bg="blue")
            B8.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        elif B3["text"]==B6["text"]==B9["text"]==self.Move:
            B3.config(bg="blue")
            B6.config(bg="blue")
            B9.config(bg="blue")
            textw=self.Player+" Won"
            messagebox.showinfo("Tic Tac Toe",textw)
            return True
        else:
            return False

#Placing widgets    
B1.grid(row=1,column=0)
B2.grid(row=1,column=1)
B3.grid(row=1,column=2)
B4.grid(row=2,column=0)
B5.grid(row=2,column=1)
B6.grid(row=2,column=2)
B7.grid(row=3,column=0)
B8.grid(row=3,column=1)
B9.grid(row=3,column=2)

#Placing Widgets for showing Wins and Losses
Win1=Label(root1,text=P1,fg=C1)
Win1.grid(row=0,column=3)
Wins1=Label(root1,text="0")
Wins1.grid(row=1,column=3)
Win2=Label(root1,text=P2,fg=C2)
Win2.grid(row=0,column=4)
Wins2=Label(root1,text="0")
Wins2.grid(row=1,column=4)

def exit():
    sroot1.destroy()

def retry():
    global Count,T
    B1["text"]=B2["text"]=B3["text"]=B4["text"]=B5["text"]=B6["text"]=B7["text"]=B8["text"]=B9["text"]=" "
    B1.config(bg="White")
    B2.config(bg="White")
    B3.config(bg="White")
    B4.config(bg="White")
    B5.config(bg="White")
    B6.config(bg="White")
    B7.config(bg="White")
    B8.config(bg="White")
    B9.config(bg="White")
    Count=0
    T="O"

#Creating and placing buttons for back and retry
B0=Button(root1,padx=3,pady=1,text="Back",command=exit)
B0.grid(row=0,column=1)
B10=Button(root1,text="Retry",padx=3,pady=1,command=retry)
B10.grid(row=0,column=0)

root1.mainloop()
