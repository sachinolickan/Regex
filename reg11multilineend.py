import re
match=re.findall(r'[\w]$','sachin\nGokul\nAnju',re.MULTILINE)
for i in match:
    print(i)
