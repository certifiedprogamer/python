
print("Backstory:")
print("You are a poor miner looking for riches in a presumably \"cursed\" cave. The locals won't go anywhere near it, but this means its resources are untapped. This better be worth it.")
input("Press enter to continue: ")
stolen_artifact = False
pickaxe_gone = False


def choice(prompt, *choices):
    while True:
        choice = input(prompt).strip()
        if choice in (choices):
            return choice
        else:
            print("That is not one of the options.")


def start():
    print("You're near the entrance of the cave. Do you want to go in, or are you having second thoughts?")
    user_choice = choice(
        "Say \"in\" to go in, or say \"leave\" to turn around and leave:", "in", "leave")
    if user_choice == "in":
        branch()
    else:
        print("You chose to leave the cave and go back home, unable to feed your family.")
        print("Your name will join the many who have died to poverty.")
        exit()


def branch():
    print("You decide to go in and are met with a fork in the cave system.")
    print("The branch on the left is completely dark while something from the branch on the right emits a dim blue light.")
    print("Which do you go in?")
    user_choice = choice(
        "Say right to go \"right\", and \"left\" to go to the left.", "right", "left")
    if user_choice == "right":
        right_branch()
    elif user_choice == "left":
        left_branch()


def left_branch():
    print("You decided to go to the left branch.")
    print("As you go on, you are shrouded in darkness.")
    print("You decide to turn on your flashlight, and you see something on the floor, reflecting its light.")
    user_choice = choice(
        "Say \"take\" to bend down and pick it up, and \"go\" to keep moving forwards: ", "take", "go")
    if user_choice == "take":
        global stolen_artifact
        stolen_artifact = left_take()
    left_continue()


def left_take():
    print("You bend down and grab the unknown object.")
    print("On closer inspection, it appears to be a medium sized piece of gold with strange markings.")
    input("Hit enter to continue:")
    return True


def left_continue():
    print("You continue down the system,")
    if stolen_artifact == True:
        print("with a small fortune in your hand..")
    print("and you eventually come across a vein of silver and get to work.")
    print("After a while, you have mined a lot, but there still is some left.")
    if stolen_artifact == True:
        print("You could leave right now with your gold piece along with everything else and be set for a month or two, or you could keep going.")
    user_choice = choice(
        "Say \"mine\" to keep mining, and \"leave\" to head back: ", "leave", "mine")
    if user_choice == "mine":
        left_greed()
    else:
        left_leave()


def left_greed():
    print("You continue mining.")
    print("Soon, everything is mined, but you still need more.")
    if stolen_artifact == True:
        print(
            "The gold piece whispers to you. It tells you there is much more deeper down.")
        print("You listen to it and continue going down. Eventually, your flashlight runs out of battery, and you are left alone in the dark.")
        print("Nobody will be there to find you.")
        exit()
    else:
        print("With nothing left to do, and your flashlight running out of battery, you leave to return home with the materials you have gotten.")
        print("It is not much, but will last for enough to find a real job.")
        exit()


def left_leave():
    print("You decide to leave with your goods, content with what you've gotten.")
    if stolen_artifact == True:
        print("The piece of gold you found has heated up and burnt a hole through your sack. It and along with most of the silver falls to the ground")
        print("You scramble to pick everything back up, and in the process, the gold scalds your hand.")
        print("It heats up further and begins to melt itself and the silver around it.")
        print(
            "The situation is unsalveageable, and you leave with only burns on your hands.")
        exit()
    else:
        print("It is not much, but it will last long enough to find a real job.")
        exit()


def right_branch():
    print("You decided to go to the right branch.")
    print("You are met with many glowing crystals and are shocked by their beauty.")
    user_choice = choice(
        "Say \"mine\" to attempt to mine the crystals, \"go\" to keep moving forwards, and \"stay\" to admire the crystals: ", "mine", "stay", "go")
    if user_choice == "stay":
        print("You stand still and admire the crystals.")
        print("You stand there for a long time.")
        print("Eventually, your body gives out and you collapse to the floor, next to the precious crystals.")
        exit()
    elif user_choice == "mine":
        print("You hit a crystal with your pickaxe and it shatters, its pieces losing their illuminous properties as they fall to the floor")
        print("As pretty as they were, you can't bring the crystals back in this state.")
        print("You decide to move on.")
        input("Hit enter to continue:")
    right_continue()


def right_continue():
    print("As you continue along the system, you find a black growth spread across the right wall. It spans across the entire tunnel. ")
    user_choice = choice(
        "Say \"mine\" to attempt to mine into the growth, and \"go\" to ignore it.", "mine", "go")
    if user_choice == "mine":
        global pickaxe_gone
        pickaxe_gone = right_stolen_pickaxe()
    right_ignore()


def right_stolen_pickaxe():
    print("As you hit the growth with your pickaxe, it snags onto it and envelops half of your pickaxe's head.")
    print("You fail continuously to pull it out, and eventually, you give up and move on.")
    input("Hit enter to continue:")
    return True


def right_ignore():
    print("You continue along the system, cautious of the growth.")
    print("As you reach the end of the growth, you come across an opening near where it ends.")
    print("The opening seems to lead into a small chamber.")
    if pickaxe_gone == True:
        print("Since your pickaxe is out of commission, it might be a good idea to check it out.")
    user_choice = choice(
        "Say \"inspect\" to go into the opening, and \"go\" to keep moving.", "inspect", "go")
    if user_choice == "inspect":
        print("You crawl into the opening, reaching the chamber after a bit.")
        print("You step out of the tunnel and into the chamber and find 2 skeletons at your feet and nothing else.")
        print("You quickly turn back to try and get out, but you see the growth has moved over the opening, sealing you in.")
        exit()
    else:
        print("You keep going and eventually come to another fork in the path. The left path goes up, and the right path goes down.")
        right_labyrinth()


def right_labyrinth():
    user_choice = choice(
        "Say \"left\" to go to the left, and \"right\" to go to the right.", "left", "right")
    if user_choice == "left":
        print("You go to the left path.")
    elif user_choice == "right":
        print("You go to the right path.")
    print("You come across another fork. This time the left goes down and the right goes up.")
    user_choice = choice(
        "Say \"left\" to go to the left, and \"right\" to go to the right.", "left", "right")
    if user_choice == "left":
        print("You go to the left path.")
    elif user_choice == "right":
        print("You go to the right path.")
    print("There's another fork in the system.")
    print("You should probably turn back.")
    while user_choice != "back":
        user_choice = choice(
            "Say \"left\" to go to the left, and \"right\" to go to the right, or \"back\" to turn back.", "left", "back", "right")
        if user_choice == "back":
            print("You turn around in an attempt to leave, but where there should have been one exit, there's another fork.")
            right_end()
        elif user_choice == "left":
            print("You go to the left.")
        elif user_choice == "right":
            print("You go to the right.")
        print("There's yet another fork in the system.")


def right_end():
    print("The cave continues to branch out")
    print("No matter where you go, there's always two paths you end up on.")
    print("You will never leave this place.")
    exit()


start()
