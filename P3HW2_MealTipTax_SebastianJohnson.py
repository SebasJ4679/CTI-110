
# In this program i will be building upon P2HW1_MealTipTax
#From the original I will be adding in new functions by using boolean logic
# 10/02
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Sebastian Johnson
# 1. Prompt user to enter the charge for food
# 2. Prompt user to enter the tip for server ( remember this is a percentage , the input therefore should be decimal. For example,  for a 15% tip, 0.15 should be entered)
# 3. If the user enters a tip rate other than those listed display an error and have the user enter a recommended rate
# 3. Since the tax is a fixed variable display what the tax will be on the meal
# 4. Write a function to calculate tip and tax
# 5. Display the following:
   #*Calculated tip
   #*Calculated tax
   #*Display total cost of meal ( food charge + tip+ tax)
   #*Original food charge




tip1 = .16
tip2 = .18
tip3 = .20
tax = 0.06

food_charge = float(input('Please enter the charge for your food: '))
tip = float(input('Please enter a recommended percentage to tip in decimal form (.16, .18, or .20) : '))
if tip == tip1:
    print('The original food charge is $', format(food_charge,',.2f'),".",sep='')
    print('The total tax on your meal will be $' ,format(food_charge * tax,',.2f'),".",sep='')
    print('The original tip of 16% will be $', format(food_charge * tip1,',.2f'),".",sep='')
elif tip == tip2:
        print('the original food charge is $', format(food_charge,',.2f'),".",sep='')
        print('The total tax on your meal will be $' ,format(food_charge * tax,',.2f'),".",sep='')
        print('The original tip of 18% will be $', format(food_charge * tip1,',.2f'),".",sep='')
elif tip == tip3:
    print('The original food charge is $', format(food_charge,',.2f'),".",sep='')
    print('The total tax on your meal will be $' ,format(food_charge * tax,',.2f'),".",sep='')
    print('The original tip of 20% will be $', format(food_charge * tip1,',.2f'),".",sep='')
else:
    reEnter = input(float =('!ERROR! please close the program and enter a recommended tip: ')) 



tax = 0.06
calculatedTip1 = (food_charge * tip1)
calculatedTip2 = (food_charge * tip2)
calculatedTip3 = (food_charge * tip3)
calculatedTax = (food_charge * tax)
total_cost1 =(food_charge + calculatedTip1 + calculatedTax)
total_cost2 =(food_charge + calculatedTip2 + calculatedTax)
total_cost3 =(food_charge + calculatedTip3 + calculatedTax)
if tip == tip1:
    print('The total cost of your meal is $', format(total_cost1,',.2f'),".",sep='')
elif tip == tip2:
    print('The total cost of your meal is $', format(total_cost2,',.2f'),".",sep='')
elif tip == tip3:
    print('The total cost of your meal is $', format(total_cost3,',.2f'),".",sep='')
    





