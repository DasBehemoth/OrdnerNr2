print "Welcome to the Fizzbuzz game!!"

number = raw_input("Enter a number between 1 and 100: ")

try:
    number = int(number)
    for number in range(1, number+1):
        if number % 3 == 0:
            print "Fizz"
        elif number % 5 == 0:
            print "Buzz"
        elif number % 3 == 0 and number % 5 == 0:
            print "FizzBuzz"
        else:
            print number

except:
    print "Sorry, you didn't enter a number between 1 and 100, try again!"





