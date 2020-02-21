import datetime

def Zellers_congruence(day,month,year):
    q=day #date
    if month==1 or month==2:
        if month==1: #january
            m=13 
        else:               #february
            m=14
        k=(year-1)%100  #year-1
        j=(year-1)//100
    else:
        m=month #month
        k=year%100 #last 2 digit of year
        j=year//100 #first 2 digit of year
    h=(q+13*(m+1)//5+k+k//4+j//4-2*j)%7 #formula
    return h


def date():
    error=True
    while error == True:
        date=input("Enter date (dd-mm-yyyy):").split("-")
        try:
            datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
            error=False

        except:
            print("invalid date...")
            print("Please enter a valid date.")
            print()

    return date
        
print("                 Zeller’s Congruence | Find the Day for a Date")

code={0:"Saturday",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday"}

date=date()

d,m,y=int(date[0]),int(date[1]),int(date[2])

weekday=code[Zellers_congruence(d,m,y)]
print("It's >>",weekday)
