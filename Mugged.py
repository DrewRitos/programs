import time
import random
import sys

def wordlen(x):
    x.split(" ")
    return len(x)

def ts(x):
    time.sleep(x)
    
def randomchance(x):
    b = random.randint(0,100)
    if x >= b:
        return 1
    else:
        return 0

def printt(x):
    print(x)
    ts(wordlen(x)*0.05)
    print("\n")

def think(x):
    y = "you think to yourself.", "you murmur under your breath.", "you think.", "you tell yourself."
    t = '"'+x+'"'+" "+random.choice(y)
    print(t)
    ts(wordlen(t)*0.05)
    print("\n")

def inputt(x):
    print(x)
    e = input(": ")
    print("\n")
    return e

op = 0
hit = 0

printt("You rub your eyes and blink rapidly, trying to get the haze out of your vision.")
printt("Once you do, you dreamily stare at the shelves of whiskey and bourbon stacked high on the walls.")
printt("You also notice many of the others have left, and only the lonely late timers remained in the booths of the now quiet bar.")
printt('"I should probably get home" you tell yourself, pleading for your legs to obey.')
printt("Shakily, you steady yourself on the black and white tiled flooring and search for an exit")
printt("You spot it by the out of place gumball machine and red tape, and stumble your way to it.")
printt(""""I shoulnd't of drunk so much" you gasp as you clutch your aching stomach.""")
printt("You arrive at the door.")
while True:
    push_pull = inputt("<A> Push or <B> pull the door?")
    if push_pull == "A":
        printt("You push the door open and step out into the fresh air. The usually busy streets are dark and desolate. Creepy.")
        break
    elif push_pull == "B":
        if randomchance(60) == 1:
            printt("You pull on the door handle and soon realize it's a push door.")
        else:
            printt("You pull on the door and loose your grasp, falling flat on your back.")
printt("As soon as you start to walk towards your car in the lot, someone grabs you from behind, covering your mouth, and drags you into an alleyway.")
printt(""""This is a robbery kid; fork over your wallet." he says hurriedly.""")
printt("""You notice the gun he has pointed right at your nose as he looks at you impatiently.""")
printt(""""What're you staring at asshole? Gimme the money!" he hisses at you.""")
while True:
    d1 = inputt("""<A> "I don't have any money! Get lost!"\n<B> "Alright alright! Take it!" *hand him your wallet*\n<C> "No please! Please let me go!" """)
    if d1 == "A":
        break
    elif d1 == "B":
        break
    elif d1 == "C":
        break
    
if d1 == "A":
    if randomchance(10) == 1:
        printt(""""Oh. Alright get lost then." he rasps at you, pushing you out of the alleyway.""")
        printt("You won.")
        sys.exit(0)
    else:
        printt(""""Bullshit!" He hits you with the butt of his gun and you crumple to the cold asphalt.""")
        hit += 1
if d1 == "B":
    printt("You carefully hand him your wallet. The thief starts to search through it, diverting his attention.")
    d2 = inputt("<A> *run away*\n<B> *do nothing*\n<C> *tackle him*")
    if d2 == "A":
        if randomchance(75):















        
