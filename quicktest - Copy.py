##p = "Apple iPhone 5s - 16GB - Silver (AT&T;) Liquid Damaged for Parts/Repair"
##
##words = p.split()
##
##for wrd in words:
##    wrd.split('/')
##    check = wrd.lower()
##    clean = check.lower().strip("(").strip("<").strip(">").strip(")").strip("*").strip("!").strip("-").strip(";").strip(".").strip("*").strip(",").strip("[").strip("]").strip("/")
##    print(clean)


#smoothes the numbers and brings everything down by 3%
import math
import itertools
import operator

adj = [(500,488),(500,488),(500,488),(500,488),(450,449.99),(420,412.5),(410,410),(409.99,400),(409.99,399.99),(399.99,205),(500,488),(450,449.99),(420,412.5),(410,410),(409.99,400),(409.99,399.99),(500,488),(450,449.99),(420,412.5),(410,410),(409.99,400),(409.99,399.99),(160,150)]

neww = map(operator.itemgetter(1), adj)
print(neww)

number_list = []
for item in adj:
    number_list.append(item[1])
print(number_list)
print()

fixed = []
weekly = []
x = 1
for i in number_list:
    weekly.append(i)
    if len(weekly) >= 7:
        wek_avg = float(sum(weekly)/7)
        tup = (wek_avg,x)
        fixed.append(tup)
        x +=1
        weekly = []
    else:
        continue

print(fixed)
    
##    weekly.append(i)
##    if len(weekly) > 7:
##        wek_avg = sum(weekly)
##        tup = (wek_avg,x)
##        fixed.append(tup)
##        x += 1
##        weekly = []
##    else:
##        continue
##print(fixed)
    


     

##print(k, sum(list(v)), give)









###do it by percentage and then compare the output to group
##from itertools import groupby
##
##litt = [21, 26, 29, 100, 102, 105, 109, 134, 139]
##
####new_l = []
####    
####for k, v in itertools.groupby(litt, key=lambda n: n//10):
####  
####    
####    print (k, sum(list(v)), )
####print()
####print("daily average is:",int(sum(new_l)/len(new_l)),"and the other is:",int(sum(litt)/len(litt)) )
##groups = []
##uniquekeys = []
##data = sorted(litt, key=keyfunc)
##for k, g in groupby(data, keyfunc):
##    groups.append(list(g))      # Store group iterator as a list
##    uniquekeys.append(k)
##    print(uniquekeys)
##        
        



