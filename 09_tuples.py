'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. '''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "Error"
    exit()
count = dict()
for line in handle:
    line = line.rstrip()
    if line == "" : continue
    words = line.split()
    if len(words)==0 : continue
    if words[0] != "From" : continue
    time = (words[5].split(':'))[0]
    count[time] = count.get(time,0) + 1

lst = list()

for key,value in count.items() :
	lst.append((key,value))
lst.sort()

for hr,value in lst:
    print hr, value