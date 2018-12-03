import re
match=re.findall(r'aleena','hi Aleena,are aLeeNa hI,AlEEnA',re.IGNORECASE)
for i in match:
    print(i)
