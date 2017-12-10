# zahlen bis 100

print range(101)

# wenn zahl gerade print "yu"

for number in range (1,101):
    if number % 2 == 0:
        print "yu", number
    elif number %2 !=0 and number > 50:
        print "yo", number
    elif number < 20:
        print "ye", number
    else:
        print number

# wenn zahl ungerade und groesser 50: print "yo"
# wenn zahl kleiner 30 print "ye"
# sonst pritne die zahl