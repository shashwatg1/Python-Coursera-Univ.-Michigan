''' Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case '''

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:    
    fh = open(fname)
    str = fh.read()
    print str.upper().strip()
except:
    print "error"




''' Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output '''

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
    exit()
count=0
s=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ext=line[(line.find(':')+1):]
    try:
        n=float(ext)
        s+=n
        count+=1
    except:
        print("skipped")
print "Average spam confidence:",(s/count)
