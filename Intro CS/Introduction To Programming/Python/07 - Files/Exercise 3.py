file = input("Enter file name: ")
if (file == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been pink'd!")
    quit()
try:
    fileHandler = open(file)
    for line in fileHandler:
        if (line.startswith("X-DSPAM-Confidence")):
            firstIndex = line.find(": ");
            print(line[firstIndex+2:])
except:
    print("Cannot find a file with the name", file)
