####################################################################################################################################################################################################################################################################
#  Computer Project #3
#
#  Algorithm
#    starting a while loop(which stays True until it breaks only when the choice is anyting other "y" or "Y")
#       printing the welcome banner
#       prompt for location_place(string input)
#       prompt for maximum square footage(string input)
#       prompt for maximum monthly pay(string input)
#       prompt for down payment(string input)
#       prompt for current APR(string input)
#       conditional statement(1) for the value of down payment
#           if NA, then it's value is equal to 0
#
#       conditional statement(2) to check for an instance where both maximum square footage amd maximum monthly payment are equal to NA
#           if it becomes True, then the program would print a message for not enough information
#
#       conditional statement(3) to check if the inputted location_place is not equal any of the 4 cities that we have specified
#           if True, display unknown location_place message
#
#           conditional statement to check maximum sqaure footage is equal to NA(under unknown location_place)
#               one more conditional statement to check if apr is NA
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement
#
#           conditional statement to check maximum monthly payment is equal to NA(under unknown location_place)
#               calculating cost_amt and principle_amt
#               one more conditional statement to check if apr is NA         
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement
#
#           else statement for the case where the location_place is unknown(this is already under this condition but both maximum monthly payment and maximum square footage is given)
#               calculating cost_amt and principle_amt  
#               one more conditional statement to check if apr is NA     
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement
#
#       conditional statement to check if maximum square footage is NA(Now as we move through the program from top to bottom, we have already filtered out whether both max_sqft and max_monpay are NA or location_place is NA so this implies that location_place and max_monpay is known)
#           using a mixture of for loop and enumerate function to find out the location_place 
#               one more conditional statement to check if apr is NA
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement
#
#       conditional statement to check if maximum monthly payment is NA(Now as we move through the program from top to bottom, we have already filtered out whether both max_sqft and max_monpay are NA or location_place is NA so this implies that location_place and max_sqft is known)
#           using a mixture of for loop and enumerate function to find out the location_place 
#               one more conditional statement to check if apr is NA
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement   
#      
#       conditional statement to check if both maximum monthly payment and maximum square footage are not NA(so location_place is also known as explained previously)
#           using a mixture of for loop and enumerate function to find out the location_place 
#           calculating cost_amt, principle_amt and tax_amt
#               one more conditional statement to check if apr is NA
#                  if True, the program uses 6.68% as apr(APR_2023) and print the statement; else the given value and print the statement
#
#       conditional statement to ask the users to print the ammortization table only in the cases where maximum square footage is given(a flag variable is being used to keep a track of that)
#           prompt for "y" or "Y" for a yes to print the table; else will not print the table 
#           a combination of string formatting, conditional statements and for loop is used to successfully print the ammortization table
#
#       prompt for the user if the person wants to calculate another morgage payment
#       conditional statement to check if True or not; of not, the loop breaks
####################################################################################################################################################################################################################################################################


