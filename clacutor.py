# Create the  30/10/2021 ; update the 1/11/2021 by Benjamin Descours
def addition():
    num_1 = input("a number ")
    num_2 = input("a number ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    result = num_1 + num_2
    print("The result of {} + {} = {}".format(num_1, num_2, result))


def subtraction():
    num_1 = input("a number ")
    num_2 = input("a number ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    result = num_1 - num_2
    print("The result of {} - {} = {}".format(num_1, num_2, result))


def muiltiplication():
    num_1 = input("a number ")
    num_2 = input("a number ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    result = num_1 * num_2
    print("The result of {} * {} = {}".format(num_1, num_2, result))


def divison():
    num_1 = input("a number ")
    num_2 = input("a number ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    result1 = num_1 / num_2
    result2 = num_1 % num_2
    print("The result of {} / {} = {}".format(num_1, num_2, result1))
    print("The remains for Euclidean divison is : {} .".format(result2))


def calc():
    print("Welcome to PyCalc_terminal")
    vla_1 = input("1. + ; 2. - ; 3. * ; 4. / ")
    vla_1 = int(vla_1)
    if vla_1 == 1:
        addition()
    elif vla_1 == 2:
        subtraction()
    elif vla_1 == 3:
        muiltiplication()
    elif vla_1 == 4:
        divison()
    elif vla_1 != 1 or 2 or 3 or 4:
        print("Restart")
        return calc()
    vla_2 = input("\nA new calculation for that choose a number please (y or n) ")
    vla_3 = "y"
    if vla_2 == vla_3:
        return calc()
    elif vla_2 != vla_3:
        print("\nbye\n")


calc()
