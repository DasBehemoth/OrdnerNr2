print("Moose Quiz")

question = 0    # Tells us which questions the user has completed
questions = ["What is the average life span of a moose?: ",
             "How much do moose eat on a daily basis?: ",
             "The fastest moose ran...?: "]

userAnswers = ["","",""] # Stores the users answers

answers = ["a. 10 - 14 years\nb. 15 - 25 years\nc. Blue\nd. 26 - 35  years\n",
           "a. 24 lbs a day\nb. 39 lbs a day\nc. 67 lbs a day\nd. 73 lbs a day",
           "a. 20 mph\nb. 25 mph\nc. 35 mph\nd. 40 mph"]

correct = 0

while question < 3:
   print(questions[question])
   print(answers[question])
   answers[question] = input("To answer, pick a letter or leave it blank to skip it: ").lower()

   if question == 0:
       if answers[question] == "a":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Good Job! That is correct.")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "c":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()
       else:
           print("Invalid character, please try again.")

   elif question == 1:
       if answers[question] == "a":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "c":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Terrific! You got it right!")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()
       else:
           print("Invalid character, please try again.")

   elif question == 2:
       if answers[question] == "a":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "c":
           print()
           print("Amazing! You're awesome!")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()
           print("Thanks for playing!")
       again = input("Would you like to play again?: ")