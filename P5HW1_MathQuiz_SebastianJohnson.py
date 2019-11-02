# Today i will be creating a math quiz that will prompt the user to enter the sum or the remainder of two numbers
# 10/28/19
# CTI-110 P5HW1 - Random Number
# Sebastian Johnson
#




#Pseudocode
 #1. Dispplay the menu to the user
 #2. create a function that will carry out the program
 #3. add a while loop so that the program can continue running
 #4. Prompt the user to enter a choice they would like to proceed with
 #5. Create a function that will execute if option 1 is chosen
 #6. Create a function that will execute if option 2 is chosen
 #7. if option 3 is selected end the program
 #8. if the user gets the answer right congraulate them



import random
import P5HW1_Menu
print()
print()
print()
def main():
    name = input('Greetings, welcome to the Math Quiz. What is your name?: ')
    print('Hello', name)
    keep_going = 'y'
    while keep_going =='y':

        choose = int(input('Enter 1, 2, or 3 to continue: '))
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        sum =(value1 + value2)
        remainder =(value1 - value2)

        if choose == 1:
             print(value1)
             print(value2)
             answer1 = int(input('What is the sum of the values displayed?: '))
             if answer1 == sum:
                 print('Congratulations', name,' that is correct')
                 playAgain = input('Would you like to play again? (y/n): ')
                 keep_going ='j'
                 while keep_going =='j':
                     if playAgain == 'y':
                         value1 = random.randint(1, 100)
                         value2 = random.randint(1, 100)
                         print(value1)
                         print(value2)
                         answer1 = int(input('What is the sum of the values displayed?: '))
                     if  answer1 == sum:
                         print('Congratulations', name, ' that is correct')
                     else:
                         print('Exiting program...')
                 keep_going = input('Press any key to exit')









                 else:
                     print('Exiting program...')


             else:
                 print(name,'that is incorrect')
                 input('Press any key to restart: ')

        elif choose == 2:
            print(value1)
            print(value2)
            answer2 = int(input('What is the remaider of the values displayed?: '))
            if answer2 == remainder:
                print('Congratulations', name, ' that is correct')
            else:
                print(name, 'that is incorrect')

        elif choose == 3:
            print('Exiting program...')

        else:
            print('Please enter one of the choices listed')
            input('Press any key to restart: ')
        keep_going = input('Press any key to exit: ')




















main()














