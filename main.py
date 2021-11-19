# Tic tac toy game - Osama Alsikhan
from tkinter import messagebox



from tkinter import *

#create the main app game_ui

game_ui=Tk()


#Change title
game_ui.title("X / O game")

#set dimensions
game_ui.geometry("600x400")



dict1={'player1':'', 'player2':'', 'pressed':0}


def setX(): #Set player1 as X
    global dict1,turn,bot,player1,player2,botChoice
    if dict1['pressed']==0:
        dict1['player1']='X'
        dict1['player2']='O'
        turn = 1
        dict1['pressed']=1
        if bot==1:
            player1='X'
            botChoice='O'
            player2='O'
        elif bot==0:
            player1='X'
            player2='O'
        playersDisplay()
        btn_choose.destroy()
        btn_choose2.destroy()
        the_text2.destroy()



def setO(): #Set player1 as O
    global dict1,turn,player1,player2,botChoice
    if dict1['pressed']==0:
        dict1['player1']='O'
        dict1['player2']='X'
        dict1['pressed']=1
        turn = 1
        #turn=2
        if bot == 1:
            player1 = 'O'
            botChoice = 'X'
            player2='X' ###
        elif bot == 0:
            player1 = 'O'
            player2 = 'X'
        playersDisplay()
        btn_choose.destroy()
        btn_choose2.destroy()
        the_text2.destroy()









c = 0
def bot_player(x):
    global c,bot
    bot = 0
    if c==0:
        if x==1:
            bot=1
            btn_Bot.destroy()
            btn_Bot2.destroy()

        elif x==2:
            bot=0


    btn_Bot.destroy()
    btn_Bot2.destroy()
    the_text.destroy()

    c+=1


#create lable

the_text=Label(game_ui,text="Choose an opponent: ",height=2, font=("Arial",12))
the_text.grid()

#create buttons to choose player2 or Bot
btn_Bot=Button(game_ui,text="Bot" , width=6, height=1,bg="#e91e63",font="14", borderwidth=0,command=lambda: bot_player(1))
btn_Bot.grid()
btn_Bot2=Button(game_ui,text="Player2" , width=6, height=1,bg="#e91e63",font="14", borderwidth=0,command=lambda: bot_player(2))
btn_Bot2.grid()


#create lable

the_text2=Label(game_ui,text="Player1: Choose X or O",height=2, font=("Arial",14))
the_text2.grid()

#create buttons to choose X or O
btn_choose=Button(game_ui,text="X" , width=6, height=1,bg="#e91e63",font="14", borderwidth=0,command=setX)
btn_choose.grid()
btn_choose2=Button(game_ui,text="O" , width=6, height=1,bg="#e91e63",font="14", borderwidth=0,command=setO)
btn_choose2.grid()

def playersDisplay(): # display players choice X or O
    global dict1,player1,player2
    lbl = Label(game_ui, text="Tic-tac-toe Game", font=('Helvetica', '15'))
    lbl.grid()
    lbl = Label(game_ui, text="Player 1: "+dict1['player1'], font=('Helvetica', '10'))
    lbl.grid()
    lbl = Label(game_ui, text="Player 2: "+dict1['player2'], font=('Helvetica', '10'))
    lbl.grid()

#This function will do the role of computer player

