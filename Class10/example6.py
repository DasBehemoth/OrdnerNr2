import random # = ordner der in python gespeichert ist

if __name__ == '__main__':
    numbers = range(20)
    print numbers
    random.shuffle(numbers)
    print numbers
