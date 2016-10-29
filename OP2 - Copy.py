#ok so orgo is way to fucking big and my computer is way to fucking slow
#this program will open the "clean" and then chop it up into carriers
#this is now OP 2

import csv

def memory_check (made_it):

    """Here is the filter to organize everything by memory, so split into 3 new lists"""

    print()
    print()
    print("checking memory")
    print()
    print()

    gb16_list = []
    gb32_list =[]
    gb64_list = []
    memory_16_words = ["16gb"]
    memory_32_words = ["32gb"]
    memory_64_words = ["64gb"]
    

    for row in made_it:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)      
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")")
            if clean in memory_32_words:
                gb32_list.append(row)

    for row in made_it:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")").strip("*")
            if clean in memory_64_words:
                gb64_list.append(row)

    for row in made_it:
        if row not in gb32_list:
            if row not in gb64_list:
                gb16_list.append(row)
            

    print(len(gb16_list),"16gb iphones")
    #print(gb16_list)
    print()
    print(len(gb32_list),"32gb iphones")
    #print(gb32_list)
    print()
    print(len(gb64_list),"64gb iphones")
    #print(gb64_list)

    #I wonder if this could be skipped below, make this whole program faster,
    #so instead pass the GB lists and write files.
    with open("year_w16gb.csv", "w", newline= '', encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(gb16_list)
        f.close()
    with open("year_w32gb.csv", "w", newline= '', encoding="UTF-8") as h:
        writer = csv.writer(h)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(gb32_list)
        h.close()
    with open("year_w64gb.csv", "w", newline= '', encoding="UTF-8") as u:
        writer = csv.writer(u)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(gb64_list)
        u.close()

    att_filter(gb16_list,gb32_list,gb64_list)


def att_filter(gb16_list,gb32_list,gb64_list):

    """chopping up the GB lists to grab only the AT&T listings"""

    print()
    print("att check")

    ATT = ["at&t", "att"]

    att_gb16 = []
    att_gb32 = []
    att_gb64 = []

    mega = [att_gb16,att_gb32,att_gb64]
    stock = [gb16_list,gb32_list,gb64_list]

    #filter by the carrier + GB

    for row in gb16_list:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)      
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
            if clean in ATT:
                att_gb16.append(row)
                
    for row in gb32_list:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)      
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
            if clean in ATT:
                att_gb32.append(row)
                
    for row in gb64_list:
        title = str(row[0])
        n_title = title.split()
        #print(n_title)      
        for word in n_title:
            #print(word)
            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
            if clean in ATT:
                att_gb64.append(row)
                
    print("done with at&t")
    #print(att_gb16)
    #print(len(att_gb16))
    print()
    
    with open("year_15_att16gb.csv", "w", newline= '', encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(att_gb16)
        f.close()
    with open("year_15_att32gb.csv", "w", newline= '', encoding="UTF-8") as h:
        writer = csv.writer(h)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(att_gb32)
        h.close()
    with open("year_15_att64gb.csv", "w", newline= '', encoding="UTF-8") as u:
        writer = csv.writer(u)
        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
        writer.writerows(att_gb64)
        u.close()

##
##    verizon_filter(gb16_list,gb32_list,gb64_list)
##
##def verizon_filter(gb16_list,gb32_list,gb64_list):
##
##    """same as the function above, this time only filter out Verizon"""
##
##    print()
##    print("verizon check")
##
##    Verizon = ["verizon"]
##
##    ver_gb16 = []
##    ver_gb32 = []
##    ver_gb64 = []
##
##    #filter by the carrier + GB
##
##    for row in gb16_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in Verizon:
##                ver_gb16.append(row)
##                
##    for row in gb32_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in Verizon:
##                ver_gb32.append(row)
##                
##    for row in gb64_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in Verizon:
##                ver_gb64.append(row)
##                
##    print("done with verizon")
##    print()
##    
##    with open("year_ver16gb.csv", "w", newline= '', encoding="UTF-8") as f:
##        writer = csv.writer(f)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(ver_gb16)
##        f.close()
##    with open("year_ver32gb.csv", "w", newline= '', encoding="UTF-8") as h:
##        writer = csv.writer(h)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(ver_gb32)
##        h.close()
##    with open("year_ver64gb.csv", "w", newline= '', encoding="UTF-8") as u:
##        writer = csv.writer(u)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(ver_gb64)
##        u.close()
##
##    sprint_filter(gb16_list,gb32_list,gb64_list)
##
##
##def sprint_filter(gb16_list,gb32_list,gb64_list):
##
##    """same shit, this time Sprint"""
##
##    print()
##    print("sprint check")
##
##    sprint = ["sprint"]
##
##    
##    spr_gb16 = []
##    spr_gb32 = []
##    spr_gb64 = []
##
##    #filter by the carrier + GB
##
##    for row in gb16_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in sprint:
##                spr_gb16.append(row)
##                
##    for row in gb32_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in sprint:
##                spr_gb32.append(row)
##                
##    for row in gb64_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in sprint:
##                spr_gb64.append(row)
##                
##    print("done with sprint")
##    print()
##    
##    with open("year_spr16gb.csv", "w", newline= '', encoding="UTF-8") as f:
##        writer = csv.writer(f)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(spr_gb16)
##        f.close()
##    with open("year_spr32gb.csv", "w", newline= '', encoding="UTF-8") as h:
##        writer = csv.writer(h)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(spr_gb32)
##        h.close()
##    with open("year_spr64gb.csv", "w", newline= '', encoding="UTF-8") as u:
##        writer = csv.writer(u)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(spr_gb64)
##        u.close()
##
##    T_Mobile_filter(gb16_list,gb32_list,gb64_list)
##
##def T_Mobile_filter(gb16_list,gb32_list,gb64_list):
##
##    """you get the picture by now"""
##    
##    print()
##    print("t-mobile check")
##
##    T_Mobile = ["t-Mobile", "t", "mobile", "t-mobile"]
##    
##    tmo_gb16 = []
##    tmo_gb32 = []
##    tmo_gb64 = []
##
##
##    #filter by the carrier + GB
##
##    for row in gb16_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in T_Mobile:
##                tmo_gb16.append(row)
##                
##    for row in gb32_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in T_Mobile:
##                tmo_gb32.append(row)
##                
##    for row in gb64_list:
##        title = str(row[0])
##        n_title = title.split()
##        #print(n_title)      
##        for word in n_title:
##            #print(word)
##            clean = word.lower().strip("(").strip(")").strip("*").strip(";")
##            if clean in T_Mobile:
##                tmo_gb64.append(row)
##                
##    print("done with t-mobile")
##    print()
##    
##    with open("year_tmo16gb.csv", "w", newline= '', encoding="UTF-8") as f:
##        writer = csv.writer(f)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(tmo_gb16)
##        f.close()
##    with open("year_tmo32gb.csv", "w", newline= '', encoding="UTF-8") as h:
##        writer = csv.writer(h)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(tmo_gb32)
##        h.close()
##    with open("year_tmo64gb.csv", "w", newline= '', encoding="UTF-8") as u:
##        writer = csv.writer(u)
##        writer.writerow(["Listing title", "Price Sold", "Date Sold"])
##        writer.writerows(tmo_gb64)
##        u.close()
##
##    #The statement below is not true when the OP file is > 3MB...
##    print("IT MADE IT; DIDN'T CRASH")
##    quit


            
def main ():
    
    made_it = []

    with open("year_15_clean.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        
        #make the list of ALL the rows
        for row in reader:
            made_it.append(row)

    memory_check(made_it)

main()
        