NUMBER_OF_PAYMENTS = 360                    #Symbolic constant: 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092          #Symbolic constant: Seattle property tax rate
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074    #Symbolic constant: San Francisco property tax rate
AUSTIN_PROPERTY_TAX_RATE = 0.0181           #Symbolic constant: Austin property tax rate
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162     #Symbolic constant: East Lansing tax rate
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011  #Symbolic constant: Average national property tax rate
SEATTLE_PRICE_PER_SQ_FOOT = 499.0           #Symbolic constant: Seattle price per sq foot
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0    #Symbolic constant: San Francisco price per sq foot
AUSTIN_PRICE_PER_SQ_FOOT = 349.0            #Symbolic constant: Austin price per sq foot
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0      #Symbolic constant: East Lansing price per foot
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0  #Symbolic constant: Average national price per sq foot
APR_2023 = 0.0668                           #Symbolic constant: Annual Percentage Rate of 2023
I_2023=APR_2023/12                          #Symbolic constant: Interest rate per month
while True:
    max_monpay=max_sqft=principle_amt=principal=balance_amt=cost_amt=\
        tax_amt=apr=down_pay=location_place=cal_maxmp=total_amt=None        #Setting all the variables equal to None just to make sure that they don't have old values       
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")  #printing banner  
    print("\nEnter a value for each of the following items or \
type 'NA' if unknown ")                                                       
    location_place=input("\nWhere is the house you are considering \
(Seattle, San Francisco, Austin, East Lansing)? ")              #asking for inputs
    max_sqft=input("\nWhat is the maximum square footage you \
are considering? ")
    max_monpay=input("\nWhat is the maximum monthly payment you can afford? ")
    down_pay=input("\nHow much money can you put down as a down payment? ")
    apr=input("\nWhat is the current annual percentage rate? ")
    flag=0        #Now this acts like a counter in my program which is to make sure that the table gets printed only when max sq ft is given by the user 
    if down_pay=="NA":     #this is just to set down_pay equal to zero whrn the input is NA
        down_pay=0
    if max_sqft=="NA" and max_monpay=="NA":  #an if statement to check when noth max monthly pay and max square footage are NA
        print("\nYou must either supply a desired square footage or a \
maximum monthly payment. Please try again.") #you display this message when the above condition is satisfied
    elif location_place!="Seattle" and location_place!="San Francisco" and \
        location_place!="Austin" and location_place!="East Lansing":  #when inputted location is unknown
        print("\nUnknown location. Using national averages for price \
per square foot and tax rate.")           #printing unknown loc message and giving the user the disclaimer
        if max_sqft=="NA":                #an if condition to check when inputted max sq footage is NA and location is unknown
            if apr=="NA":                 #if inputted apr is NA under these conditions, we go into this
                principle_amt=(float(max_monpay)*(((1+I_2023)**\
                                                   NUMBER_OF_PAYMENTS)-1))\
                    /(I_2023*((1+I_2023)**NUMBER_OF_PAYMENTS)) #calculating principle amount
                cost_amt=principle_amt+float(down_pay)         #calculating cost
                max_sqft=cost_amt/AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT     #calculating max sq footage
                print("\n\nIn the average U.S. housing market, a maximum \
monthly payment of ${:.2f} allows the purchase of a house of {} sq. feet for \
${}\n\t assuming a 30-year fixed rate mortgage with a ${} down payment at \
6.7% APR.".format(float(max_monpay),int(round(float(max_sqft))\
    ),int(round(float(cost_amt)\
    )),int(down_pay)))              #printing the final statement
            else:
                principle_amt=(float(max_monpay)*(((1+(float(apr)/1200)\
)**NUMBER_OF_PAYMENTS)-1))/((float(apr)/1200)*((1+(float(apr)/1200)\
                                    )**NUMBER_OF_PAYMENTS))
                cost_amt=principle_amt+float(down_pay)    #if apr is not NA under these conditions, we go into this
                max_sqft=cost_amt/AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT  #calculating max sq footage
                print("\n\nIn the average U.S. housing market, a maximum \
monthly payment of ${:.2f} allows the purchase of a house of {} sq. feet for \
${}\n\t assuming a 30-year fixed rate mortgage with a ${} down payment at \
{:.1f}% APR.".format(float(max_monpay),int(round(float(max_sqft))\
    ),int(round(float\
    (cost_amt))),int(down_pay),float(apr)))     #printing the final statement
        elif max_monpay=="NA":           #if max monthly pay is NA (given already that location is unknown)
            flag=1                       #the counter which I was talking about before  
            cost_amt=AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT*float(max_sqft)    #calculating cost
            principle_amt=cost_amt-float(down_pay)          #calculating principle
            if apr=="NA":                #if apr is NA under the above conditions,we go into this
                max_monpay=(principle_amt*((I_2023*((1+I_2023)**\
                NUMBER_OF_PAYMENTS))))/(((1+I_2023)**NUMBER_OF_PAYMENTS)-1) #calculating max monthly payment
                tax_amt=cost_amt*AVERAGE_NATIONAL_PROPERTY_TAX_RATE/12    #calculating taxes
                total_amt=max_monpay+tax_amt        #calculating total amount to pay
                print("\n\nIn the average U.S. housing market, an average \
{} sq. foot house would cost ${}.".format(int(round(float(max_sqft))),int(\
    round(float(cost_amt)))))                       #printing final statements
                print("A 30-year fixed rate mortgage with a down payment of \
${} at 6.7% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) \
+ ${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),tax_amt,\
    max_monpay,total_amt))                          #printing final statements
            else:                                   #if apr is not NA
                max_monpay=(principle_amt*(((float(apr)/1200)*(\
                                        (1+(float(apr)/1200)\
    )**NUMBER_OF_PAYMENTS))))/(((1+(float(apr)/1200))**NUMBER_OF_PAYMENTS)-1)  #calculating monthly payment
                tax_amt=cost_amt*AVERAGE_NATIONAL_PROPERTY_TAX_RATE/12    #calculating tax amount
                total_amt=max_monpay+tax_amt         #calculating total amount to pay
                print("\n\nIn the average U.S. housing market, an average {} \
sq. foot house would cost ${}.".format(int(round(float(max_sqft))),int(round(\
    float(cost_amt)))))                               #printing final statements
                print("A 30-year fixed rate mortgage with a down payment of \
${} at {:.1f}% APR results\n\tin an expected monthly payment of ${:.2f} \
(taxes) + ${:.2f} (mortgage payment) = ${:.2f}".format(int\
    (down_pay),float(apr),\
    tax_amt,max_monpay,total_amt))             #printing final statements
        else:                              #if both max monthly payment and max sq footage is given(but location is unknown), we go into this    
            flag=1                         #counter (for the table)
            cost_amt=AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT*float(max_sqft)     #calculating cost
            principle_amt=cost_amt-float(down_pay)                  #calculating principle
            if apr=="NA":                  # if apr is NA under the above conditions
                cal_maxmp=(principle_amt*((I_2023*((1+I_2023)**\
                NUMBER_OF_PAYMENTS))))/(((1+I_2023)**NUMBER_OF_PAYMENTS)-1)    #calculating max monthly payment
                tax_amt=cost_amt*AVERAGE_NATIONAL_PROPERTY_TAX_RATE/12     #calculating taxes
                total_amt=cal_maxmp+tax_amt       #calculating taxes
                print("\n\nIn the average U.S. housing market, an average {} \
sq. foot house would cost ${}.".format(int(round(float(max_sqft))),int(round(\
    float(cost_amt)))))            #printing final statments
                print("A 30-year fixed rate mortgage with a down payment of \
${} at 6.7% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) \
+ ${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),tax_amt,\
    cal_maxmp,total_amt))          #printing final statements 
            else:                  #if apr is not NA we go into this
                cal_maxmp=(principle_amt*(((float(apr)/1200)*(\
                                (1+(float(apr)/1200)\
    )**NUMBER_OF_PAYMENTS))))/(((1+(float(apr)/1200))**NUMBER_OF_PAYMENTS)-1)   #calculating max monthly payment
                tax_amt=cost_amt*AVERAGE_NATIONAL_PROPERTY_TAX_RATE/12   #calculating tax amount
                total_amt=cal_maxmp+tax_amt           #calculating total amount to pay per month
                print("\n\nIn the average U.S. housing market, an average \
{} sq. foot house would cost ${}.".format(int(round(float(max_sqft))),int(\
    round(float(cost_amt)))))      #printing final statements
                print("A 30-year fixed rate mortgage with a down payment of \
${} at {:.1f}% APR results\n\tin an expected monthly payment of ${:.2f} \
(taxes) + ${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay)\
    ,float(apr),tax_amt,cal_maxmp,total_amt))  #printing final statements
            if float(max_monpay)>=total_amt:   #a special case when both max sq footage and max monthly pament are given, we can compare the givan and the computed values to check whether the person can actually afford or not
                print("Based on your maximum monthly payment of ${:.2f} \
you can afford this house.".format(float(max_monpay)))  
            else:
                print("Based on your maximum monthly payment of ${:.2f} you \
cannot afford this house.".format(float(max_monpay)))   
    elif max_sqft=="NA":      #now if the location is known but max sq footage is unknown we come to this
        if apr=="NA":         #if apr is NA we go into this
            principle_amt=(float(max_monpay)*((\
                                (1+I_2023)**NUMBER_OF_PAYMENTS)-1)\
                       )/(I_2023*((1+I_2023)**NUMBER_OF_PAYMENTS)) #calculating principle amount
            cost_amt=principle_amt+float(down_pay)  #calculating cost
            if location_place=="Seattle":           #finding out the location(max sq ft as per location)
                max_sqft=cost_amt/SEATTLE_PRICE_PER_SQ_FOOT
            elif location_place=="San Francisco":
                max_sqft=cost_amt/SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            elif location_place=="Austin":
                max_sqft=cost_amt/AUSTIN_PRICE_PER_SQ_FOOT
            elif location_place=="East Lansing":
                max_sqft=cost_amt/EAST_LANSING_PRICE_PER_SQ_FOOT
            print("\n\nIn {0}, a maximum monthly payment of ${1:.2f} allows \
the purchase of a house of {2} sq. feet for ${3}\n\t assuming a 30-year \
fixed rate mortgage with a ${4} down payment at 6.7% APR.".format(\
    location_place,\
    float(max_monpay),int(round(float(max_sqft))),int(round(float(cost_amt)\
                                            )),int(down_pay))) #printing final print statements
        else:               #if apr is not NA, we go into this
            principle_amt=(float(max_monpay)*(((1+(float(apr)/1200)\
)**NUMBER_OF_PAYMENTS)-1))/((float(apr)/1200)*((1+(float(apr)/1200)\
                                    )**NUMBER_OF_PAYMENTS))      #calculating principle amount
            cost_amt=principle_amt+float(down_pay)        #calculating cost
            if location_place=="Seattle":                 #finding location(max sq ft as per location)
                max_sqft=cost_amt/SEATTLE_PRICE_PER_SQ_FOOT
            elif location_place=="San Francisco":
                max_sqft=cost_amt/SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            elif location_place=="Austin":
                max_sqft=cost_amt/AUSTIN_PRICE_PER_SQ_FOOT
            elif location_place=="East Lansing":
                max_sqft=cost_amt/EAST_LANSING_PRICE_PER_SQ_FOOT
            print("\n\nIn {0}, a maximum monthly payment of ${1:.2f} allows \
the purchase of a house of {2} sq. feet for ${3}\n\t assuming a 30-year \
fixed rate mortgage with a ${4} down payment at {5:.1f}% APR.".format(\
 location_place,float(max_monpay),int(round(float(max_sqft))\
                                    ),int(round(float(cost_amt))\
                                ),int(down_pay),float(apr))) #printing final print statements
    elif max_monpay=="NA":               #if location is known but max monthly payment is NA
        flag=1                           #counter.....
        if location_place=="Seattle":    #finding out the location(cost and tax as per the location)
            cost_amt=SEATTLE_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*SEATTLE_PROPERTY_TAX_RATE/12
        elif location_place=="San Francisco":
            cost_amt=SAN_FRANCISCO_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*SAN_FRANCISCO_PROPERTY_TAX_RATE/12
        elif location_place=="Austin":
            cost_amt=AUSTIN_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*AUSTIN_PROPERTY_TAX_RATE/12
        elif location_place=="East Lansing":
            cost_amt=EAST_LANSING_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*EAST_LANSING_PROPERTY_TAX_RATE/12
        principle_amt=cost_amt-float(down_pay)
        if apr=="NA":                   #if apr is NA under the above conditions
            max_monpay=(principle_amt*((I_2023*((1+I_2023)**\
                NUMBER_OF_PAYMENTS))))/(((1+I_2023)**NUMBER_OF_PAYMENTS)-1)   #finding max monthly payment
            total_amt=max_monpay+tax_amt           #finding out total amount to pay per month
            print("\n\nIn {}, an average {} sq. foot house would cost \
${}.".format(location_place,int(round(float(max_sqft))\
    ),int(round(float(cost_amt)))))                #printing final print statements
            print("A 30-year fixed rate mortgage with a down payment of ${} \
at 6.7% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) + \
${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),\
    tax_amt,max_monpay,total_amt))                 #printing final print statements
        else:                            #if apr is not NA under the above conditions, we go into this
            max_monpay=(principle_amt*(((float(apr)/1200)*(\
(1+(float(apr)/1200))**NUMBER_OF_PAYMENTS))))/((\
                        (1+(float(apr)/1200))**NUMBER_OF_PAYMENTS)-1)     #calculating max monthly payment
            total_amt=max_monpay+tax_amt         #calculating total money to pay per month
            print("\n\nIn {}, an average {} sq. foot house would cost \
${}.".format(location_place,int(round(float(max_sqft))\
    ),int(round(float(cost_amt)))))              #printing final print statements
            print("A 30-year fixed rate mortgage with a down payment of ${} \
at {:.1f}% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) \
+ ${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),float(apr)\
    ,tax_amt,max_monpay,total_amt))              #printing final print statements
    elif max_monpay!="NA" and max_sqft!="NA":    #if location, max sq ft, max monthly payment are all known, we go into this  
        flag=1                                   #counter.....
        if location_place=="Seattle":            #finding out location(cost, tax as per location)
            cost_amt=SEATTLE_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*SEATTLE_PROPERTY_TAX_RATE/12
        elif location_place=="San Francisco":
            cost_amt=SAN_FRANCISCO_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*SAN_FRANCISCO_PROPERTY_TAX_RATE/12
        elif location_place=="Austin":
            cost_amt=AUSTIN_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*AUSTIN_PROPERTY_TAX_RATE/12
        elif location_place=="East Lansing":
            cost_amt=EAST_LANSING_PRICE_PER_SQ_FOOT*float(max_sqft)
            tax_amt=cost_amt*EAST_LANSING_PROPERTY_TAX_RATE/12
        principle_amt=cost_amt-float(down_pay)  #calculating principle
        if apr=="NA":                           # if apr is NA under these conditions 
            cal_maxmp=(principle_amt*((I_2023*((1+I_2023)**NUMBER_OF_PAYMENTS)\
                                  )))/(((1+I_2023)**NUMBER_OF_PAYMENTS)-1)   #calculating max monthly payment
            total_amt=cal_maxmp+tax_amt         #calculating total amount to pay per month
            print("\n\nIn {}, an average {} sq. foot house would cost \
${}.".format(location_place,int(round(float(max_sqft))\
    ),int(round(float(cost_amt)))))             #printing final print statements
            print("A 30-year fixed rate mortgage with a down payment of ${} \
at 6.7% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) + \
${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),tax_amt,\
    cal_maxmp,total_amt))                       #printing final print statements
        else:                                   #now if apr is not NA under these conditions, we go into this
            cal_maxmp=(principle_amt*(((float(apr)/1200)*((1+(float(apr)/1200)\
    )**NUMBER_OF_PAYMENTS))))/(((1+(float(apr)/1200))**NUMBER_OF_PAYMENTS)-1)  #calculating max monthly payment
            total_amt=cal_maxmp+tax_amt         #calculating total payment per month
            print("\n\nIn {}, an average {} sq. foot house would cost \
${}.".format(location_place,int(round(float(max_sqft))\
    ),int(round(float(cost_amt)))))             #printing final print statements
            print("A 30-year fixed rate mortgage with a down payment of ${} \
at {:.1f}% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) \
+ ${:.2f} (mortgage payment) = ${:.2f}".format(int(down_pay),float(apr),\
    tax_amt,cal_maxmp,total_amt))               #printing final print statements
        if float(max_monpay)>=total_amt:        #a special case when both max sq footage and max monthly pament are given, we can compare the givan and the computed values to check whether the person can actually afford or not
            print("Based on your maximum monthly payment of ${:.2f} you can \
afford this house.".format(float(max_monpay)))
        else:
            print("Based on your maximum monthly payment of ${:.2f} you \
cannot afford this house.".format(float(max_monpay)))   
    if flag==1:                                #now here we use the counter to ask the user for a monthly schedule only if flag is 1
        table=input("\nWould you like to print the monthly payment \
schedule (Y or N)? ")                          #prompt user for input  
        if table.lower()=="y":                 #if True(yes), we go into this  
            print()
            print("{:^7}|{:^12}|{:^13}|{:^14}".format("Month","Interest",\
                                                      "Principal","Balance"))  #printing table header using string formatting
            print("{}".format("="*48))         #printing table header decoration(continued)
            if apr=="NA":                      #the case where apr is NA, we take apr 2023 value  
                apr=6.68
            if cal_maxmp==None:                #now the case where cal_maxmp variable not used condition works, we assign this value
                cal_maxmp=float(max_monpay)
            else:
                pass
            for n in range(1,361):             #for loop is being employed
                month_no=n                     #month number
                interest_amt=(principle_amt*(float(apr)/100))/12  #calculating interest
                principal=cal_maxmp-interest_amt    #calculating principal
                balance_amt=principle_amt           #calculating balance loan amount
                principle_amt-=principal            #updating value
                print("{:^7}| ${:>9.2f} | ${:>10.2f} | ${:>11.2f}".format(\
                            month_no,interest_amt,principal,balance_amt))      #printing values using string formatting
    choice_again=input("\nWould you like to make another attempt (Y or N)? ")  #prompt user if the person wants to use tha mortage calculator again 
    if choice_again.lower()!="y":
        break          #if not true, the loop breaks