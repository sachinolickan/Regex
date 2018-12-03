import re
match=re.findall(r'([\w]+)\s([\w]+)','Sarath Joy,Gokul av,Fathima Fahida, time to go bed')
for i in match:
    print(i)
