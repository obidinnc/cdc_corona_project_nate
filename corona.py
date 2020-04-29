#All of the data we're using to detemrine the risk of severe illness come from the CDC.
#You can find it here at this website: https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/people-at-higher-risk.html

#First, we'll determine the age of the user.
age = input("enter your age.")
age = int(age)
if age > 65:
    print("You are at high risk for covid-19. Please take the necessary precautions to protect yourself.")

else:
    print("Thank you. Let's continue.")

#Once that is complete, we can get to the nitty gritty. We'll calculate the household size, and how many people leave the house on a daily basis. 
fno = input("How many people are in your household?")
fno = int(fno)

leave = input("How many people leave the house on a daily basis?")
leave = int(leave)

#Once that is complete, we can calculate how many people practice proper hygiene. 
hygiene = input("How many people practice proper hygine ettiquite in your home?")
hygiene = int(hygiene)

#The wash variable will serve in our mission later. An arbitrary number, but practical.
wash =  hygiene / fno * 100 
print(wash)
    
#Now we work on the CDC junk, starting from the top.
print("Now we'll ask some health questions.")
#We'll perform some loops, starting with the first question. 
print("Do you have chronic lung disease or moderate to severe asthma?")
 
answer = None
health1 = 0
while answer != 'yes' or answer != 'no':
    answer = input("Please enter yes or no: ")

    if answer == "yes":
        h1r = health1 + 1
        print("Thank you. Let's continue.")
        break
    elif answer == "no":
        h1r = health1 + 0
        print("Thank you. Let's continue.")
        break

    else:
        print("Seems we didn't get that.")

#And we'll continue the process, just as we had before.
print("Next. Do you have a serious heart condition/heart conditions?")
answer2 = None
while answer2 != 'yes' or answer2 != 'no':
    answer2 = input("Please enter yes or no: ")

    if answer2 == "yes":
        h2r = h1r + 1
        print("Thank you. Let's continue.")
        break
    elif answer2 == "no":
        h2r = h1r + 0
        print("Thank you. Let's continue.")
        break

    else:
        print("Seems we didn't get that.")

print("Are you immunocompromised in any way?")
answer3 = None
while answer3 != 'yes' or answer3 != 'no':
    answer3 = input("Please enter yes or no: ")

    if answer3 == "yes":
        h3r = h2r + 1
        print("Thank you. Let's continue.")
        break
    elif answer3 == "no":
        h3r = h2r + 0
        print("Thank you. Let's continue.")
        break

    else:
        print("Seems we didn't get that.")
        
#Now, we'll break it up and go back to the traditional, just for a second. 
BMI = input("What is your BMI (Body Mass Index)?")
BMI = int(BMI)
if BMI >= 40:
    h4r = h3r + 1
else:
    h4r = h3r + 0

#Back to our yes/no loops.
print("Do you have diabetes?")
answer4 = None
while answer4 != 'yes' or answer4 != 'no':
    answer4 = input("Please answer yes or no: ")

    if answer4 == "yes":
        h5r = h4r + 1
        print("Thank you. Let's continue.")
        break
    elif answer4 == "no":
        h5r = h4r + 0
        print("Thank you. Let's continue.")
        break
    
    else:
        print("Hmm, seems we didn't get that.")


print("Do you have chronic kidney disease?")
answer5 =  None
while answer5 != 'yes' or answer5 != 'no':
    answer5 = input("Please answer yes or no: ")

    if answer5 == "yes":
        h6r = h5r + 1
        print("Thank you. Let's continue.")
        break
    elif answer5 == "no":
        h6r = h5r + 0
        print("Thank you. Let's continue.")
        break

    else:
        print("Hmm, seems we didn't get that.")

print("Do you have  liver disease?")
answer6 =  None
while answer6 != 'yes' or answer6 != 'no':
    answer6 = input("Please answer yes or no: ")

    if answer6 == "yes":
        h7r = h6r + 1
        print("Thank you.")
        break
    elif answer6 == "no":
        h7r = h6r + 0
        print("Thank you.")
        break

    else:
        print("Hmm, seems we didn't get that.")
#Now that that's done, we can bring it all home with the final results.
print(h7r, "of your responses to the 8 health questions have determined your risk for catching covid-19.")