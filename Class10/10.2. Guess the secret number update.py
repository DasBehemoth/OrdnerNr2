#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():
    secret = random.randint(1, 10)

    while True:
        try:
            guess = int(raw_input("Please enter a number between 1 and 10: "))

            if guess == secret:

                print "Congratulations!"
                break

            else:
                print ""
                print "You entered " + str(guess)
                if guess < secret:
                    print "Your guess is too low"
                    print ""
                if guess > secret:
                    print "Your guess is too high"
                    print ""
                new = raw_input("Sorry, this is the wrong number, do you want to try again? (yes/no): ")
                if new == "no":
                    print "The secret number was " + str(secret)
                    break

        except ValueError:
            print "Value Error, try again!"

if __name__=='__main__':
    main()

# wie kann ich feststellen ob die secret number während dem Loop gleich bleibt?