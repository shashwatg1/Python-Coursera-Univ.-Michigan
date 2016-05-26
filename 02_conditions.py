''' Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.  '''

try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter rate:")
    r = float(rate)
    if h<=40:
        print h*r
    else:
        print (40*r + (h-40)*r*1.5)
except:
    print "error"




''' Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. '''

score = raw_input("Enter Score: ")
try:
    s = float(score)
    if s<0.0:
        print "error"
    elif s>1.0:
    	print "error"
    elif s>= 0.9:
        print "A"
    elif s>= 0.8:
        print "B"
    elif s>= 0.7:
        print "C"
    elif s>= 0.6:
        print "D"
    else:
        print "F"
except:
    print("Error")