#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
ordercost = input("What was the total bill?\n $") 

tippercent = input("How much tip would you like to give? 10, 12, or 15?\n") 
      #10, 12, or 15? 12
payer = input("How many people to split the bill?\n")
#7
#totalcost = float(ordercost) + (float(tippercent)*float(ordercost)/100)
totalcost = float(ordercost) * (1 + float(tippercent) / 100)

#perperson = round(totalcost/int(payer),2)
perperson = "{:.2f}".format(totalcost/int(payer))
print(f"Each person should pay: ${perperson} ")
#19.93


