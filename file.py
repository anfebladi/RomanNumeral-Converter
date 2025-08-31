
number = str(input("what number do you want to convert?").lower())
def number_generator(number):
    new_num = 0
    if "cm" in number:
        new_num += 900
        number = number.replace("cm", "")
    if "cd" in number:
        new_num += 400
        number = number.replace("cd", "")
    if "xc" in number:
        new_num += 90
        number = number.replace("xc", "")
    if "xl" in number:
        new_num += 40
        number = number.replace("xl" , "")
    if "ix" in number:
        new_num += 9
        number = number.replace("ix", "")
    if "iv" in  number:
        new_num += 4
        number = number.replace("iv", "")
    for num in number:
        if num == "i":
            new_num += 1
        elif num == "v":
            new_num += 5
        elif num == "x":
            new_num +=10
        elif num == "l":
            new_num +=50
        elif num== "c":
            new_num += 100
        elif num == "d":
            new_num += 500
        elif num == "m":
            new_num += 1000
    print("Your roman number is equal to " + str(new_num))

number_generator(number)