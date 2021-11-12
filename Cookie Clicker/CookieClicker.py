from tkinter import *
import tkinter as tk
import random
import threading
import time

cookieAmount = 0
cookiePrice = 1
positionCounter = 100
friendPay = 0



def foreground():
    
    game = Tk()

    #=====================================================

    def cookieUpdate():
        text2.configure(text = f'{cookieAmount}')

    def background():
        global cookieAmount
        global friendPay
        while True:
            cookieAmount += friendPay
            cookieUpdate()
            time.sleep(1)

    def cookiePress():
        global cookieAmount
        global cookiePrice
        global positionCounter
        cookieAmount += cookiePrice
        cookieUpdate()
        positionCounter -= 1
        if positionCounter <= 0:
            positionCounter = 100
            cookieButton.place(x = random.randint(399, 700), y = random.randint(99, 400))

    def staleUpgrade():
        global cookieAmount
        global cookiePrice
        if cookieAmount >= 10:
            cookieAmount -= 10
            cookiePrice += 1
            cookieUpdate()
            
    def tastyUpgrade():
        global cookieAmount
        global cookiePrice
        if cookieAmount >= 10000:
            cookieAmount -= 10000
            cookiePrice += 150
            cookieUpdate()
            
    def goldenUpgrade():
        global cookieAmount
        global cookiePrice
        if cookieAmount >= 250000:
            cookieAmount -= 250000
            cookiePrice += 2000
            cookieUpdate()
            
    def platinumUpgrade():
        global cookieAmount
        global cookiePrice
        if cookieAmount >= 100000000:
            cookieAmount -= 100000000
            cookiePrice += 250000
            cookieUpdate()

    def uFriend1():
        global cookieAmount
        global friendPay

        if cookieAmount >= 100:
            cookieAmount -= 100
            friendPay += 1
            cookieUpdate()

    def uFriend2():
        global cookieAmount
        global friendPay

        if cookieAmount >= 100000:
            cookieAmount -= 100000
            friendPay += 1000
            cookieUpdate()

    def uFriend3():
        global cookieAmount
        global friendPay

        if cookieAmount >= 2500000:
            cookieAmount -= 2500000
            friendPay += 50000
            cookieUpdate()

    def uFriend4():
        global cookieAmount
        global friendPay

        if cookieAmount >= 1000000000:
            cookieAmount -= 1000000000
            friendPay += 1000000
            cookieUpdate()

    #=====================================================

    cookie = PhotoImage(file = "cookie.png")
    tastycookie = PhotoImage(file = "tastycookie.png")
    goldencookie = PhotoImage(file = "goldencookie.png")
    platinumcookie = PhotoImage(file = "platinumcookie.png")
    stalecookie = PhotoImage(file = "stalecookie.png")

    friend1 = PhotoImage(file = "friend1.png")
    friend2 = PhotoImage(file = "friend2.png")
    friend3 = PhotoImage(file = "friend3.png")
    friend4 = PhotoImage(file = "friend4.png")

    cookieButton = Button(game, image = cookie, height = 60, width = 60, command = cookiePress)


    uButton1 = Button(game, text = "£10", font = ("Verdana", 26), image = stalecookie, height = 100, width = 240, command = staleUpgrade, compound = "left")
    uButton2 = Button(game, text = "£10K", font = ("Verdana", 26), image = tastycookie, height = 100, width = 240, command = tastyUpgrade, compound = "left")
    uButton3 = Button(game, text = "£250K", font = ("Verdana", 26), image = goldencookie, height = 100, width = 240, command = goldenUpgrade, compound = "left")
    uButton4 = Button(game, text = "£100M", font = ("Verdana", 26), image = platinumcookie, height = 100, width = 240, command = platinumUpgrade, compound = "left")

    f1Button = Button(game, text = "£100", font = ("Verdana", 26), image = friend1, height = 100, width = 260, command = uFriend1, compound = "right")
    f2Button = Button(game, text = "£100K", font = ("Verdana", 26), image = friend2, height = 100, width = 260, command = uFriend2, compound = "right")
    f3Button = Button(game, text = "£2.5M", font = ("Verdana", 26), image = friend3, height = 100, width = 260, command = uFriend3, compound = "right")
    f4Button = Button(game, text = "£1B", font = ("Verdana", 26), image = friend4, height = 100, width = 260, command = uFriend4, compound = "right")

    text1 = Label(game, text = "Cookies", font = ("Verdana", 26), fg = "blue")
    text2 = Label(game, text = "0", font = ("Verdana", 26), fg = "orange")
    text3 = Label(game, text = "Upgrades", font = ("Verdana", 26), fg = "blue")
    text4 = Label(game, text = "Friends", font = ("Verdana", 26), fg = "blue")
     
    cookieButton.place(x = 550, y = 250)
    uButton1.place(x = 15, y = 135)
    uButton2.place(x = 15, y = 245)
    uButton3.place(x = 15, y = 355)
    uButton4.place(x = 15, y = 465)
    text1.place(x = 15, y = 5)
    text2.place(x = 15, y = 45)
    text3.place(x = 15, y = 85)
    text4.place(x = 925, y = 85)

    f1Button.place(x = 925, y = 135)
    f2Button.place(x = 925, y = 245)
    f3Button.place(x = 925, y = 355)
    f4Button.place(x = 925, y = 465)

    #=====================================================
    b = threading.Thread(name = 'background', target = background)
    b.start()
    game.title("Cookie Clicker")
    game.geometry("1200x600")
    game.mainloop()


f = threading.Thread(name = 'foreground', target = foreground)

f.start()

