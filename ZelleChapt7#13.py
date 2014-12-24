#ZelleChapt7#12ValidDate_plus_Day_Number.py
# A program to take a date and determine whether or not it is valid,
# and then calculate the day number. 

def zero_evaluator(nn):
    if nn[0] == "0":
        new_number = nn[1]
    else:
        new_number = nn
    print(new_number)  
    return new_number

def Leap_year(x):
    year = x
    yeardiv4 = year%4
    yeardiv100 = year%100
    yeardiv400 = year%400
    if yeardiv100 == 0:
        if yeardiv400 == 0:
            return "yes"
        elif yeardiv400 != 0:
            return "no"
    elif yeardiv4 == 0:
        return "yes"
    else:
        return "no"

def Valid(month, day, year):  
    if year >=1 and year <=2100:
        print("Yowza!")
        if month >=1 and month <=12:
            if month == 2:
                if Leap_year(year) == "yes":
                    print("This is a Leap Year!")
                    if day >=1 and day <= 29:
                        return "The date is valid."
                    else:
                        return "The date is not valid."
                else:
                    print("This is not a Leap Year!")
                    if day >=1 and day <=28:
                        return "The date is valid."
                    else:
                        return "The date is not valid."                   
            elif month == 9 or 4 or 6 or 11:
                if day >=1 and day <=30:
                    return "The date is valid."
                else: 
                    return "The date is not valid."
            else:
                if day >=1 and day <=31:
                    return "The date is valid."
                else: 
                    return "The date is not valid."
        else:
            return "The date is not valid."
    else:
        return "The date is not valid."

       
def main():
    date = input("Please enter the date in the form 'nn/nn/nnnn':")
    try:
        date_info = date.split("/")
        month = int(zero_evaluator(date_info[0]))
        day = int(zero_evaluator(date_info[1]))
        year = int(date_info[2])
        print(month, day, year)
        dayNum1 = 31*(month - 1) + day
    
        if Valid(month, day, year) == "The date is valid.":
            print("The date is valid.")
            if month < 3:
                print("The day number is", dayNum1)  
            else:
                dayNum2 = dayNum1 - ((4 * month + 23)//10)
                if Leap_year(year) == "yes":
                    print("The day number is:", dayNum2 + 1)
                else: 
                    print("The day number is:", dayNum2)        
        else:
            print("The date is not valid. No day calculation possible!")
    except ValueError:
        print("Try again. You must use slashes to separate your numbers.")
    
main()
