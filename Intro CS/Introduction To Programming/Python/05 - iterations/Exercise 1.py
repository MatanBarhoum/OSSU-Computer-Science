is_not_done = True
while is_not_done:
  try:
    userInput = input("Enter a number: ").lower()
    if (userInput == "done"):
      is_not_done = False
    else:
      float(userInput)
  except:
    print("invalid input")
