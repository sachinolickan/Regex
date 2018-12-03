import re
match=re.findall(r'.*','Hi, did you ship it, Hillary?\nNo, I did, but Hi')
for i in match:
    print(i)
