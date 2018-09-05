#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_117330.txt (There are 70 values and the sum ends with 126)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

print("\n\n\n\n It is a pleasure for me to take this course !!!\n\n")
#text = open('regex_sum_42.txt') #Opening sample data file
text = open('regex_sum_117330.txt') #Opening Actual data file

sum_numbers = 0 #Initialyzing sum_numbers variable to 0
for line in text: #Loop to read a line in the file
    #print(line)
    numbers_in_line = re.findall('[0-9]+', line) #Reading numbers in the line
    #print(number)
    for number in numbers_in_line: #Loop to read number on by one in numbers list
        sum_numbers += int(number) #Adding the current number to the sum_numbers
print(sum_numbers) #Printing the final sum result
