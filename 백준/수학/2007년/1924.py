import sys

month, days = map(int, sys.stdin.readline().split())


def findDay(month, days):

    one = [1, 3, 5, 7, 8, 10, 12]
    zero = [4, 6, 9, 11]
    days_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    tot_days = 0
    for i in range(1,12):
        if i == month:
            break

        if i == 2:
            tot_days += 28

        elif i in zero:
            tot_days += 30

        elif i in one:
            tot_days += 31


    tot_days += days
    remain =  tot_days % 7 
    print(days_list[remain])
    
    
        
findDay(month,days)