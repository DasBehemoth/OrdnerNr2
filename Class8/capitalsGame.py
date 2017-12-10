
import random
punkte = 0



while True:
    user = raw_input("Hello there, what's your name? ")

    if len(user) > 0 and user.isalpha():
      print "Hello %s, welcome to the capitals game!" %(user.upper())
      break

    else:
        print "Enter a name"



capitals = {"France": "Paris", "Iceland": "Reykjavik","Denmark": "Copenhagen", "Lithuania": "Vlnius", "Canada": "Ottawa", "Austria":"Vienna"}


current_country = random.choice(capitals.keys())

guess= raw_input("Please enter the capital of "+current_country +": ")



