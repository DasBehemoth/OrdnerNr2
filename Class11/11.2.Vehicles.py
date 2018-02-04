class Vehicle:
    def __init__(self, brand, model, kilometers_done):
        self.brand = brand
        self.model = model
        self.kilometers_done = kilometers_done

    def list_vehicles(self):
            print ""
            print self.brand + self.model + " (%s)"%self.kilometers_done
            print ""

    def print_brandmodel(self):
        return self.brand + self.model

def add_vehicle(moving_things):
    brand = raw_input("Enter the vehicle brand: ")
    model = raw_input("Enter the vehicle model: ")
    kilometers_done = raw_input("How many kilometers did it move so far: ")

    new = Vehicle(brand=brand, model=model, kilometers_done=kilometers_done)
    moving_things.append(new)

    print ""
    print new.print_brandmodel() + " was successfully added to your list of things that move."

def edit_km(moving_things):
    print "Select the vehicle which you'd like to edit:"

    for vehicle in enumerate(moving_things):
        print vehicle.print_brandmodel

    print ""  # empty line
    selected_id = raw_input("What contact would you like to edit? (enter ID number): ")
    selected_contact = contacts[int(selected_id)]

    new_email = raw_input("Please enter a new email address for %s: " % selected_contact.get_full_name())
    selected_contact.email = new_email

    print ""  # empty line
    print "Email updated."
    # ... you can do the same for other fields.


def main():
    print "Welcome to your list of moving things"


    horse = Vehicle(brand="Horse", model =" drawn-carriage", kilometers_done="50km")
    husky = Vehicle(brand="Husky", model =" drawn-sleigh", kilometers_done="150km")
    shark = Vehicle(brand="Shark", model =" drawn-boat", kilometers_done="0,1km")
    moving_things = [horse, husky, shark]

    print "List of Vehicles: "
    print ""

    for vehicle in moving_things:
        print vehicle.list_vehicles()

    if not moving_things:
        print "You'll probably have to walk"

    while True:
        print ""
        print "What would you like to do?"
        print "a) Add a new vehicle"
        print "b) Edit a vehicle"
        print "c) Quit the program."
        print ""

    abc = raw_input("Enter your a, b or c: ")
    print ""

    if abc.lower() == "a":
        add_vehicle(moving_things)
    elif selection.lower() == "c":
        print "Thank you, bye bye!"
        break
    else:
        print "Please do as you're told and try again."
        continue

if __name__ == "__main__":
    main()
