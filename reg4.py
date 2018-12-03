import re
match=re.search('^\w*end','Hey! What are your plans for the weekend?') #check whether is is in the starting of a strimg 
print(match.group())

#it gives error as output,This is because we specified that this pattern should be at the beginning of the string. 
