class human (object): #container fuer viele sachen (zahlen, namen etc)
    def __init__(self, age, name): # self ignoriern, stehen lassen
        """
        :type age: int
        :type name: str
        """
        self.age = age # attributes
        self.name = name

if __name__ == '__main__':
    Alfred = human(19, "Alfred") # alfred ist eine instanz der klasse human (erschaffen aus klasse), klammer heisst rufe init funktion
    print Alfred.age
    print Alfred.name