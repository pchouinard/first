#this program will open the OP and then chop it up into the "clean" and "dirty"
#this is now OP 1

whole_list = []
shit_list = []
import csv


##    print("started")
##    print()

#these are the words that are used to filter out "bad" condition listings.
#they go in their own list
#might remove the words: excellent, mint
shit_words = ["damage","bad","error","liquid","part","parts","problem","problems","crack","cracks","wont",
              "wont't","only","water","repair","waterdamage","damaged","power","unknown","as","see","water",
              "parts","blacklisted","unlocked","broken","dead","issue","issues","poor", "factory", "bad",
              "defective", "cracked", "lot", "iPod","locked","lock","restore","perfect","read","break",
              "logic","stuck","excellent","restore","motherboard","mint","read","flawless","care","beat", "4",
              "4s","bent","activation","disabled","icloud"]
x = 0
y = 0
z =0

with open("Y_2015_iphone5s.csv", "r", encoding="UTF-8") as f:
    reader = csv.reader(f)
    
    #make the list of ALL the rows
    for row in reader:
        whole_list.append(row)
        x+=1
        #print(row)

    #make a list of shit rows from rows in the whole_list   
    for row in whole_list:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")").strip("*").strip("!").strip("-").strip(";").strip(".").strip("*").strip(",").strip("[").strip("]").strip("/").strip("~")
            if clean in shit_words:
                shit_list.append(row)
                y+=1
                

    #get rid of dups....i still don't know why there are doubles
    #anything that is "shit" gets duplicated and I don't know y
    dup_shit = []
    for row in shit_list:
        if row not in dup_shit:
            dup_shit.append(row)
            #y+=1

    #make list of rows that are clean!
    #these are rows not in the shit list,
    #so they are clean
    made_it = []
    for row in whole_list:
        if row not in dup_shit:
            made_it.append(row)
            z+=1

print(x, "rows total")
print()
print("clean list")
#print(z, "rows that are clean")
print()
#print(made_it)
print()
#ha, this crashed the computer
##    for row in made_it:
##        print(row)
##    print()  
##    print()
print()
print("shit list")
#print(y, "rows that are shit")
print()
#print(dup_shit)
#print(dup_shit)
print()

with open("year_15_clean.csv", "w", newline= '', encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Listing title", "Price Sold", "Date Sold"])
    writer.writerows(made_it)
    f.close()
with open("year_15_dirty.csv", "w", newline= '', encoding="UTF-8") as h:
    writer = csv.writer(h)
    writer.writerow(["Listing title", "Price Sold", "Date Sold"])
    writer.writerows(dup_shit)
    h.close()


print("yay it worked")
quit
