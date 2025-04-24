from anytree import Node, RenderTree
import time
from termcolor import colored
import random

weapons = []
global blacksmith_found  #global variables to update the map during the game
blacksmith_found = False
global medic_found
medic_found = False
global sword_found
sword_found = False
global magician_found
magician_found = False
global cave_found
cave_found = False
global juction_found
junction_found = False
global gate_found
gate_found = False

global dragon_hp
dragon_hp = 100
global health
health = 100
global dragon_alive
dragon_alive = True


def Map():  #the map in your house
    print("The map:\n")
    global blacksmith_found
    global medic_found
    global castle_found
    global junction_found
    global gate_found
    global cave_found
    house = Node("house")
    village = Node(colored("village", "green"), parent=house)
    forest = Node(colored("forest", "green"), parent=house)
    if blacksmith_found:
        blacksmith = Node("blacksmith", parent=village)
    if medic_found:
        medic = Node("medic", parent=village)
    if junction_found:
        junction = Node("junction", parent=forest)
    if magician_found:
        magician = Node("magician", parent=junction)
    if cave_found:
        cave = Node("cave", parent=junction)
    if gate_found:
        gate = Node("gate", parent=junction)

    for pre, fl, node in RenderTree(house):
        print("%s%s" % (pre, node.name))


def home():  #print map if you arrive at home
    print("\n")
    Map()


def blacksmith():  #blacksmith leaf
    global blacksmith_found
    blacksmith_found = True
    try:
        your_weapon = weapons.pop()
        weapons.append(your_weapon)
    except IndexError:
        your_weapon = str
        pass
    if your_weapon == 'broken_sword':
        print("Well done, wait a sec and I will repair the sword for you!")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("There is your repaired sword, use it carefully!")
        weapons.append("sword")
        time.sleep(2)
        print("\n* new item received:", colored("sword", "blue"), "*\n")
        time.sleep(2)

    else:
        print(
            "\nBlacksmith: Bring me a broken sword and I will repair it for you."
        )
        time.sleep(3)
        print("Blascksmith: You don't have a sword, so don't waste my time!\n")
        time.sleep(3)


def hut():  #magician leaf
    global magician_found
    magician_found = True
    print("You are walking by the river...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")

    time.sleep(1)
    print("There is a small, old hut in front of you.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Old man: Hello wonderer, what are you looking for?")
    time.sleep(3)
    print(
        "Old man: I heared about the terrible things that happend last week in the village"
    )
    time.sleep(3)
    print(
        "Old man: Find me, if you ever get in a real trouble and I will help you!"
    )
    time.sleep(2)
    input("What do you want to say?: ")
    time.sleep(1)
    print("The old man raised his eyebrows and dissapeared.")
    time.sleep(3)
    print("\nYou decided to return to the forest...\n")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)


def deep_forest():  #junction to the gate and the cave
    global junction_found
    junction_found = True
    print("You are walking deeper to the forest")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    gate_cave()


def medic():  #medic leaf
    global medic_found
    global health
    medic_found = True
    if health <= 75:
        print(
            "\nMedic: Your health is low!\nMedic: I will heal you, but you must try and defeat that Dragon again!!"
        )
        print("Health:", health)
        time.sleep(2)
        print("\nMedic: This may hurt a little")
        heal = 100 - health
        health = health + heal
        time.sleep(2)
        print("Medic: Now go and finish the fight!!")
        print("Health:", health)

    elif health >= 76:
        print("\nMedic: I can heal you if you get injured.")
        print("Your hp:", health)
        time.sleep(3)
        print("Medic: Now get out of here, you are fine!")
        time.sleep(2)
        print("...")
        time.sleep(2)


def gate_cave():  #gate or cave junction
    while True:
        print("You see a", colored("cave", "green"), "and a big stone",
              colored("gate", "green"), ".")
        print("Where do you want to go? (", colored("back", "green"), ")")
        token = input()
        if token.startswith("g"):
            print("There is something written on the gate...")
            gate()

        if token.startswith("c"):
            time.sleep(2)
            print("\n\n")
            print(r"""     ,-------,  ,  ,   ,-------,
      )  ,' /(  |\/|   )\ ',  (
       )'  /  \ (qp)  /  \  '(
        ) /___ \_\/(_/ ___\ (
         '    '-(   )-'    '
                )w^w(
                (W_W)
                 ((
                  ))
                 ((
                  )  """)
            time.sleep(1)
            print("\n\n")
            print(
                "There is a small, angry looking dragon in front of you! Do you want to",
                colored("fight", "green"), "or", colored("run", "green"),
                "away?")
            cave()

        if token.startswith("b"):
            time.sleep(1)
            print("...")
            time.sleep(1)
            break


def gate():
    global dragon_alive  #the gate leaf
    global gate_found
    global health
    gate_found = True
    while True:  #gate
        print("*Say a password to open the gate,", colored("return", "green"),
              "if you don't know the password.*")
        token = input()
        if "bitcoin" in token and not dragon_alive:
            print("Congratulation, you found a bitcoin!")

            time.sleep(200)
        if token.startswith("r"):
            break
        else:
            print("Wrong password, your hitpoints were reduced by 5.")
            time.sleep(1)
            health -= 5
            if (health < 0):
                game_over()
            print("Your hp:", health, ".")
            time.sleep(1)
            print("...")
            time.sleep(1)
            break


def cave():  #the cave leaf
    global cave_found
    cave_found = True
    while True:
        token = input()
        time.sleep(1)
        if token.startswith("f"):
            dragon_fight()
            break

        if token.startswith("r"):
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            break


