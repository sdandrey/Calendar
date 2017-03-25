weekdays = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4,
            "Friday":5, "Saturday":6}
anchorDay = [5,3,2,0]
mdoom = [ 3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12 ]


def getAnchorDay(year):
    return anchorDay[((year + 200)%400)//100]

def doomsDay(day, month, year):
    yy = (year%100)//12
    diference = (year%100)%12
    ydiference = diference//4
    anchorDay = getAnchorDay(year)
    return (anchorDay + ydiference + diference + yy)%7

def doomsMonth(day, month, year):
    dommsDay = doomsDay(day, month, year)
    if( (month == 1 or month == 2) and isLeap(year)):
        l = 1
    else:
        l = 0
    return mdoom[month - 1] - l

def getDay(day, month, year):
    dayI = doomsDay(day, month, year)
    monthI = doomsMonth(day, month, year)
    if(day<monthI):
            while(monthI!=day):
                monthI = monthI-1
                dayI = dayI - 1
                
            if(dayI<0):
                dayI = 7 - (dayI*-1) % 7
    else:
        while(monthI!=day):
            monthI = monthI+1
            dayI = dayI + 1
        if(dayI>6):
            dayI = dayI%7
        
    return dayI;

def isLeap(a):
    if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
        return True
    return False
