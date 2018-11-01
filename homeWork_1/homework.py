numbers = ["zero", "one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine"]

numInput = int(input("select num\n"))
if numInput < 9:
    print(numbers[numInput])
elif numInput > 9 and numInput < 99:
    sum = (int(numInput % 10)) + (int(numInput / 10))
    print("number has two digits and the sum is :%s" % sum)
elif numInput > 90 and numInput < 990:
    sum = (int(numInput % 10)) * (int(numInput / 10) %
                                  10) * (int(numInput / 100))
    print("number has three digits and the sum is :%s" % sum)
else:
    print("number is too fucking big for my 2 bit processor")
