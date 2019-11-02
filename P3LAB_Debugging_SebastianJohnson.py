# CTI-110 
# P3LAB - Debugging 
# Sebastian Johnson 
# 10/02/2019



#Pseudocode 
# 1.Re-type the code from web programming and databases page. 123 into python
# 2.Next define your variables to make things easier on yourself
# 3.Run the program to see where the first error will show then work from there
# 4.Align if/else statements correctly so you dont get any "syntax errors" or "Unexpected indentation"
# 5.Notice that after the first if/else statement the I in the next "if" lines up with the colon on the first "else:"
# 6.Correct indentation so that if lines up with the colon on the "else:" above it
# 7.Backspace until the print is on the same line as the "if" and hit enter it should align itself. if not press tab until the p in "print" is lined up with the c in "score"
# 8.Line the e in "else:" up with the p in "print"
# 9.Repeat lines 4-8 until no more errors are found

score = 0
A_score = 90
B_score =80
C_score = 70
D_score = 60
F_score = 50


score = int(input('Enter the numerical value of your score: '))
if score >= A_score:
    print('Your grade is a A.')
else:

    if score >= B_score:
        print('Your grade is a B.')
    else:
        

        if score >= C_score:
            print('Your grade is a C.')
        else:

            if score >= D_score:
                print('Your grade is a D.')
            else:
                print('Ypur grade is F.') 

