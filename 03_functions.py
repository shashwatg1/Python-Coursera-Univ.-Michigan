''' Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value '''

def computepay(h,r):
    if h>40:
        return 40*r + (h-40)*r*1.5
    else:
        return h*r

try:
    h = float(raw_input("Enter Hours:"))
    r = float(raw_input("Enter Rate:"))
    print computepay(h,r)
except:
    print "Error"