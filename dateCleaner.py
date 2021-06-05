import pyperclip
import re

#copy
# (such as 3/14/2019, 03-14-2019, and 2015/3/19)

text = pyperclip.paste()
print(text)
print()

dateRegex = re.compile(r'''(
    (\d{1,4}) #years or days or months
    (/|-)
    (\d{1,2}) #days or months
    (/|-)
    (\d{1,4}) #days or years

)''', re.VERBOSE)

# print(dateRegex.findall(text))

found = []

for groups in dateRegex.findall(text) :
    if len(groups[1]) == 4 :
        found.append(groups[0])
    elif len(groups[5]) == 4 :
        found.append("".join([groups[5],groups[4],groups[3],groups[2],groups[1]]))

if len(found) >0 :
    pyperclip.copy("\n".join(found))
else :
    print("No dates found.")