# In this project will be making bug collector using for loops
# 10/17/19
# CTI-110 P4T2 - Bug Collector
# Sebastian Johnson 
#


#initialize the accumulator
total = 0


# Get the bugs collected for each day.

for day in range(1, 8):
    # Prompt the user.
    print ('Enter the amount of bugs collected on day', day)


    #input number of bugs.
    bugs = int(input())


    # Add bugs to total
    total += bugs


# Display the total bugs.
print('You collected a total of', total,'bugs.')
