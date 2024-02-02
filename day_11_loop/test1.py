#WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate
#for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.


hour = float(input("enter the number "))
rate = float(input("enter the rate"))
if hour <= 40:
    pay = (hours*10.5)
    print(pay)
else:
    pay = (40*rate)
    ove = (hours-40)*1.5*rate
    total_pay = pay + ove
    print(total_pay)
