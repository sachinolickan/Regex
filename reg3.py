import re
match=re.search('\w*end','Hey! What are your plans for the weekend?') #searching for weekend in string
print(match.group())
