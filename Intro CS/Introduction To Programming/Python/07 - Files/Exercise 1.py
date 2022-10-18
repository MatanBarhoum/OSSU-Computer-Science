file = input("Enter file name: ")
try:
    fileHandle = open(file)
except:
    print("File cannot be opened: ", file)
    exit()

count = 0
for line in fileHandle:
    print(line.upper())
    count += 1
print("Lines in file: ", count)
