print "Welcome to guess the secret number!"
print ""

secret=42

guess = int(raw_input("Please enter a number between 1 and 100: "))

if guess == secret:

    print "Congratulations!"

else:
    print ""
    print "You entered " + str(guess)
    print "Sorry, this is the wrong number, try again"

