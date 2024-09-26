#Author: Morgan Mackey
#Created Date: 18 April 2023
#Function: This program helps one decide on what to eat

#importing modules to use in the program
import time
import random


#Exits the program
def program_end():
    print("\033[H\033[J", end="")
    print("Thank you for using the program")
    time.sleep(2)
    return True
  
#First question of the program, the Hunger question.
def first_question():

    #Defines the hunger menu
    HungerQuestion = ["Yes, I am on a diet","I want that gain!","No, Just hungry","Exit"]

    MyNumber = 1
    while MyNumber < len(HungerQuestion):
        for Hunger in HungerQuestion:
            print((str(MyNumber)) + ". " + Hunger)
            MyNumber = MyNumber + 1

    #Runs through the user input and sets the Global hunger answer
    while True:
        Typehunger = input("< Choose an option or " + str(len(HungerQuestion)) + " to quit the program > \n")
        try:
            Numhunger = int(Typehunger)

            if Numhunger <= 0:
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return first_question()
            elif Numhunger > len(HungerQuestion):
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return first_question()
            elif Numhunger == len(HungerQuestion):
                return program_end()
            elif Numhunger < len(HungerQuestion):
                print("\033[H\033[J", end="")
                global hungeranswer
                hungeranswer = HungerQuestion[Numhunger - 1]
                return second_question()
        except:
            print("\033[H\033[J", end="")
            print("You didn't enter a number. Please try again.\n")
            return first_question()

#Second question of the program, proteins list.
def second_question():

    print("Now lets pick your main protein.\n")
    
    #Defines the Protein list
    ProteinQuestion = ["Chicken","Fish","Beef","Turkey","Egg","Surprise Me!","EXIT"]

    MyNumber = 1
    while MyNumber < len(ProteinQuestion):
        for Protein in ProteinQuestion:
            print((str(MyNumber)) + ". " + Protein)
            MyNumber = MyNumber + 1

    #Runs through the user input and sets the Global Potien answer
    while True:
        Typeprotien = input("< Choose what sounds good or " + str(len(ProteinQuestion)) + " to quit the program > \n")
        try:
            Numprotein = int(Typeprotien)
            if Numprotein <= 0:
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return second_question()
            elif Numprotein > len(ProteinQuestion):
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return second_question()
            elif Numprotein == len(ProteinQuestion):
                return program_end()
            elif Numprotein < len(ProteinQuestion):
                print("\033[H\033[J", end="")
                global proteinanswer
                proteinanswer = ProteinQuestion[Numprotein - 1]
                return third_question()
        except:
            print("\033[H\033[J", end="")
            print("You didn't enter a number. Please try again.\n")
            second_question()

#Third question of the program, Sides list
def third_question():

    print("YUM! " + proteinanswer + " Shounds good, now lets pick your side item.\n")
    
    #Defines the sides list
    SidesQuestion = ["Potatoes","Vegetables","Fruit","Pasta","Surprise Me!","EXIT"]

    MyNumber = 1
    while MyNumber < len(SidesQuestion):
        for Sides in SidesQuestion:
            print((str(MyNumber)) + ". " + Sides)
            MyNumber = MyNumber + 1

    #Runs through the user input and sets the Global sides answer
    while True:
        Typesides = input("< Choose what sounds good or " + str(len(SidesQuestion)) + " to quit the program > \n")
        try:
            Numsides = int(Typesides)
            if Numsides <= 0:
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return third_question()
            elif Numsides > len(SidesQuestion):
                print("\033[H\033[J", end="")
                print("The number you enter is not one of the options. Please try again.\n")
                return third_question()
            elif Numsides == len(SidesQuestion):
                return program_end()
            elif Numsides < len(SidesQuestion):
                print("\033[H\033[J", end="")
                global sidesanswer
                sidesanswer = SidesQuestion[Numsides - 1]
                return recipe_search()
        except:
            print("\033[H\033[J", end="")
            print("You didn't enter a number. Please try again.\n")
            return third_question()

#Finds the recipe for the user based on the anwsers to the questions once all questions are asked.
def recipe_search():

  menu = proteinanswer + "," + sidesanswer

  #Runs the random gen if user picked "Surprise me!" in any of the second or third questions.
  if proteinanswer == "Surprise Me!":
    SurPro = ["Chicken","Fish","Beef","Turkey","Egg"]
    Pro = random.choice(SurPro)
  else:
    Pro = proteinanswer
    
  if sidesanswer == "Surprise Me!":
    SurSide = ["Potatoes","Vegetables","Fruit","Pasta"]
    side = random.choice(SurSide)
    menu = Pro + "," + side
  else:  
    menu = Pro + "," + sidesanswer


  #Finds the requested recipe based on the answer to the questions asked.  
  if hungeranswer == "Yes, I am on a diet":
    with open("Diet.txt", "r") as file:
      for lines in file:
        if lines == menu + "\n":
          recipe = open("Recipe.txt", "w")
          while True:
            nextlines = file.readline()
            if nextlines == "END\n":
              recipe.close()
              print("Your recipe will be in a file called Recipe, it will have whats required and directions on how to make it.")
              time.sleep(5)
              return program_end()
            recipe.write(nextlines)
  elif hungeranswer == "I want that gain!":
   with open("Gain.txt", "r") as file:
     for lines in file: 
        if lines == menu + "\n":
          recipe = open("Recipe.txt", "w")
          while True:
            nextlines = file.readline()
            if nextlines == "END\n":
              recipe.close()
              print("Your recipe will be in a file called Recipe, it will have whats required and directions on how to make it.")
              time.sleep(5)
              return program_end()
            recipe.write(nextlines)
  elif hungeranswer == "No, Just hungry":
    with open("Food.txt", "r") as file:
      for lines in file:
        if lines == menu + "\n":
          recipe = open("Recipe.txt", "w")
          while True:
            nextlines = file.readline()
            if nextlines == "END\n":
              recipe.close()
              print("Your recipe will be in a file called Recipe, it will have whats required and directions on how to make it.")
              time.sleep(5)
              return program_end()
            recipe.write(nextlines)

#Main program start
#Creates the wecome screen for the program
outputMenu="""\tWHAT'S TO EAT?

\t_        _
\t \\_(\"/)_/

Let's get started."""
print(outputMenu)

#Clears the screen and waits 3 secs before moving on to the first question.
time.sleep(3)
print("\033[H\033[J", end="")
print("First I need to know a few things, like are you on a diet, trying to gain, or just hungry?\n")
first_question()