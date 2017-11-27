while True:
    entry = raw_input("Doy you want to continue? (y,n)?")
    if entry == "y":
        print "lets continue"
    elif entry == "n":
        break
    else:
        print "Invalid input,try again"
    break

print "finished"