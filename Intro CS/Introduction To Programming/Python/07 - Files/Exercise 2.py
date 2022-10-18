file = input("Enter file name: ")
try:
    fileHandler = open(file)
except:
    print("Cannot find a file with the name", file)

for line in fileHandler:
    if (line.startswith("X-DSPAM-Confidence")):
        firstIndex = line.find(": ");
        print(line[firstIndex+2:])
