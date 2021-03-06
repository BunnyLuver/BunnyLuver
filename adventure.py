money = 120
#money_left()
def money_left():
    global money
    print("\nYou now have " + str(money) + " microbucks left.")
    print("What would you like to do with it? (1 or 2)")
    print("1) Save the rest up to buy a house later")
    print("2) Buy a hoverboard")

    answer = input(">")

    if answer == "1":
        print("Good idea, this will be a good investment.")

    elif answer == "2":
        money -= 50
        print(" You decided to buy the cheapest hoverboard you can find.")
        print("You buy a hoverboard for 50 microbucks.  It says it can hold 2 people.")
        print("You have " + str(money) + " microbucks left.")


#clothes_shop
def clothes_shop():
    print("\nYou enter the clothes shop and are given 2 options.")
    print("You can either buy a blue suit with one pocket and minimal tech for 30 microbucks.")
    print("Or you can buy a purple suit with 4 pockets and a fair amount of tech for 45 microbucks.")
    print("What will you do? (1 or 2)")
    print("1) Blue suit, 30 microbucks")
    print("2) Purple suit, 45 microbucks")

    answer = input(">")

    if answer == "1":
        global money
        money -=30
        print("\nYou chose the blue suit with minimal tech and saved some money.")
        print("You now have " + str(money) + " microbucks.")

    elif answer == "2":
        money -= 45
        print("\nYou chose the purple suit with a fair amount of tech.  Good choice.")
        print("You now have " + str(money) + " microbucks.")

    else:
        game_over("\nYou can't buy it if it doesn't exist.")

#Bakery
def bakery():
    print("\nYou enter the bakery looking for some food.")
    print("\nThere is a large selection of food.")
    print("\nWhat will you choose? (1 or 2)")
    print("1) Donut and coffee: 5 microbucks")
    print("2) Bagel and hot cocoa 5 microbucks")

    answer = input(">")
    if answer == "1":
        global money
        money -= 5
        print("\nYou buy a donut and coffee for 5 microbucks.")
        print("You now have " + str(money) + " microbucks.")

    elif answer == "2":
        print("\nYou buy the bagel and hot cocao for 5 microbucks.")
        print("You now have " + str(money) + " microbucks.")


# pay day
def pay_day():
    print("\nYou worked for 8 hours.  The sun is down now. ")
    print("You earned 120 microbucks for a hard day of work.")
    print("You were also given a virtual bank for free which they put on a little handheld device.")
    print("It seems to work like a credit card, and everyone gets one when they get their first job.")
    print("\nWhat will you do next? (1 or 2)")
    print("1) Buy some clothes to fit in")
    print("2) Buy some food to eat")

    answer = input(">")

    if answer == "1":
        print("\nYou need clothes.  You set out for the clothes shop.")
        clothes_shop()

    elif answer == "2":
        print("\nYou have to buy some food to eat.  You set out for the local bakery.")
        bakery()

    else:
        print("\n Do you even have number keys?")


# book store
def book_store():
    print("\nYou suddenly see a book store.")
    print("The window shows a display, Hiring Humans, 15 microbucks an hour.")
    print("What will you do? (1 or 2)")
    print("1) Apply for the job")
    print("2) Quit Game")

    answer = input(">")

    if answer == "1":
        print("\n Your application is accepted and you start the job.")
        print("Your job is to program the robots to retrieve the books and interact with customers.")
        pay_day()

    elif answer == "2":
        game_over("Goodbye for now, come back soon.")

    else:
        game_over("The last thing you hear is the sound of people weeping because of your dreadful typing.")

#Coffee Shop
def coffee_shop():
    print("\n It suddenly occurs to you you don't have any money.")
    print("You see a flyer, human help needed 15 microbucks an hour, no experience necessary.")
    print("What will you do? (1 or 2)")
    print("1) Apply for the job")
    print("2) Explore the future")

    answer = input(">")

    if answer == "1":
        print("\nYour application is accepted and you start the job.")
        print("Your job is to program the robots to make coffee and interact with customers.")
        pay_day()

    elif answer == "2":
        print("\nThe city has tall buildings and sleek futuristic technology.")
        print("\nThe city is bustling with people and you notice that everyone is wearing the same kind of clothes.")
        print("You want to fit in, but you don't have money to get clothes.")
        book_store()

    else:
        game_over("You need a class in typing numbers properly.")


# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()


# future room
def future_room():
  # some prompts
  print("\nYou realize ")
  print("\nYou could stay in the future and build a life for yourself!")
  print("But that would mean leaving your friends and family back home.")
  print("What would you do? (1 or 2)")
  print("1). Go to the future")
  print("2). Stay in the present")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    print("\nThe future is really cool.")
    coffee_shop()
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are an honest man! Congrats you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")


# cookie room
def cookie_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou enter a room full of cookies!")
  print("Behind the cookies you find a futuristic looking keycard")
  print("You notice a door with a keycard reader")
  print("What would you do? (1 or 2)")
  print("1). Eat all the cookies.")
  print("2). Open the door.")

  # take input()
  answer = input(">")

  if answer == "1":
    # dead()
    game_over("The cookies were poisoned!  You die instantly.")
  elif answer == "2":
    # go to future_room()
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room()
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


# bear room
def cake_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThere is an unlimited supply of cake!")
  print("But what's this? Behind the cake you find a futuristic looking keycard.")
  print("You notice a door with keycard reader.")
  print("What would you do? (1 or 2)")
  print("1). Eat all the cake")
  print("2). Open the door")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("The cake was poisoned you died instantly.")
  elif answer == "2":
    # future
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")


#START HERE#


def start():
 # money = int(120)
  # give some prompts.
  print("\nYou are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead player to cake room)
    cake_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    cookie_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()