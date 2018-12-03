import re
match=re.findall(r'^hi','hi sachin\nGokul hi\nhi Anju',re.MULTILINE)
for i in match:
    print(i)
