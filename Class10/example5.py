
def square_numbers(x): # mit den drei anfuehrungszeichen kann man definition dazu machen, wird dann angezeigt, stichwoerter muessen so sein
    """
    :param x: number to square
    :type x: int
    :return:
    :rtype: int or float
    """
    return x**2

def cube_numbers(x):
    return x**3

def check_square_numbers():
    assert square_numbers(9) == 81
    assert square_numbers(-3) == 9

def check_cube_numbers():
    assert cube_numbers(3) == 27


if __name__ == '__main__': # fixer startpunkt ab hier werden funktionen ausgefuehrt
    check_square_numbers()
    print "affirmative"
    check_square_numbers()
    print "okidoki"