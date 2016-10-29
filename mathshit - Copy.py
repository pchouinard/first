#!/usr/bin/python
#MATH SHIT

#figure out the dayily, weekly, and monthly average
#then apply this to the year long data

#do this for fucking errthing and see if makes any sort of difference: att vs. errthing

#LOOK THIS STUFF OVER; NOT GOOD ENOUGH

import csv
import operator
whole_list = []
fixed = []




def open_start(whole_list):

    mean_list = []
    d_store = []
    day = 1
    month = 1

    with open("year_15_att16gb.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        print("started")

        for row in reader:
            #print(row)
            whole_list.append(row)

    dating(whole_list, d_store, day, month)
    

def dating(whole_list, d_store, day, month):
    
    daily = []
    cnt =0 
    date_thing = str(month)+"/"+str(day)+"/2015"
    
    for row in whole_list:
        check = str(row[2])
        if check == date_thing:
            print("woerk")
            daily.append(float(row[1]))
            cnt += 1
    print(daily)
                      
    if cnt == 0:
        print("0 sold day")
        update_day(whole_list,d_store, day,month)

 
    else:
        #math to find mean on the date
        daily_avg = (sum(daily))/cnt
        tup = (date_thing,daily_avg)

        #need more math to find Volume Weighted Moving Average
##        VWMA = [Sum for Length, from a specific day of PV ()] / [Sum for Length, from a specific day of V ()]
##        P(n) = Price at day n
##        V(n) = Volume at day n
##        PV(n) = P(n) x V(n)
        #this won't work
        #going to have to make something propriety to get a general PV(n)..or do something else

        
        print(tup)
        d_store.append(tup)
        fixed.append(daily_avg)
       
        update_day(whole_list,d_store,day,month)
        


def update_day(whole_list, d_store, day, month):

    if day < 32:
        day +=1
        dating(whole_list, d_store, day, month)
    else:
        update_month(whole_list, d_store, day, month)
        

def update_month(whole_list, d_store, day, month):

    month += 1
    
    if month < 13:
        day = 1
        dating(whole_list, d_store, day, month)
    if month == 13:
        match_up(d_store)
    else:
        match_up(d_store)
        
        
def match_up(d_store):
    
    neww = map(operator.itemgetter(1), d_store)
    all_day = []
    for item in d_store:
        all_day.append(item[1])

    fixed = []
    w_store = []
    x = 1
    for i in all_day:
        weekly.append(i)
        if len(weekly) >= 7:
            wek_avg = float(sum(weekly)/7)
            tup = (wek_avg,x)
            w_store.append(tup)
            x +=1
            weekly = []
        else:
            continue

    #print(fixed)
    
    print()
    print()
    #print(d_store)
    #choose if you want daily averages or weekly
    #or make two files
    #d_store = daily averages
    #fixed = weekly averages
    
    with open("W_2015_iphone5s_att16_avg.csv", "w", newline= '', encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date Sold","Average Sold Price(daily)"])
        writer.writerows(w_store)
        f.close
    quit
    

def main():
    open_start(whole_list)

main()
