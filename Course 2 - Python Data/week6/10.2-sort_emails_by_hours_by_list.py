#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

previous = None
hours = list()
hours_dict = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    #print(words[5].split(":")[0])
    hour = words[5].split(":")[0]
    hours.append(hour)
hours.sort()
#print(hours)
for hour in hours:
    hours_dict[hour] = hours_dict.get(hour, 0) + 1
    #print(previous, hour, (previous == hours))
    if previous is None or previous != hour:
        previous = hour
        print(hour, hours.count(hour))

#print(hours_dict)
#for key,value in hours_dict.items():
    #print(key, value)
