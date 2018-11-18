'''
    Napoleonic War Simulator

    You can either play as the French or the British

    The "rooms" are a number of battlefields. The goal will to be to win each battle
    and make it to the enemies capital - London or Paris.

    In order to win the battle you need more soldiers, the ratio of soldiers between the two
    armies will decide how many soldiers you lose in a battle.

    To get more soldiers you will need to pillage towns. As you get further along there's a chance
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
    mySoldiers = 50
    
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
If you wait until later battles to gather soldiers you have a higher chance of being ambushed.
You will recruit less soldiers as well.




''')

def chooseFaction():
    try:
        choice = int(input(''' Choose a faction:\n
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
        print('''
Welcome, Napoleon!\n
    We are in Paris. The English are ready to attack! What should we do?
    ''')
    else:
        print('''
Welcome, Lord Nelson!\n
    We are in London. The French are ready to attack! What should we do?
    ''')


    
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








def battle(location,mySoldiers,theySoldiers):
    if mySoldiers > theySoldiers:
        casualties = 3 * int(mySoldiers/theySoldiers)
        print("Battle Won! You lost " + str(casualties) + " soldiers\n" +"We have taken " + location)
        return(casualties)
    else:
        print("You lost the battle, and the war")
        sys.exit
   





def running(location,mySoldiers): # The game loop
    i = 0
    dictionary = {"Paris" : 54,             # A dictionary representing the number of soldiers at each location
                  "Chartres" : 70,
                  "Versailles" : 70,
                  "Le Havre" : 67,
                  "Amiens" : 54,
                  "Brighton" : 40,
                  "Calais" : 70,
                  "Hastings" : 67,
                  "London" : 54}
    while i != "Quit":
        i = input('''
Enter "Map" to show map\n                   
Enter "Attack" to attack\n
Enter "Pillage" to Gather troops\n
Enter "Move to ___" to move your troops"\n
Enter "Quit" to End

Soldiers = ''' + str(mySoldiers) + " Location = " + location + "\n")

        header("Napoleonic War Simulator ")
        
        if i == "Attack":
            mySoldiers = mySoldiers - battle(location,mySoldiers,dictionary[location])
            
        
            
        elif i == "Map":
            showMap()

        if i == "Pillage":
            if dictionary[location] == 54:
                print("You can't pillage your own city!")
            elif random.randint(1,len(location)) == 2 or 5 or 7:
                print("You have been ambushed while pillaging!")
            else:
                mySoldiers = mySoldiers + random.randint(7,19)
        
            
















































































startGame()




