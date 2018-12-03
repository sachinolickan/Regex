import re
import os
os.chdir('F:\python programs\Regular expression') #finding text word in a file
f=open('new.txt')
match=re.findall('java[\w]*',f.read())
for i in match:
    print(i)
