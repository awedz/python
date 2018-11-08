# a list => multi the numbers
# a = [str(int(currID[x-1]) * 1) if x % 2 != 0 else str(int(currID[x-1])* 2) for x in range(1, len(currID)+1)]
# b list=> if bigger then 9 add the numbers
# b = [int(x) if int(x) < 10 else int(x[0]) + int(x[1]) for x in a]
# c int value => sum() the list
# c = sum(b)
# retun true or false for sum %10 ==0
# return c % 10 == 0


def Validate_id(ID):
    return sum([int(x) if int(x) < 10 else int(x[0]) + int(x[1]) for x in [str(int(ID[x-1]) * 1) if x % 2 != 0 else str(int(ID[x-1]) * 2) for x in range(1, len(ID)+1)]]) % 10 == 0


def TakeInput():
    userInput = input("enter ID number")
    if len(userInput) < 9:
        userInput.zfill(9)
    elif len(userInput) > 9:
        return "ID length too long"
    else:
        if Validate_id(userInput):
            return "ID is valid"
        else:
            return "ID is not valid"


print(TakeInput())
