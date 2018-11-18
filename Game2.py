'''
    Napoleonic War Simulator

    You can either play as the French or the British

    The "rooms" are a number of battlefields. The goal will to be to win each battle
    and make it to the enemies capital - London or Paris.

    In order to win the battle you need more soldiers, the ratio of soldiers between the two
    armies will decide how many soldiers you lose in a battle.

    To get more soldiers you will need to pillage towns. When you pillage there's a chance
    you will be ambushed. 

'''
import random
import sys
def startGame():
    header("Napoleonic War Simulator")
    introduction()
    faction = chooseFaction()
    print(faction[0])
    establish(faction)
    mySoldiers = 10000
    
    location = faction[1]
    print(location)
    running(location,mySoldiers)
    

def header(string):
    print("="*25 + " " + string + 25 * "=")
    
    




def introduction():
    print('''
Welcome to Napoleonic War Simulator! \n
You may pick the French or the British. Fight each battle and make
it to the capital of the enemy\n
You need more soldiers than the enemy to win. Get more soldiers by pillaging towns.
When you pillage a town there is a chance of being ambushed.




''')

def chooseFaction():
    try:
        global choice
        global faction
        choice = int(input(''' Choose a faction:
Enter 1 or 2\n
1. France
2. England
    '''))
    
    except ValueError:
        print("Not a choice. Choose again")
        chooseFaction()
    if choice == 1:
        faction = "France"
        location = "Paris"
        print(faction)
        return(faction,location)
    elif choice == 2:
        faction = "England"
        location = "London"
        print(faction)
        return(faction,location)
    else:
        print("Not a choice. Choose again")
        chooseFaction()



def establish(faction):
    if faction[0] == "France":
        header("Napoleonic War Simulator")
        print('''
Welcome, Napoleon!\n
    We are in Paris. The English are ready to attack! What should we do?
    ''')
    else:
        header("Napoleonic War Simulator")
        print('''
Welcome, Lord Nelson!\n
    We are in London. The French are ready to attack! What should we do?
    ''')



def youLose():
    header("Napoleonic War Simulator")
    print("\n You Lose!")
    sys.exit("Try Again! Don't lose all of your soldiers.")
    
def youWin():
    header("Napoleonic War Simulator")
    print("\n You Win!")
    sys.exit()
    
def showMap():
    print('''
            London
              |
              |
              |
      | --------------|
      |               |
    Brighton        Hastings ------ Calais
      |                               |
      |                               |
      |                               |
   Le Havre                          Amiens
      |                               |
      |                               |
      |                               |
    Chartres                        Versailles
      |                               |
      |                               |
      |------------ Paris -------------
      ''')



battlesWon = {"London":False,
                          "Hastings":False,
                          "Calais":False,
                          "Amiens":False,
                          "Versailles":False,
                          "Paris":False,
                          "Brighton":False,
                          "Le Havre":False,
                          "Chartres":False
                          }




def battle(location,mySoldiers,theySoldiers):
    if battlesWon[location] == True:
        print("We have already taken this city")
      
        return(0)
    elif mySoldiers >= theySoldiers and battlesWon[location] == False:
        
        casualties = 3 * int(theySoldiers*.25)
        battlesWon[location] = True
        print("Battle Won! You lost " + str(casualties) + " soldiers\n" +"We have taken " + location + "\n\n")
        
        
        if faction == "France" and location == "London" or faction == "England" and location == "Paris":
            if battlesWon[location] == True:
                youWin()
                sys.exit
  
        return(casualties)





def running(location,mySoldiers): # The game loop
    i = 0
    dictionary = {"Paris" : 54,             # A dictionary representing the number of soldiers at each location
                  "Chartres" : 70,
                  "Versailles" : 72,
                  "Le Havre" : 67,
                  "Amiens" : 53,
                  "Brighton" : 40,
                  "Calais" : 77,
                  "Hastings" : 67,
                  "London" : 54}
    while i != "Quit":
        i = input('''
Enter "Map" to show map\n                   
Enter "Attack" to attack\n
Enter "Pillage" to Gather troops\n
Enter "Move" to move your troops\n
Enter "Quit" to End

Soldiers = ''' + str(mySoldiers) + " Location = " + location + "\n")

        header("Napoleonic War Simulator ")
        
        if i == "Attack":
            try:
                mySoldiers = mySoldiers - battle(location,mySoldiers,dictionary[location])
                if battlesWon[location] == True:
                    print("We have already taken this city")
                
                   
            except ValueError:
                print("You lost the battle. Come back with more soldiers")
                mySoldiers = 0
            
        elif i == "Map":
            showMap()

        elif i == "Pillage":
            if dictionary[location] == 54:
                print("You can't pillage your own city!")
            elif random.randint(1,7) == 2 or random.randint(1,7) == 7:
                print("You have been ambushed while pillaging!")
                mySoldiers = mySoldiers - 15
                if mySoldiers < 0:
                    youLose()
            else:
                mySoldiers = mySoldiers + random.randint(7,19)
        
        

        elif i == "Move":
            
            destination = input("Where would you like to move?\n")
            if destination == "Map":
                showMap()
                destination = input("Where would you like to move?\n")
            fluidMapDictionary1 = {1 : "London",
                                  2 : "Hastings",
                                  3 : "Calais",
                                  4 : "Amiens",
                                  5 : "Versailles",
                                  6 : "Paris"
                                   }
            fluidMapDictionary2 = {1 : "London",
                                   2 : "Brighton",
                                   3 : "Le Havre",
                                   4 : "Chartres",
                                   5 : "Paris"
                                   }
            originalLocation = location
            if battlesWon[location] == False and battlesWon[destination] == False:
                print("You need to attack before moving on!")
                destination = "flop"
            try:
                for i , v in fluidMapDictionary1.items():
                    if v == location:
                        index = i
                        for i , v in fluidMapDictionary1.items():
                            if v == destination:
                                destinationIndex = i
                                if index - destinationIndex == 1 or index - destinationIndex == -1:
                                    location = destination
                                else:
                                    i/0
            except:
                pass
            try:
                for i , v in fluidMapDictionary2.items():
                    if v == location:
                        index = i
                        for i , v in fluidMapDictionary2.items():
                            if v == destination:
                                destinationIndex = i
                                if index - destinationIndex == 1 or index - destinationIndex == -1:
                                    location = destination
                                else:
                                    i/0
            
            except:
                print("You can only move one city at a time!")

       
                    
           
            print("We are in " + location)
            
        















































































startGame()




