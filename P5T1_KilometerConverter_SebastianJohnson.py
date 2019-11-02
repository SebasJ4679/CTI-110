# Todday i will create a program that converts kilometers to miles
# 10/27/19
# CTI-110 P5T1_KilometerConverter
# Sebastian Johnson 
#


#Pseudocode
#1. Prompt the user to enter a distance in kilometers
#2. display the formula so the user knows what calculation is about to occur
#3 write a function that carries out the formula
#4. display the end result to the user


def main():
    kilometers= float(input('Enter the kilometers you would like converted to miles: '))
    print('The formula being used is miles = kilometers * 0.6214.')
    miles = (kilometers) * 0.6214
    print('The conversion of', kilometers,'kilometers','to miles is', miles)

main()

