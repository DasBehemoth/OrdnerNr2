class human (object): #container fuer viele sachen (zahlen, namen etc)
    def __init__(self, age, name): # self ignoriern, stehen lassen
        """
        :type age: int
        :type name: str
        """
        self.age = age # attributes
        self.name = name

    def get_older(self):
        self.age += 1 # += erhoeht den wert um den wert nach em = (statt self.age = self.age + 1)
    def get_younger(self):
        self.age -= 1
    def greet(self):
        return "Hello I'm " + self.name + "and i am" + str(self.age) + "."

if __name__ == '__main__':
    Alfred = human(19, "Alfred") # alfred ist eine instanz der klasse human (erschaffen aus klasse), klammer heisst rufe init funktion
    print Alfred.age
    print Alfred.name
    Alfred.get_younger()
    print Alfred.age
    Alfred.greet()
    print Alfred.name

