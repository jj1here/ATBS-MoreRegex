import pyperclip
import re

#copies

#https://www.google.com and or asf as http://www.nesin.net nice coolasf www.hi.plac asf fsaf.oin3is.as miaosf saf websie3.mc The brown count ran. lost dogs died.

text = str(pyperclip.paste())
print(text)
print()

webRegex = re.compile(r'''(
    (http(s)?://)?
    ([www.]|(\w+\.))?
    [a-zA-z0-9._%+-]+
    (\.\w{2,4})
)''', re.VERBOSE)

found = []
for groups in webRegex.findall(text) :
    found.append(groups[0])
    
if len(found) > 0 :
    pyperclip.copy("\n".join(found))
    print(pyperclip.paste())
else:
    print("No websites found")





