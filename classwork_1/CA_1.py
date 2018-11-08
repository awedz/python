userInput = input("put number")
match = 0
i = 0
while i < len(userInput):
    if userInput[i] == userInput[len(userInput)-i-1]:
        match += 1
    i += 1
print("yes") if match == len(userInput) else print("no")
