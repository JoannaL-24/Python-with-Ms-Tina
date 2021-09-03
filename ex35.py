from sys import exit

def gold_room():
    """The good ending room, prompt a input and finish the game."""
    print("This room is full of gold. How much do you take?")

    next = input("> ")

    try:
        next = float(next)

        if next < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard!")
    except ValueError:
        print("Man, learn to type a number.")

def bear_room():
    """The bear room, prompt for an input to continue the game."""
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        elif "Fly away" in next:
            cthulhu_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    """The cthulhu room, prompt an input from the player. Call itself if the input does not match with any if or elif."""
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    elif "Fly":
        gold_room()
    else:
        cthulhu_room()

def dead(why):
    """End the game with printed reason."""
    print(why, "Good job!")
    exit(0)

def start():
    """The start of the game, prompt for a input to continue."""
    print("You are in a dark room")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

"""
Study Drill:
1. Google Classroom 
"""