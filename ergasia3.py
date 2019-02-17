fin=open("test.py","r")
lines=fin.readlines()
fin.close()
for line in lines:
        if "#" in line:  
                l=line.strip()        
                if l[0]!="#":
                        newline = line.split("#")
                        a1=newline[0].count("'")
                        a2=newline[0].count('"')
                        if (a1%2)==1 or a2%2==1:
                        	print line
                        else:
                                print line.split("#")[0]
        else:
                print line 



