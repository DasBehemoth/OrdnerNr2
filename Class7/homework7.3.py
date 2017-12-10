print "Welcome to guess the secret number!"
print ""

secret=42

while True:
  guess = int(raw_input("Please enter a number between 1 and 100: "))

  if guess == secret:

    print "Congratulations!"
    break

  else:
    print ""
    print "You entered " + str(guess)
    print "Sorry, this is the wrong number, try again"

