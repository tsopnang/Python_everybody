#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email = list()
greatest_email = ""
count_email = 0
count = 0
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    #print(words[1])
    email.append(words[1])
    count += 1
for ls in email:
    if(email.count(ls) > count_email):
        greatest_email = ls
        count_email = email.count(ls)
print(ls, count_email)

#print("There were", count, "lines in the file with From as the first word")
