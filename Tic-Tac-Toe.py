from tkinter import *
from tkinter import messagebox


Root=Tk()
Root.title("Tic Tac Toe")
Root.iconbitmap(r'Icons\tic-tac-toe_39453.ico')
Root.minsize(height=250,width=500)



def Open1():
    from Game_Modes import Player_Vs_Player
    
def Open2():
    from Game_Modes import Player_Vs_Computer

def Open3():
    from Game_Modes import Super_OX
        
def Exit():
    ans=messagebox.askquestion("Exit?","Do you really want to quit?")
    if ans=="yes":
        Root.destroy()

L1=Label(Root,text="Tic Tac Toe",font=("Bauhaus 93",60))
B1=Button(Root,text="Player V/s Computer",font=("Arial",10),command=Open2)
B2=Button(Root,text="Player V/s Player",font=("Arial",10),command=Open1)
B3=Button(Root,text="Super O-X",font=("Arial",10),command=Open3,bg="magenta",fg="blue")
L2=Label(Root,text="(for now only pvp in Super OX is available)",font=("Arial",8))
Exit=Button(Root,text="Exit",font=("Arial",10),command=Exit)

L1.pack(side=TOP)
B1.pack()
B2.pack()
B3.pack()
L2.pack()
Exit.pack(side=BOTTOM)

Root.mainloop()
