html_str  =raw_input("give me the title of the page without the html_tag in the end \n")
f=open("%s.html" %(html_str),"r")
sum1 = 0
sum2 = 0
brsum = 0
psum = 0
asum = 0
lines=f.readlines()
for line in lines:
    print line.split(" ")
    br_tag = line.count("br>")
    p_tag = line.count("<p>")
    a_tag = line.count("<a")
    brsum = br_tag + brsum
    psum = psum + p_tag
    asum = asum + a_tag
    
total = brsum + psum + asum         
print( "<br> = %d  <p> = %d  <a> = %d  total = %d ")  %(brsum,psum,asum,total)