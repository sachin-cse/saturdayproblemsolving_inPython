def check_leapYear(n):
    if(n%4 == 0 and n%100 != 0) or (n%400 == 0):
        return "true"
    else:
        return "false"
    
year  = int(input("enter your year"))

print(check_leapYear(year))