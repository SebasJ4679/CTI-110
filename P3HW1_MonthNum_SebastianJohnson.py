# In this program i will be asking the user to enter a months number and based upon that number i will provide the month that corresponds with the number.
# CTI-110
# P3HW1 - Month number
# Sebastian Johnson
# 10/02/2019


#Pseudocode
#1.Assign variables(numbers to months)
#2.Prompt the user to enter a months number 1 - 12
#3.Display the the month name with the corresponding number
#start creating if/else statements that contain the variables set and print functions that will display the month name
#4.If the number that the user enters is outside of the range display an error and prompt them to close the program and try again
#5.Display the month

month1 = 1
month2 = 2
month3 = 3
month4 = 4
month5 = 5
month6 = 6
month7 = 7
month8 = 8
month9 = 9
month10 = 10
month11 = 11
month12 = 12


monthNumber = int(input('Enter the number of the month you would like to be displayed(1-12): '))
if monthNumber == 1:
    print('The first month of the year is January',".",sep='')
elif monthNumber == 2:
    print('The second month of the year is Febuary',".",sep='')
elif monthNumber == 3:
    print('The third month of the year is March',".",sep='')
elif monthNumber == 4:
    print('The fourth month of the year is April',".",sep='')
elif monthNumber == 5:
    print('The fifth month of the year is May',".",sep='')
elif monthNumber == 6:
    print('The sixth month of the year is June',".",sep='')
elif monthNumber == 7:
    print('The seventh month of the year is July',".",sep='')
elif monthNumber == 8:
    print('The eighth month of the year is August',".",sep='')
elif monthNumber == 9:
    print('The ninth month of the year is September',".",sep='')
elif monthNumber == 10:
    print('The tenth month of the year is October',".",sep='')
elif monthNumber == 11:
    print('The elventh month of the year is November',".",sep='')
elif monthNumber == 12:
    print('The twelth month of the year is December',".",sep='')
else:
    print('!ERROR! please restart this program and enter a correct input (1-12)',".",sep='')