def dragon_fight():
    global dragon_hp
    global health
    global dragon_alive
    your_weapon = weapons.pop()
    weapons.append(your_weapon)
    if your_weapon == "sword":
        while True:
            print("Spam as many messages in 5 seconds to deal damage!! ")
            print("Start the", colored("fight", "green"), "or",
                  colored("run", "green"), "away.")
            token = input()
            if token.startswith("f"):
                t_end = time.time() + 5
                messages = []
                dragon_dmg = random.randint(15, 30)

                while time.time() < t_end:
                    message = input()
                    messages.append(message)

                count = len(messages)
                dragon_hp -= count
                health -= dragon_dmg
                print("\n\nYou dealed: ", count, " dmg to the dragon.")
                time.sleep(1)
                if dragon_hp > 0 and health > 0:
                    print("\nThe dragons now has", dragon_hp,
                          " hitpoints left.")
                    print("\n\nThe dragon dealed", dragon_dmg,
                          "damage to you.")
                    print("You have", health, "hp left.\n\n")
                    continue
                if dragon_hp < 0 and health > 0:
                    time.sleep(2)
                    print(r"""                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                     
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              ')""")
                    time.sleep(5)
                    print("\n\n\n")
                    print(
                        "Congratulation, you trained your dragon! The password is bitcoin."
                    )
                    time.sleep(4)
                    dragon_alive = False
                    break
                if ((dragon_hp > 0) and (health < 0)) or ((dragon_hp < 0) and
                                                          (health < 0)):
                    game_over()
            if token.startswith("run"):
                break

    else:
        print(
            "\nYou need a weapon to fight the dragon! Otherwise you have no chance of succes.\n"
        )
        time.sleep(2)


def game_over():
    print("\n\n")
    print(r"""                                 
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |                  ||
          |                  ||
  *       | *   **    * **   |**      **
   \)),,..,/.,(//,,..,,\||(,,.,\\,.((//)""")
    print("\n\n")
    time.sleep(5)
    print("You were defeated.")
    print("Thank you for playing.")
    time.sleep(500)

    #this is where the game starts


print("\n" * 5)
print('             __                  __ ')
print('            ( _)                ( _)')
print('           / / \\               / /\_\_')
print('          / /   \\             / / | \ \ ')
print('         / /     \\           / /  |\ \ \ ')
print('        /  /   .  \ .       / /   /|  \ \ ')
print('       /  /    |\_ /|      / /   / \   \_\ ')
print('      /  /  |\/ _  _| \   / /   /   \    \\')
print('     |  /   |/  0 ,0\    / |    |    \    \\')
print('     |    |\|      \_\_ /  /    |     \    \\')
print('     |  | |/    \.\ o\o)  /      \     |    \\')
print('     \    |     /\\`v-v  /        |    |     \\')
print('     | \/    /_| \\_|  /         |    | \    \\')
print('     | |    /__/_ `-` /   _____  |    |  \    \\')
print('     \|    [__]  \_/  |_________  \   |   \    ()')
print('       /   [___] (    \         \  |\ |   |   //')
print('      |    [___]                  |\| \|   /  |/')
print('     /|    [____]                  \  |/\ / / ||')
print('    (  \   [____ /     ) _\      \  \    \| | ||')
print('     \  \  [_____|    / /     __/    \   / / //')
print('     |   \ [_____/   / /        \    |   \/ //')
print('     |   /  ----|   /=\____   _/    |   / //')
print('  __ /  /        |  /   ___/  _/\    \  | ||')
print(' (/-(/-\)       /   \  (/\/\)/  |    /  | /')
print('               (/\/\)           /   /   //')
print('                     __________/   /    /')
print('                     \____________/    (   \n')
print('                                    ',
      colored("(Art by Shanaka Dias)", "grey"), "\n\n")

time.sleep(2)
print("Recently, there was a dragon seen near to your village.")
time.sleep(3)
print("People are affraid that the dragon lives somewhere in a forest.")
time.sleep(3)
print("You are now in your house.")

#the main loop
while True:
    home()
    token = input("\nChoose a place from the map you want to visit: ").lower()

    if token.startswith("f"):  #the forest loop
        print("You are walking to the forest...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print('You arrived into the forest.\n')
        time.sleep(1)
        if not sword_found:
            print('\nYou found a', colored('broken sword', 'cyan'))
            time.sleep(2)
            print('\n\nDo you want to take the sword?', colored(
                "yes", "green"), ",", colored("no", "green"))
            token = input()
            if token.startswith("y"):
                sword_found = True
                weapons.append('broken_sword')
                time.sleep(1)
                print("\n* new item received: ", colored(
                    'broken sword', "cyan"), "*\n\n")
                time.sleep(2)
            else:
                print("I would definitely take the sword.\n")
                time.sleep(2)
        while True:  #magician or deep forest junction
            print("Do you want to go", colored("right",
                                               "green"), "(by the river),",
                  colored("left", "green"),
                  "(deeper to the forest) or back to your",
                  colored("house", "green"), "?")
            token = input()
            if token.startswith("r"):
                hut()
                continue
            if token.startswith("l"):
                deep_forest()
                continue

            if token.startswith("h"):
                print("You are on your way back home.")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                break
            else:
                print("I dont understand.")
                time.sleep(2)

    if token.startswith("v"):  #the village loop
        print("You are walking to the village... ")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("You arrived to the village. ")
        time.sleep(1)
        print("\n" * 2)
        while True:
            print("Do you want to talk with a", colored("medic",
                                                        "green"), ", with a",
                  colored("blacksmith", "green"), "or go back to your",
                  colored("house", "green"), "?")
            token = input()
            if token.startswith("b"):
                blacksmith()
                continue
            if token.startswith("m"):
                medic()
                continue
            if token.startswith("h"):
                print("You are on your way back home.")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                break
            else:
                print("\nWhat do you mean?\n")
                time.sleep(2)
