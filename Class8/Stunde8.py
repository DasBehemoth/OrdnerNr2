a_list = []
b_list = [1,2,3,4]

print a_list
print b_list

#referenzieren

print b_list[1]
b_list[1]=10 #ist mutable, das letzte zaehlt
print b_list

#slicen

print b_list[1:3]
print b_list[1:-1] #-1 ist von hinten zaehlen
print b_list[-2:] # -2 bis zum Ende
print b_list[::-2] #doppelterdoppelpunkt jeder zweite wert von hinten, von vorne ist ohne minus
print b_list[::-1] # ruft jeden wert auf aber rueckwaerts

#[start : end : iterationsrule
#iterationrule <0: reverse
#iterationruel = 2 : every other (jeder zweite wert)

#append = an die letzte stelle was hinzufuegen

b_list.append(5)
print b_list



#remove (bezieht sich auf element)

b_list.remove(3)
print b_list



#extend (am ende dranhaengen) += ist dasselbe wie extend.

b_list.extend([0,77,99])
print b_list
b_list+= [100,101]
print b_list