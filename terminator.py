import random
import time
#python3.6

defaultInventory = {'Ration' : 1, 'Hand-Gun' : 1, 'Bullets' : 12, 'Body Armor' : 1, 'Knive' : 1}
firstLoot = ['Ration', 'Bullets', 'Pulse Rifle']
newInventory = defaultInventory

def displayIntro():
    print()
    print('The year is 2029.')
    print('Los Angeles has become a total wasteland due to the ongoing war against the machines.')
    print('It was August 29, 1997 the world changed in a day known as Judgement Day.')
    print('You begin your journey among the nearly-extinct living hoping for survival')
    time.sleep(3)


def displayInventory(inventory):
    print()
    print('Your Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(defaultInventory.get(k, 0)) + ' ' + k)
        time.sleep(1)
    print('Total number of items:   ' + str(item_total))
    print()

def addToInventory(inventory, addedLoot): #adding a list 'addedLoot' to a dictionary 'inventory'
    print()
    for i in range(len(addedLoot)): #note you can use range() and len() on a list. Loops through code_block according to number of items in list
        inventory.setdefault(addedLoot[i], 0) #add a new key equal to list[i]
        inventory[addedLoot[i]] = inventory[addedLoot[i]] + 1 #dictionary[list[i]] + 1 value.

    return inventory

def firstAction():
    time.sleep(2)
    print('Suddenly, a T-800 appears from a nearby building!')
    move = ''
    while move != '1' and move != '2':
        print()
        time.sleep(2)
        print('Choose whether to run towards a refinery (1) or towards the hospital (2)...')
        move = input()
    return move

def secondAction():
    time.sleep(2)
    print()
    print('In the place you found shelter...')
    time.sleep(2)
    print('You locate a storage locker containing some supplies and add it to your inventory...')
    time.sleep(2)
    print('You take these items and pack them into your backpack...')
    addToInventory(newInventory, firstLoot)
    displayInventory(newInventory)

def firstEffect(action):
    print('You sprint towards your chosen building...')
    time.sleep(2)
    print('The T-800 has spotted you...')
    time.sleep(2)
    print('You immediately hear a blast of fire towards your direction...')
    time.sleep(2)
    print()

    survivalEffect = random.randint(1, 2)

    if action == str(survivalEffect):
        print('...but fortunately dodge the incoming fire and escape the terminator.')
        secondAction()

    else:
        print('...and become pierced by a wave of gunfire. ')
        time.sleep(2)
        print('YOU HAVE BEEN TERMINATED....')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Yes' or playAgain == 'Y':

    displayIntro()

    displayInventory(defaultInventory)

    choosen_action = firstAction()

    firstEffect(choosen_action)

    print()
    print('Do you want to play again? (yes or no)')
    playAgain = input()
