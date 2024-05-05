fileName = 'mySoulIsDark.txt'
with open(fileName, mode='r') as fileData:
    for line in fileData:
        print(line, end='')

