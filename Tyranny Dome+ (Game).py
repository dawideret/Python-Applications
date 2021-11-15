import os
import time
import sys
import random
from random import randrange

GoblinPack1 = False
GoblinPack2 = False
GoblinPack3 = False

Woman1 = False
Woman2 = False

Husband1 = False
Husband2 = False

Wolves1 = False
Wolves2 = False
Wolves3 = False

Troll1 = False
Troll2 = False
Troll3 = False

Mage1 = False

Druid1 = False

StoneGuardian1 = False
StoneGuardian2 = False

Chimera1 = False

FredFlinston = False

Dragon = False

DarkOverlord = False

def WholeProgram():

    global PlayerHUNGER
    global PlayerHUNGER_current
    global PlayerHEALTH
    global PlayerHEALTH_current
    global PlayerSTRENGTH
    global PlayerSTRENGTH_current
    global PlayerFood
    global PlayerScore
    global PlayerMoney
    global SetDifficulty
    global typeSpeed
    global PlayerAge

    PlayerScore = 0
    
    typeSpeed = 2500

    def Type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(1/typeSpeed)
        print('')

    def cls():
        os.system("cls")

    def Nope():
        cls()
        print("<!> <!> <!> <!> <!> <!> <!> <!> <!> ")
        Type("Thats not an option... Try again friend!")
        print("<!> <!> <!> <!> <!> <!> <!> <!> <!> ")

    def Nope1():
        cls()
        print("")
        Type("Shopkeeper: Um. You can't do that sir.")
        print("")

    verifier = True

    while verifier == True:
        Type("Tavern Keep: Oh! A new face in our Tavern!")
        Type("Tavern Keep: Do not fret my friend, we're all good folks round here.")
        Type("Tavern Keep: What's your Name Traveller?")
        PlayerNAME = str(input(" >>> "))
        Type("Tavern Keep: So " + PlayerNAME + ", is how you're called! ")
        input_one = str(input("yes or no >>> "))
        if input_one == "yes":
            break
        else:
            cls()
            Type("Tavern Keep: Oh... Sorry, Let me start again then will ya?")
            continue
        
    while verifier == True:
        print("-------------------------------")
        Type("Choose your difficulty:")
        print("0. More Information")
        print("1. Child")
        print("2. Man")
        print("3. Hard")
        print("4. Masochism")
        print("-------------------------------")
                
        input_one = str(input(" >>> "))

        SetDifficulty = input_one

        if SetDifficulty != "0" and SetDifficulty != "1" and SetDifficulty != "2" and SetDifficulty != "3" and SetDifficulty != "4":
            Nope()
            continue
        
        if SetDifficulty == "0":
            cls()
            print("=====================")
            print("Child Difficulty")
            print("Starting Age: 18")
            print("Starting Hunger: 160")
            print("Starting Health: 100")
            print("Starting Strength: 10")
            print("=====================")
            print("Man Difficulty")
            print("Starting Age: 26")
            print("Starting Hunger: 100")
            print("Starting Health: 100")
            print("Starting Strength: 7.5")
            print("=====================")
            print("Hard Difficulty")
            print("Starting Age: 40")
            print("Starting Hunger: 60")
            print("Starting Health: 100")
            print("Starting Strength: 5.5")
            print("=====================")
            print("Masochism Difficulty")
            print("Starting Age: 60")
            print("Starting Hunger: 20")
            print("Starting Health: 50")
            print("Starting Strength: 1.0")
            print("=====================")
            continue
        
        if SetDifficulty == "1":
            cls()
            print("CHILD DIFFICULTY CHOSEN")
            Type("Tavern Keep: We're all panic-stricken so you will fit right in!")
            PlayerAGE = 18
            PlayerHEALTH = 160.0
            PlayerHUNGER = 100.0
            PlayerSTRENGTH = 10.0
            difficulty = "Child"
            break
                    
        if SetDifficulty == "2":
            cls()
            print("MAN DIFFICULTY CHOSEN")
            Type("Tavern Keep: Come and drink with us! You will need to gather strength.")
            PlayerAGE = 26
            PlayerHEALTH = 100.0
            PlayerHUNGER = 100.0
            PlayerSTRENGTH = 7.5
            difficulty = "Man"
            break
                   
        if SetDifficulty == "3":
            cls()
            print("HARD DIFFICULTY CHOSEN")
            Type("Tavern Keep: Are you sure you've ventured into the right territory? Good luck then!")
            Type("You will need it...")
            PlayerAGE = 40
            PlayerHEALTH = 100.0
            PlayerHUNGER = 60.0
            PlayerSTRENGTH = 5.5
            difficulty = "Hard"
            break
                    
        if SetDifficulty == "4":
            cls()
            print("MASOCHISM DIFFICULTY CHOSEN")
            Type("Tavern Keep: You've got the guts to show in an area like this one,")
            Type("how can you be sure I won't just stab you right here right now?")
            Type("I'm joking of course, but the next person you meet might not.")
            PlayerAGE = 60
            PlayerHEALTH = 50.0
            PlayerHUNGER = 20.0
            PlayerSTRENGTH = 1.0
            difficulty = "Masochism"
            break

    def Death():
        cls()
        print("=======================")
        print("=======================")
        print("=======================")
        print("=======================")
        print("YOU'VE DIED")
        print("=======================")
        print(" Your score >>> " + str(PlayerScore))
        print("=======================")
        print("=======================")
        print("Press Enter to continue...")
        input()
        cls()
        WholeProgram()

    PlayerHEALTH_current = PlayerHEALTH
    PlayerHUNGER_current = PlayerHUNGER
    PlayerSTRENGTH_current = PlayerSTRENGTH

    def StatUpdate():
        global PlayerHUNGER
        global PlayerHUNGER_current
        global PlayerHEALTH
        global PlayerHEALTH_current
        global PlayerSTRENGTH
        global PlayerSTRENGTH_current

        if PlayerHUNGER_current > PlayerHUNGER:
            PlayerHUNGER_current = PlayerHUNGER
        if PlayerHUNGER_current < 0:
            PlayerHUNGER_current = 0
        if PlayerHEALTH_current > PlayerHEALTH:
            PlayerHEALTH_current = PlayerHEALTH
        
        PlayerSTRENGTH_current = PlayerSTRENGTH
        if PlayerHUNGER_current > PlayerHUNGER:
            PlayerHUNGER_current = PlayerHUNGER
        if PlayerHEALTH_current <= PlayerHEALTH / 2:
            print(" Injuries weaken you.")
            PlayerSTRENGTH_current *= 0.5
        if PlayerHUNGER_current <= PlayerHUNGER / 2:
            print(" Hunger weakens you.")
            PlayerSTRENGTH_current *= 0.5
        if PlayerHEALTH_current <= 0:
            Death()

    PlayerFood = 0
    PlayerMoney = 0

    def move():
        global PlayerHUNGER
        global PlayerHUNGER_current
        global PlayerHEALTH
        global PlayerHEALTH_current
        global PlayerSTRENGTH
        global PlayerSTRENGTH_current
        global PlayerFood
        
        PlayerHUNGER_current -= 5

        if PlayerFood > 0 and PlayerHUNGER_current < PlayerHUNGER * 0.75:
            PlayerFood -= 1
            PlayerHUNGER_current += PlayerHUNGER * 0.25

        if PlayerHUNGER_current >= PlayerHUNGER * 0.75:
            PlayerHEALTH_current += PlayerHEALTH * 0.05
        StatUpdate()

    def PlayerProfile():
        global PlayerHUNGER
        global PlayerHUNGER_current
        global PlayerHEALTH
        global PlayerHEALTH_current
        global PlayerSTRENGTH
        global PlayerSTRENGTH_current
        global PlayerFood
        print("--------------------------------------------------")
        Type("  Adventurer Profile")
        print("--------------------------------------------------")
        StatUpdate()
        print(" Difficulty: " + str(difficulty))
        print(" Hero Name: " + str(PlayerNAME))
        print(" Current Age: " + str(PlayerAGE))
        print(" Current Health: " + str(PlayerHEALTH_current) + " / " + str(PlayerHEALTH))
        print(" Current Hunger: " + str(PlayerHUNGER_current)+ " / " + str(PlayerHUNGER))
        print(" Current Strenght: " + str(PlayerSTRENGTH_current) + " / " + str(PlayerSTRENGTH))
        print(" Food Rations Left: " + str(PlayerFood))
        print(" Money in your Wallet: " + str(PlayerMoney))
        print("--------------------------------------------------")
        print("Press Enter to continue...")
        input()
        cls()

    PlayerProfile()

    Type("Tavern Keep: What is the reason you travelled all the way out here?")
    input_one = str(input(" >>> "))
    Type("Tavern Keep: Oh... Well Anyways I think I might have a job for you.")
    Type("Tavern Keep: Just West from here some wolves have made a den.")
    Type("Tavern Keep: My Clients are constantly being harassed by those beasts.")
    Type("Tavern Keep: Could you do Something about that?")
    time.sleep(3)
    Type("Tavern Keep: I Knew I could count on you!")
    Type("Tavern Keep: Um. Here! Take two food rations for you quest.")
    PlayerFood += 2
    print("")
    print("You exit the tavern deeply confused and head West")
    print("")

    def EnemyTurn(EnemyAttackX, EnemyName):
        print("")
        print(str(EnemyName) + " attack(s) you dealing: " + str(EnemyAttackX) + " DMG")
        print("")
        global PlayerHEALTH_current
        PlayerHEALTH_current -= EnemyAttackX

    def Fight(EnemyName, EnemyNumber, EnemyHealth, EnemyAttack, EnemyIntelect, Location):
        cls()
        global PlayerHUNGER
        global PlayerHUNGER_current
        global PlayerHEALTH
        global PlayerHEALTH_current
        global PlayerSTRENGTH
        global PlayerSTRENGTH_current
        global PlayerScore
        global randrange
        global PlayerMoney
        Type("Fight with " + str(EnemyName) + " Begun!")
        ScoreGain = EnemyNumber * EnemyAttack
        print("This fight is worth from 10 to " + str((ScoreGain * 4) + 9) + " coins!")
        EnemyHealthX = EnemyNumber * EnemyHealth
        EnemyAttackX = EnemyNumber * EnemyAttack
        fightcontinues = False
        while True:
            StatUpdate()
            if EnemyNumber <= 0 or EnemyHealthX <= 0:
                print("You Win!")
                PlayerScore += ScoreGain
                PlayerMoney += randrange(1, (ScoreGain * 4) + 1) + 9
                EnemyCon = True
                return EnemyCon
            if fightcontinues == True:
                Type("Fight Continues!")
            fightcontinues = True
            print("Your Health: " + str(PlayerHEALTH_current))
            print("There are: " + str(EnemyNumber) + " enemies left.")
            print("1. Attack (deal damage)")
            print("2. Scream (might scare them)")
            print("3. Try to run (emergency exit)")
            input_one = str(input(" >>> "))
            choiceA = ["1", "2", "3"]
            if input_one in choiceA:
                if input_one == "1":
                    EnemyTurn(EnemyAttackX, EnemyName)
                    move()
                    print("")
                    print("You attack the enemy dealing: " + str(PlayerSTRENGTH_current) + " DMG")
                    print("")
                    EnemyHealthX -= PlayerSTRENGTH_current

                    casualties = PlayerSTRENGTH_current // EnemyHealth
                    if EnemyHealthX <= (EnemyNumber - 1) * EnemyHealth:
                        EnemyNumber -= casualties
                        EnemyAttackX -= casualties * EnemyAttack

                        if EnemyHealthX  <= (EnemyNumber - 1) * EnemyHealth:
                            EnemyNumber -= 1
                        if EnemyHealthX  <= (EnemyNumber - 1) * EnemyHealth:
                            EnemyNumber -= 1
                        continue
                if input_one == "2":
                    EnemyTurn(EnemyAttackX, EnemyName)
                    move()
                    chance = randrange(1, 101)
                    if chance > EnemyIntelect:
                        print("")
                        print("You scared an enemy off!")
                        print("")
                        SCARED = 1
                        EnemyNumber -= SCARED
                        EnemyHealthX -= SCARED * EnemyHealth
                        EnemyAttackX -= SCARED * EnemyAttack
                        continue
                    else:
                        print("")
                        print("You failed to scare anyone!")
                        print("")
                        continue
                if input_one == "3":
                    EnemyTurn(EnemyAttackX, EnemyName)
                    move()
                    change = randrange(1, 101)
                    if EnemyNumber * 3 > change:
                        print("")
                        print("You failed to escape!")
                        print("")
                        continue
                    else:
                        print("")
                        print("You managed to escape!")
                        print("")
                        LocateBack()
            else:
                cls()
                Nope()
                continue
    
    
    def Road1():
        cls()
        global Location
        global GoblinPack1
        Location = 1
        print("You're standing in the middle of a road,")
        print("surrounded by a thin forest and birds singing the national anthem.")
        print("1. To your left forest thickens and you can't see too deep.")
        print("2. In front of you there is a cozy hut with smoke coming out of the chimney.")
        if GoblinPack1 == False:
            print("3. On your right you can see a pack of small goblins staring at you.")
        else:
            print("3. On your right you can see a pack of dead goblins.")
        print("4. (look at your stats)")
        input_one = str(input(" >>> "))
        choiceA = ["1", "2", "3", "4"]
        if input_one in choiceA:
            if input_one == "1":
                move()
                Forest1()
            elif input_one == "2":
                move()
                Hut1()
            elif input_one == "3" and GoblinPack1 == False:
                move()
                GoblinPack1 = Fight("Goblins", 5, 5, 1, 10, Location)
            elif input_one == "3":
                print("")
                print("You don't want to approach dead goblins")
                print("")
                Road1()
            elif input_one == "4":
                PlayerProfile()
                Road1()
        else:
            cls()
            Nope()
            Road1()

    def Hut1():
        global Location
        Location = 2
        global Woman1
        global Husband1
        if Woman1 == False:
            print("")
            print("You enter the hut without knocking")
            print("")
            Type("Woman: Ah! Andrew there is a strange person in our house!")
            Type("Husband: I will be there in a second, just wait a moment")
            print("")
            print("1. Ransack the place")
            print("2. Go outside")
            input_one = str(input(" >>> "))
            if input_one == "1":
                Woman1 = Fight("Woman", 1, 35, 5, 50, Location)
            elif input_one == "2":
                Road1()
            else:
                cls()
                Nope()
                Hut1()
        elif Husband1 == False:
            print("")
            Type("Husband: Honey I'm here!")
            Type("Husband: What? Where is she! What did you do!")
            print("")
            print("1. Ransack the place")
            print("2. Go outside")
            input_one = str(input(" >>> "))
            if input_one == "1":
                Husband1 = Fight("Husband", 1, 45, 3, 85, Location)
            elif input_one == "2":
                Road1()
            else:
                cls()
                Nope()
                Hut1()
        else:
            print("")
            print("The House is empty, and smells of blood.")
            print("")
            Road1()
        Hut1()

    def Forest1():
        global Location
        Location = 3
        print("You're standing deep in the woods, and while squinting your")
        print("eyes, you're able to see that you're standing on a forked road.")
        print("1. Go Left")
        print("2. Go Right")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            Forest1A()
        elif input_one == "2":
            move()
            Forest1B()
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1A():
        global Location
        Location = 4
        print("You know you have definitely moved forward, but in front of you")
        print("there is another fork on the road.")
        print("1. Go Left")
        print("2. Go Right")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            Forest1A1()
        elif input_one == "2":
            move()
            Forest1A2()
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1B():
        global Location
        Location = 5
        print("You know you have definitely moved forward, but in front of you")
        print("there is another fork on the road.")
        print("1. Go Left")
        print("2. Go Right")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            Forest1B1()
        elif input_one == "2":
            move()
            Forest1B2()
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1A1():
        global Troll1
        global Location
        Location = 6
        print("You can see the end of the forest from here!")
        print("You feel happy to see it, but you see something.")
        print("1. Walk out of the forest")
        if Troll1 == False:
            print("2. Investigate the moving bush")
        else:
            print("2. The bush you fought behind is now gone")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            HiddenStore()
        elif input_one == "2" and Troll1 == False:
            Troll1 = Fight("Disgusting Troll", 1, 100, 25, 95, Location)
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        elif input_one == "2":
            print("")
            print("There is nothing more to fight over there.")
            print("")
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1A2():
        global Wolves1
        global Location
        Location = 7
        print("You can see the end of the forest from here!")
        print("You feel happy to see it, but you see something.")
        print("1. Walk out of the forest")
        if Wolves1 == False:
            print("2. Investigate the moving bush")
        else:
            print("2. The bush you fought behind is now gone")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            HiddenStore()
        elif input_one == "2" and Wolves1 == False:
            Wolves1 = Fight("Hungry Wolves", 3, 20, 8, 68, Location)
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        elif input_one == "2":
            print("")
            print("There is nothing more to fight over there.")
            print("")
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1B1():
        global Location
        global PlayerMoney
        Location = 8
        print("You can see the end of the forest from here!")
        print("You feel happy to see it, but you see something.")
        print("1. Walk out of the forest")
        print("2. Pickup the gold then leave the forest")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            HiddenStore()
        elif input_one == "2":
            PlayerMoney += 50
            move()
            HiddenStore()
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        else:
            cls()
            Nope()
            LocateBack()

    def Forest1B2():
        global GoblinPack2
        global Location
        Location = 9
        print("You can see the end of the forest from here!")
        print("You feel happy to see it, but you see something.")
        print("1. Walk out of the forest")
        if GoblinPack2 == False:
            print("2. Investigate the moving bush")
        else:
            print("2. The bush you fought behind is now gone")
        print("3. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "1":
            move()
            HiddenStore()
        elif input_one == "2" and GoblinPack2 == False:
            GoblinPack2 = Fight("Fat Goblins", 2, 25, 5, 50, Location)
        elif input_one == "3":
            PlayerProfile()
            LocateBack()
        elif input_one == "2":
            print("")
            print("There is nothing more to fight over there.")
            print("")
        else:
            cls()
            Nope()
            LocateBack()

    global AllTrialsDefeated
    AllTrialsDefeated = False

    global TrialNumber
    TrialNumber = 0

    def TrialChoice(TrialNumber):
        global GoblinPack3
        global Woman2
        global Husband2
        global Wolves2
        global Wolves3
        global Troll2
        global Troll3
        global Mage1
        global Druid1
        global StoneGuardian1
        global StoneGuardian2
        global Chimera1
        global Dragon
        global Location
        
        if TrialNumber == 0:
            GoblinPack3 = Fight("Dwarf Goblins", 10, 5, 1, 30, Location)
        if TrialNumber == 1:
            Woman2 = Fight("Females", 5, 10, 5, 40, Location)
        if TrialNumber == 2:
            Husband2 = Fight("Males", 4, 15, 6, 50, Location)
        if TrialNumber == 3:
            Wolves2 = Fight("Beta Wolves", 3, 20, 8, 60, Location)
        if TrialNumber == 4:
            Wolves3 = Fight("Alpha Wolves", 3, 25, 10, 70, Location)
        if TrialNumber == 5:
            Troll2 = Fight("Short Troll", 1, 80, 15, 85, Location)
        if TrialNumber == 6:
            Troll3= Fight("Fat Troll", 1, 120, 20, 90, Location)
        if TrialNumber == 7:
            Mage1 = Fight("Clever Mage", 1, 35, 30, 102, Location)
        if TrialNumber == 8:
            Druid1 = Fight("Obese Druid", 1, 95, 20, 102, Location)
        if TrialNumber == 9:
            StoneGuardian1 = Fight("Stone Guardian", 1, 100, 25, 102, Location)
        if TrialNumber == 10:
            StoneGuardian2 = Fight("Stone Guardians", 2, 100, 25, 102, Location)
        if TrialNumber == 11:
            Chimera1 = Fight("Chimera", 1, 200, 20, 102, Location)
        if TrialNumber == 12:
            Dragon = Fight("Black Dragon", 1, 250, 25, 102, Location)
        if TrialNumber == 13:
            Fight("Black Dragons", 2, 250, 20, 102, Location)
        if TrialNumber == 14:
            Fight("Fairy Dragon", 1, 350, 45, 102, Location)
        if TrialNumber == 15:
            Fight("Fairy Dragons", 2, 350, 30, 102, Location)
        if TrialNumber == 16:
            Fight("Fairy Dragons", 3, 350, 25, 102, Location)
        if TrialNumber == 17:
            Fight("Oblivion", 1, 500, 65, 102, Location)
        if TrialNumber == 18:
            Fight("Garfield", 1, 750, 65, 102, Location)
        if TrialNumber == 19:
            Fight("Squidward", 1, 1500, 45, 102, Location)
        if TrialNumber == 20:
            Fight("Awakened Black Dragon", 1, 1000, 100, 102, Location)
        if TrialNumber == 21:
            Fight("Awakened Fairy Dragon", 1, 1400, 140, 102, Location)
        if TrialNumber == 22:
            Fight("True Oblivion", 1, 1500, 200, 102, Location)
        if TrialNumber == 23:
            Fight("Black Dragon Army", 10, 250, 25, 102, Location)
        if TrialNumber == 24:
            Fight("Fairy Dragon Army", 10, 350, 45, 102, Location)
        if TrialNumber == 25:
            Fight("Crystal Dragon", 1, 10000, 500, 102, Location)
        if TrialNumber == 26:
            Fight("Death Himself", 1, 50000, 1000, 102, Location)

        
    
    def HiddenStore():
        global PlayerHUNGER
        global PlayerHUNGER_current
        global PlayerHEALTH
        global PlayerHEALTH_current
        global PlayerSTRENGTH
        global PlayerSTRENGTH_current
        global PlayerScore
        global randrange
        global PlayerMoney
        global Location
        global AllTrialsDefeated
        global PlayerFood
        global TrialNumber
        if TrialNumber >= 13:
            AllTrialsDefeated = True
        Location = 10
        cls()
        if TrialNumber == 26:
            print ("YOUR NEXT BATTLE WILL BE AGAINST DEATH HIMSELF")
        if TrialNumber == 27:
            print ("Shopkeeper: Did you just... Kill Death? Is dying even possible now?")
        if TrialNumber == 13:
            print ("Shopkeeper: MANDATORY trials are over! You can continue or leave!")
        print("Shopkeeper: Welcome to my magical store!")
        print("Don't ask me how you got here, nothing makes sense anymore.")
        print("(You look around and realize that somehow you've ended up in a store.)")
        if AllTrialsDefeated == False:
            print("Shopkeeper: I'm afraid you will be stuck here until you pass all my trials!")
            print("You should probably stock up on things before you start though...")
        else:
            print("0. Leave the store and continue!")
        print("1. Buy more Strenght (+1.5 per 20 coins)")
        print("2. Buy more Max Health (+20 per 20 coins)")
        print("3. Heal yourself to Max (5 coins)")
        print("4. Buy Food Rations (5 coins)")
        print("")
        print("999. Exchange all you money for Final Score, and die. (5 coins)")
        print("")
        print("5. Fight the next Trial (Most Trial Monsters never run away)")
        print("6. (look at your stats)")
        input_one = str(input(" >>> "))
        if input_one == "0" and AllTrialsDefeated == True:
            move()
            FinalScene()
        elif input_one == "1" and PlayerMoney >= 20:
            PlayerSTRENGTH += 1.5
            PlayerMoney -= 20
            StatUpdate()
            HiddenStore()
        elif input_one == "2" and PlayerMoney >= 20:
            PlayerHEALTH += 20
            PlayerMoney -= 20
            StatUpdate()
            HiddenStore()
        elif input_one == "3" and PlayerMoney >= 5:
            PlayerHEALTH_current = PlayerHEALTH
            PlayerMoney -= 5
            StatUpdate()
            HiddenStore()
        elif input_one == "4" and PlayerMoney >= 5:
            PlayerFood += 1
            PlayerMoney -= 5
            StatUpdate()
            HiddenStore()
        elif input_one == "999":
            PlayerScore += PlayerMoney
            Death()
        elif input_one == "5":
            TrialChoice(TrialNumber)
            TrialNumber += 1
            LocateBack()
        elif input_one == "6":
            PlayerProfile()
            LocateBack()
        else:
            cls()
            Nope1()
            LocateBack()

    def FinalScene():
        global DarkOverlord
        global FredFlinston
        if DarkOverlord == True:
            ending()
        global PlayerSTRENGTH
        global PlayerFood
        cls()
        if FredFlinston == False:
            print("You were just about to leave the store, but suddenly Fred Flinston attacks!")
            FredFlinston = Fight("Fred Flinston", 1, 350, 30, 102, Location)
            FinalScene()
        print("After passing all the trials you've returned victorious to the Tavernkeep, and")
        print("Received an award for killing the wolves. (25 Food Rations and + 10 Damage)")
        PlayerSTRENGTH += 10
        PlayerFood += 25
        input("Press Enter to continue >>> ")
        cls()
        print("While talking with the town folk you heard them talk about an evil wizard")
        print("Or how others call him... Dark Overlord")
        print("Apparently he's a real douche. So... You decided to go and stop him.")
        input("Press Enter to continue >>> ")
        cls()
        DarkOverlord = Fight("Dark Overlord", 1, 600, 35, 102, Location)
        if DarkOverlord == True:
            ending()

    def ending():
        global PlayerScore
        global PlayerMoney
        global typeSpeed
        cls()
        Type("You finally defeated all evil, and decided to rest...")
        PlayerScore += PlayerMoney
        typeSpeed = 200
        Type("Your Final Score: " + str(PlayerScore))
        time.sleep(999999)

    def LocateBack():
        global Location
        if Location == 1:
            Road1()
        if Location == 2:
            Hut1()
        if Location == 3:
            Forest1()
        if Location == 4:
            Forest1A()
        if Location == 5:
            Forest1B()
        if Location == 6:
            Forest1A1()
        if Location == 7:
            Forest1A2()
        if Location == 8:
            Forest1B1()
        if Location == 9:
            Forest1B2()
        if Location == 10:
            HiddenStore()
        if Location == 11:
            FinalScene()

    input("Press Enter to Continue >>> ")
    Road1()
 
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()
    LocateBack()


WholeProgram()
