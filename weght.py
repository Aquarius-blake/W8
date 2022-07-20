


def action():
    weight= float(input("Enter Weight in grams: "))
    ton=int(10**6)
    kilo=int(10**3)
    choice=int(input('''Choose your country
    1.Ghana
    2.United Kingdom
    3.United States
    4.Mexico
    '''))

    if choice==1 or choice==2:
        result=(weight/kilo)
        
        return print("Weight is " + str(result) +" kilograms")
    elif choice==3 or choice==4:
        result=(weight/ton)
        return print("Weight is "+ str(result) + " tonnes")
    else :
        return print("Invalid response")


action()    


#Pseudocode
#Recieve weight input in grams from user
#Declare neccessary variables
#Recieve Country of interest input from user
#if choice=1 or 2 then divide weight input by 10^3
#and print result in kilograms
#else divide weight input by 10^6
#and print result in tonnes 
