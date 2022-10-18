str = 'X-DSPAM-Confidence:0.8475'

first = str.find('0')
last = str.find("5")
floatedNumber = float(str[first:last+1])
print(type(floatedNumber))
print(floatedNumber)