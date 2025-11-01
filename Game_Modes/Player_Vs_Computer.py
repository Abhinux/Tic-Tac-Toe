from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import time

P1=askstring('Custom Input',"Name for player 1:")
C1=askstring('Preferences',"Colour for player 1:").lower()

root1=Tk()
root1.title(P1+" Vs Computer")

Count=0
Ws=0
Ls=0


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


P2="Computer"

#Defining the function to change text on buttonns
def Change(b):
    global T,Ls,Ws,P1,P2
    global Count
    if b["text"]==" ":
        b["text"]="O"
        Count+=1
        w=Conditions("O",P1)
        l=Conditions("X",P2)
        W1=w.win()
        if W1!=True and Count==5:
            messagebox.showerror("Tic Tac Toe","Game Draw")
        elif W1==True:
            Ws+=1
            W=str(Ws)
            Wins["text"]=W
        elif W1!=True:
            Comp_turn1()
            if l.win()==True:
                Ls+=1
                L=str(Ls)
                Losses["text"]=L
        
#Defining Computer's Moves
def Comp_turn1():
    #first turn check
    if B5["text"]==" ":
        B5["text"]="X"
    #Offensive check
    elif (B2["text"]==B3["text"]=="X" or B7["text"]==B4['text']=="X" or B9["text"]==B5["text"]=="X") and B1["text"]==" ":
        B1["text"]="X"
    elif (B1["text"]==B3["text"]=="X" or B5["text"]==B8['text']=="X") and B2["text"]==" ":
        B2["text"]="X"
    elif (B1["text"]==B2["text"]=="X" or B9["text"]==B6['text']=="X" or B7["text"]==B5["text"]=="X") and B3["text"]==" ":
        B3["text"]="X"
    elif (B1["text"]==B7["text"]=="X" or B6["text"]==B5['text']=="X") and B4["text"]==" ":
        B4["text"]="X"
    elif (B3["text"]==B9["text"]=="X" or B4["text"]==B5['text']=="X") and B6["text"]==" ":
        B6["text"]="X"
    elif (B1["text"]==B4["text"]=="X" or B9["text"]==B8['text']=="X" or B3["text"]==B5["text"]=="X") and B7["text"]==" ":
        B7["text"]="X"
    elif (B7["text"]==B9["text"]=="X" or B2["text"]==B5['text']=="X") and B8["text"]==" ":
        B8["text"]="X"
    elif (B1["text"]==B5["text"]=="X" or B3["text"]==B6['text']=="X" or B7["text"]==B8["text"]=="X") and B9["text"]==" ":
        B9["text"]="X"
    #Defensive check
    elif (B2["text"]==B3["text"]=="O" or B7["text"]==B4['text']=="O" or B9["text"]==B5["text"]=="O") and B1["text"]==" ":
        B1["text"]="X"
    elif (B1["text"]==B3["text"]=="O" or B5["text"]==B8['text']=="O") and B2["text"]==" ":
        B2["text"]="X"
    elif (B1["text"]==B2["text"]=="O" or B9["text"]==B6['text']=="O" or B7["text"]==B5["text"]=="O") and B3["text"]==" ":
        B3["text"]="X"
    elif (B1["text"]==B7["text"]=="O" or B6["text"]==B5['text']=="O") and B4["text"]==" ":
        B4["text"]="X"
    elif (B3["text"]==B9["text"]=="O" or B4["text"]==B5['text']=="O") and B6["text"]==" ":
        B6["text"]="X"
    elif (B1["text"]==B4["text"]=="O" or B9["text"]==B8['text']=="O" or B3["text"]==B5["text"]=="O") and B7["text"]==" ":
        B7["text"]="X"
    elif (B7["text"]==B9["text"]=="O" or B2["text"]==B5['text']=="O") and B8["text"]==" ":
        B8["text"]="X"
    elif (B1["text"]==B5["text"]=="O" or B3["text"]==B6['text']=="O" or B7["text"]==B8["text"]=="O") and B9["text"]==" ":
        B9["text"]="X" 
    else:
        if B5["text"]=="X":
            if B7["text"]==" ":
                B7["text"]="X"
            elif B1["text"]==" ":
                B1["text"]="X"
            elif B9["text"]==" ":
                B9["text"]="X"
            elif B3["text"]==" ":
                B3["text"]="X"
            elif B8["text"]==" ":
                B8["text"]="X"
        else:
            if B4["text"]==" ":
                B4["text"]="X"
            elif B6["text"]==" ":
                B6["text"]="X"
            elif B2["text"]==" ":
                B2["text"]="X"
            elif B7["text"]==" ":
                B7["text"]="X"
            elif B1["text"]==" ":
                B1["text"]="X"
            elif B9["text"]==" ":
                B9["text"]="X"
            elif B3["text"]==" ":
                B3["text"]="X"
            elif B8["text"]==" ":
                B8["text"]="X"
                
        
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



#Placing Widgets for showing Wins and Losses
Win=Label(root1,text="Wins",fg=C1)
Win.grid(row=0,column=3)
Wins=Label(root1,text="0")
Wins.grid(row=1,column=3)
Loss=Label(root1,text="Losses",fg="red")
Loss.grid(row=0,column=4)
Losses=Label(root1,text="0")
Losses.grid(row=1,column=4)


def exit():
    root1.destroy()
    
def retry():
    global Count
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
    
#Creating and placing buttons for back and retry    
B0=Button(root1,padx=3,pady=1,text="Back",command=exit)
B0.grid(row=0,column=1)
B10=Button(root1,text="Retry",padx=3,pady=1,command=retry)
B10.grid(row=0,column=0)

root1.mainloop()
