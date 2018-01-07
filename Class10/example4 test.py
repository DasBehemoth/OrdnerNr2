import example2 as calk # man kann es umbenennen

def check_addition():
    assert calk.addition (10,20) == 30 # assert checkt ob das das was dannach kommt wahr ist # TEST DRIVEN DEVELOPMENT (TDD) nennt man dieses testen
    assert calk.addition (10, -10) == 0

def check_subtract():
    assert calk.subtrahieren(2,3) == -1

def check_multi ():
    assert calk.multiplizieren(3,4) == 12

def check_div ():
    assert calk.dividieren(10, 5) == 2


if __name__ == '__main__':
    check_addition()
    print "passed"
    check_subtract()
    print "juppi!"
    check_multi()
    print "jiha"
    check_div()
    print "jauza"

