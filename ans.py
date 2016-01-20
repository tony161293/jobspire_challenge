from random import randint


# funtion for doing the work
def naming(name):
    r = randint(6, 15)  # random integer generation
    print name + " " + str(r)  # printing name and integer
