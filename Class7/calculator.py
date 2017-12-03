# print welcome to user
greeting = "Welcome!"
print greeting
print "=" * 10

# read user input for operation

while True:
    operation_symbol = raw_input("Please enter an operaton (+,-,*,/): ")
    print "you entered  " + operation_symbol
    if operation_symbol in ["+","-","*","/"]:
        break
    else:
    print: "Please enter a valid operation, yo entered:" + operation_symbol

# read user input for first value

x = int(raw_input("Wert 1:"))
print "you entered" + str(x)

# read user input for second value

y = int(raw_input("Wert 2:"))
print "you entered" + str(y)

# calculate

if operation_symbol == "+":
    print x + y
elif operation_symbol == "-":
    print x - y
elif operation_symbol == "*":
    print x * y
elif operation_symbol == "/":
    print x / y
else:
    print "Enter correct symbol"


# print result