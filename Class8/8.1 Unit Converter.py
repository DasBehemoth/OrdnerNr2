print "Unit Converter"
print ""

while True:
    user = raw_input("Hello there, what's your name? ")

    if len(user) > 0 and user.isalpha():
      print "Hello %s, welcome to the unit converter! Please enter below the kilometers, which you want to convert into miles." %(user.upper())
      print ""
      break

    else:
        print "Enter a name"
        print ""

while True:
  km = raw_input("Enter kilometers: ")

  try:
      km = float(km)

      miles = km * 0.621371

      print "%s kilometers is %s miles." %(km, miles)
  except ValueError:
      print "Value Error. Enter a number, not a letter!" # wie mache ich, dass nach dem Value Error wieder "try" kommt und nicht "choice"?

  choice = raw_input("Would you like to make another conversion? (y/n) ")

  if choice != "y":
      print "Thank you, goodbye!"
      break


