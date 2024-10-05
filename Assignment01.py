
## Assignment01.py
## Author: [Mehran Khodabakhshi]
## Submission Date: [09-15-2024]
##
## Purpose:
## first part of assignment is focused on create variables of: hoursPerWeek,grossPay, federalTax , stateTax, medicare, socialSecurity
## define a fuction weeklyNetPay to calculate weekly net pay,
## finally using string formatting syntax to print the results.

## In part two the goal is define a function MonthlyNetPay to get the input of 5 tweets,
## extract certain part of the tweet string usinh string methods such as .find
## and print monthly financial situation such as loan, expense,budget,income,... .
##
## Statement of Academic Honesty:

## The following code represents my own work. I have neither
## received nor given inappropriate assistance. I have not copied
## or modified code from any source other than the course webpage
## or the course textbook. I recognize that any unauthorized
## assistance or plagiarism will be handled in accordance with
## the Georgia State University's Academic Honesty Policy and the
## policies of this course. I recognize that my work is based
## on an assignment created by the Institute for Insight at the
## Georgia State University. Any publishing
## or posting of source code for this project is strictly
## prohibited unless you have written consent from the Institute
## for Insight at the Georgia State University.






#Defined variables that are in capital hold fixed values:
FEDERAL_TAX_PERCENT=10
STATE_TAX_PERCENT=4.5
SS_PERCENT=6.2
MEDICARE_PERCENT=1.45
PAY_PER_HOUR=7.25

# def function to cal weekly  net pay 
def weeklyNetPay():
    pass

# fist part hoursPerWeek holds a fixed amount of 40 hrs
hoursPerWeek=40

# gross income
grossPay=(hoursPerWeek*PAY_PER_HOUR)

# Deductions 
federalTax=(grossPay*FEDERAL_TAX_PERCENT)/100
stateTax=(grossPay*STATE_TAX_PERCENT)/100
medicare=(grossPay*MEDICARE_PERCENT)/100
socialSecurity=(grossPay*SS_PERCENT)/100

# hers is the net pay from substracting all deductions from gross pay
weeklyNetPay = (grossPay - federalTax - stateTax - medicare - socialSecurity)

# printing the outcome of deductions 
print(f"Hours per Week:\t\t40\nGross Pay:\t\t{grossPay:.2f}\nWeekly Net Pay:\t\t{weeklyNetPay:.2f}")
print("\nDeductions")
print("Federal:               %.2f" % (federalTax))
print("State:                 %.2f" % (stateTax))
print("Social Security:       %.2f" % (socialSecurity))
print("Medicare:              %.2f" % (medicare))


# now the function asks user to input number of working hours in aweek
def WeeklyNetPay():
    
    #hours input as integer
    hoursPerWeek=int(input("Please input hourly worked hours:\t"))
    grossPay=(hoursPerWeek*PAY_PER_HOUR)
    federalTax=(grossPay*FEDERAL_TAX_PERCENT)/100
    stateTax=(grossPay*STATE_TAX_PERCENT)/100
    medicare=(grossPay*MEDICARE_PERCENT)/100
    socialSecurity=(grossPay*SS_PERCENT)/100
    weeklyNetPay=(grossPay-federalTax-stateTax-medicare-socialSecurity)
    
    print(f"Hours per Week:\t\t{hoursPerWeek}\nGross Pay:\t\t{grossPay:.2f}\nWeekly Net Pay:\t\t{weeklyNetPay:.2f}")
    print("\nDeductions")
    print("Federal:               %.2f" % (federalTax))
    print("State:                 %.2f" % (stateTax))
    print("Social Security:       %.2f" % (socialSecurity))
    print("Medicare:              %.2f" % (medicare))

    #the output of function is returned
    return weeklyNetPay

#call defined function
weeklyNetPay_final = WeeklyNetPay()



#################################### PART TWO ########################################




tweet=""

# Defining function for monthly payment as a function of weekly pay
def MonthlyNetPay(weeklyNetPay):

    
    tweets = []

    
    # Use a loop to read 5 tweets as input one by one
    for i in range(1,6):
        user_input = input(f"please input tweets ONE BY ONE \t Tweet {i}: ")
        tweets.append(user_input)

    

    # here is the month payment calculation
    monthlyNetPay=weeklyNetPay*4
    
    #initial values later will be added to
    incoming = 0
    outgoing = 0
    incoming_type=[]
    outgoing_type=[]
    
    
    # define a for loop to itrate every single tweet one by one
    for tweet in tweets:
        
        
        # how to find start,end,semiclon index and extract type
        starting_type=tweet.find("#typ")
        ending_type=starting_type+len("#typ")
        semi_index=tweet.find(";")
        type_var=(tweet[ending_type:semi_index].strip()).upper()
        
        

        # how to find start,end,semiclon index and extract detail
        starting_det=tweet.find("#det")
        ending_det=starting_det+len("#det")
        second_semi_index=tweet.find(";",semi_index + 1 )
        detail_var=tweet[ending_det:second_semi_index].strip()
        
        ## how to find start,end,semiclon index and extract location
        starting_loc=tweet.find("#loc")
        ending_loc=starting_loc+len("#loc")
        third_semi_index=tweet.find(";",second_semi_index+1 )
        location_var=tweet[ending_loc:third_semi_index].strip()
       

        # how to find start,end,semiclon index and extract currency
        starting_cur=tweet.find("#cur")
        ending_cur=starting_cur+len("#cur")
        fourth_semi_index=tweet.find(";",third_semi_index+1 )
        currency_var=tweet[ending_cur:fourth_semi_index].strip()
        

        # how to find start,end,semiclon index and extract amount
        starting_amt=tweet.find("#amt")
        ending_amt=starting_amt+len("#amt")
        fifth_semi_index=tweet.find(";",fourth_semi_index+1 )
        amount_var_str=tweet[ending_amt:fifth_semi_index].strip()
        amount_var = float(amount_var_str.replace(",", ""))
        
        
        
        # how to undrestand type of transaction and append details
        if type_var in ["INVESTMENT"]:
             incoming += amount_var
             incoming_type.append("%s , %s "%(type_var,detail_var))
     
        elif type_var in ["INCOME"]:
             incoming += amount_var
             incoming_type.append("%s , %s "%(type_var,detail_var))
        elif  type_var in ["LOAN","SAVINGS","EXPENSE"]:
             outgoing += amount_var
             outgoing_type.append("%s , %s "%(type_var,detail_var))
    
    # total budget calculation
    totalBudget = incoming + monthlyNetPay - outgoing     
    print("Weekly Net Pay:     %.3f" %(weeklyNetPay))
    print("Monthly Net Pay:    %.3f"%(monthlyNetPay))
    print("Incoming Types:     %s" % (", ".join(incoming_type)))
    print("Incoming Amount     %.3f" %(incoming))
    print("Outgoing Types:     %s" % (", ".join(outgoing_type)))
    print("Outgoing Amount     %.3f" %(outgoing))
    print("Total Budget:       %.3f" %( totalBudget))

# recalling function
MonthlyNetPay(weeklyNetPay_final)


        


        

