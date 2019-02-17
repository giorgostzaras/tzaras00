#sto keimeno exw upothesei oti to min kai to max einai ena gramma . se diaforetikh periptwsh min h max tithetai to gramma pou emfanizetai prwto.

import string
import re
x = raw_input("give me the name of the file  ")
with open("%s.txt" %x, 'r') as f:
    mytext = f.read().replace('\n', '')
    letters = mytext.replace(" " , "")
letters2 = re.sub(r'[^\w\s]','',letters)   
maxletter = max(letters2, key=letters.count)
minletter = min(letters2, key=letters.count)
print "the most popular letter is:", maxletter
print   "the less popular letter is:" , minletter

for a in (("%s" %minletter, "%s" %maxletter.upper()), ("%s" %maxletter, "%s" %minletter.upper())):
    mytext = mytext.replace(*a)
print mytext


    
