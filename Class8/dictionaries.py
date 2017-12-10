a_dict = {}
points = {"Alfred":10,
        "Bettina": 100,
        "Christian": 50,
        "Doris": 75}

print points #Dictionaries haben keine fixe reihenfolge

# reference

print points ["Alfred"]

for name in ["Alfred", "Bettina"]:
    print name, points [name]


# change

points["franz"] = 40

for name in ["Alfred", "Bettina"]:
    points[name] +=10
    print points, points[name]

#update
points.update({"erwin": -10, "alfred": 200}) #hinzufuegen oder ueberschreiben