def machinePlay():
    global botChoice,bot,turn
    from random import randrange

    while True:
         PickNum=randrange(9)

         if PickNum==0:
             if btn1["text"] == " ":
                 btn1["text"] = botChoice
                 turn=1
                 check()
                 break
         elif PickNum==1:
             if btn2["text"] == " ":
                 btn2["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==2:
             if btn3["text"] == " ":
                 btn3["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==3:
             if btn4["text"] == " ":
                 btn4["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==4:
             if btn5["text"] == " ":
                 btn5["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==5:
             if btn6["text"] == " ":
                 btn6["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==6:
             if btn7["text"] == " ":
                 btn7["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==7:
             if btn8["text"] == " ":
                 btn8["text"] = botChoice
                 turn = 1
                 check()
                 break
         elif PickNum==8:
             if btn9["text"] == " ":
                 btn9["text"] = botChoice
                 turn = 1
                 check()
                 break
         else:
            print("Bot choice error!")







def approve():
    global turn,player1,player2,bot,botChoice,dict1
    if turn == 1:
        turn = 2
        return dict1['player1']
    elif turn == 2:
        turn = 1
        if bot == 1:
            return botChoice
        else:
            return dict1['player2']



def play0():
    global turn,bot
    if btn1["text"] == " ":
        btn1["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play1():
    global turn,bot
    if btn2["text"] == " ":
        btn2["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play2():
    global turn,bot
    if btn3["text"] == " ":
        btn3["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play3():
    global turn,bot
    if btn4["text"] == " ":
        btn4["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play4():
    global turn,bot
    if btn5["text"] == " ":
        btn5["text"] = approve()
        check()
        if bot==1:
            machinePlay()


def play5():
    global turn,bot
    if btn6["text"] == " ":
        btn6["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play6():
    global turn,bot
    if btn7["text"] == " ":
        btn7["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play7():
    global turn,bot
    if btn8["text"] == " ":
        btn8["text"] = approve()
        check()
        if bot==1:
            machinePlay()



def play8():
    global turn,bot
    if btn9["text"] == " ":
        btn9["text"] = approve()
        check()
        if bot==1:
            machinePlay()









def check():
    global full
    place0 = btn1["text"]
    place1 = btn2["text"]
    place2 = btn3["text"]
    place3 = btn4["text"]
    place4 = btn5["text"]
    place5 = btn6["text"]
    place6 = btn7["text"]
    place7 = btn8["text"]
    place8 = btn9["text"]
    full += 1

    if place0 == place1 and place0 == place2 and place0 == "O" or place0 == place1 and place0 == place2 and place0 == "X":
        winMessage(place0)
    elif place3 == place4 and place3 == place5 and place3 == "O" or place3 == place4 and place3 == place5 and place3 == "X":
        winMessage(place3)
    elif place6 == place7 and place6 == place8 and place6 == "O" or place6 == place7 and place6 == place8 and place6 == "X":
        winMessage(place6)
    elif place0 == place3 and place0 == place6 and place0 == "O" or place0 == place3 and place0 == place6 and place0 == "X":
        winMessage(place0)
    elif place1 == place4 and place1 == place7 and place1 == "O" or place1 == place4 and place1 == place7 and place1 == "X":
        winMessage(place1)
    elif place2 == place5 and place2 == place8 and place2 == "O" or place2 == place5 and place2 == place8 and place2 == "X":
        winMessage(place2)
    elif place0 == place4 and place0 == place8 and place0 == "O" or place0 == place4 and place0 == place8 and place0 == "X":
        winMessage(place0)
    elif place6 == place4 and place6 == place2 and place6 == "O" or place6 == place4 and place6 == place2 and place6 == "X":
        winMessage(place6)
    elif full == 9:
        messagebox.showinfo("DRAW !", "DRAW")
        game_ui.destroy()
        exit()


def winMessage(y):
    x = str(y) +" win !"
    messagebox.showinfo("WIN !!", x)
    game_ui.destroy()
    exit()


btn1 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play0)
btn1.grid(column=1, row=1)
btn2 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play1)
btn2.grid(column=2, row=1)
btn3 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play2)
btn3.grid(column=3, row=1)
btn4 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play3)
btn4.grid(column=1, row=2)
btn5 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play4)
btn5.grid(column=2, row=2)
btn6 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play5)
btn6.grid(column=3, row=2)
btn7 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play6)
btn7.grid(column=1, row=3)
btn8 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play7)
btn8.grid(column=2, row=3)
btn9 = Button(game_ui, text=" ", bg="gray", fg="Black", width=3, height=1, font=('Arial', '20'), command= play8)
btn9.grid(column=3, row=3)



full=0
game_ui.mainloop()



