print "Welcome to the Fizzbuzz game!!"

while True:
        number = raw_input("Enter a number between 1 and 100: ")
        number = int(number)
        for number in range(number,number+1):
            if number % 3 == 0 and number > 0 and number <101:
                print "Fizz"
            elif number % 5 == 0 and number > 0 and number <101:
                print "Buzz"
            elif number % 3 == 0 and number % 5 == 0 and number > 0 and number <101:
                print "FizzBuzz"
            elif number > 0 and number <101:
                print number
            else:
                print "Sorry, you didn't enter a number between 1 and 100, try again!"