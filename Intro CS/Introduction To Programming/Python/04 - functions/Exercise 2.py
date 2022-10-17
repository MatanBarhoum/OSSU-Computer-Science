def GetScore(score):
    try:
        if (score <= 0 or score > 1.0):
            print("Bad score")
        elif (score < 0.6):
            print("F")
        elif (score >= 0.6 and score < 0.7):
            print("D")
        elif (score >= 0.7 and score < 0.8):
            print("C")
        elif (score >= 0.8 and score < 0.9):
            print("B")
        else:
            print("A")
    except:
        print("Bad score")

GetScore(1.1)
