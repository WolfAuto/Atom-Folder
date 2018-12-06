from room import Room
from character import Enemy, Character
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description(
    "A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description(
    "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

living_room = Room("Living Room")
living_room.set_description("A huge room with a large sofa and Flat Screen TV")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.linked_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
living_room.link_room(dining_hall, "west")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("life")
dining_hall.set_character(dave)


tabitha = Enemy(
    "Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("poison")
ballroom.set_character(tabitha)

john = Enemy("John", "A serial killer looking for something important.")
john.set_conversation("Hey there have you seen my important item")
john.set_weakness("bible")
living_room.set_character(john)


life = Item("life")
life.set_description("The only thing a zombie doesn't have")
ballroom.set_item(life)

poison = Item("poison")
poison.set_description("A deadly poison useful against spiders'")
dining_hall.set_item(poison)

book = Item("book")
book.set_description("A holy book which can cure all evil")
living_room.set_item(book)

current_room = kitchen
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
