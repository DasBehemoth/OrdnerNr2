print "Create your Daily Menu!"
print ""

daily_menu = {}

while True:
    dish = raw_input("Please enter a new dish: ")
    price = int(raw_input("Please enter price of the new dish: "))
    daily_menu[dish]= price

    new = raw_input("Would you like to enter a new dish? (yes/no): ")

    if new == "no":
        break

text_file = open("daily_menu.txt", "w+")
print""
print "Daily Menu:"
text_file.write("Daily Menu:\n")
print ""
for x in daily_menu:
    print "%s: %s EUR" %(x, daily_menu[x])
    text_file.write("%s: %s EUR" %(x, daily_menu[x]) + "\n")

text_file.close()

# text file speichern hat nicht funktioniert, bzw. ich sehe kein txt file, warum?
