import re
match=re.findall(r'advi[cs]e','I could advise you on your poem, but you would disparage my advice')
for i in match:
    print(i)
