from abc import abstractproperty
import pyperclip
import re

#copy
# hi here is ssn 777-23-4214 and cc is 5122-4212-4214-4214 more 433-23-4333

text = pyperclip.paste()
print(text)
print()

ssRegex = re.compile(r'''(
    (\d{3})
    (-|\s)
    (\d{2})
    (-|\s)
    (\d{4})

)''', re.VERBOSE)

ccRegex = re.compile(r'''(
    (\d{4})
    (-|\s)
    (\d{4})
    (-|\s)
    (\d{4})
    (-|\s)
    (\d{4})

)''', re.VERBOSE)

x = re.sub(ssRegex,"********",text)
y = re.sub(ccRegex,"******************",x)
pyperclip.copy(y)
print(pyperclip.paste())

