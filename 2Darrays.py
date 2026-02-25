#14/01/2026
#E Barberis
#2D Arrays example
#STEP 1: Setting up the data
stats = [[0,0,0,8,11,9, 15],          #sun
         [18,20,97,346,475,433,293],  #mon
         [11,8,63,349,411,522,239],   #tue
         [20,29,89,465,532,529,301],  #wed
         [17,36,96,501,599,0,0],      #thu
         [0,0,0,0,6,3,0],             #fri
         [0,0,0,0,1,6,12]             #sat
    ]

days = ["Sund", "Mond", "Tues", "Wedn", "Thur", "Frid", "Satu"]
times = ["6:00am" ,"7:00am" ,"8:00am" ,"9:00am" ,"10:00am" ,"11:00am" ,"12:00pm"]

#STEP 2: Printing the data without formatting
#print(stats)

#STEP 3: Print it as a CUBE of data/matrix
for row in range(7): #go through each row (day)
    for col in range(7):  #go through each col (hour)
        print(stats[row][col], end = " ")
    print()                   #After each day print a new line

#STEP 4:
#Question 1: Busisest day and time?
maxDay=0       #position of max row
maxHour=0      #position of max col

for day in range(7):   #go through each day
    for hour in range(7):    #withing each day go to each hour
        if(stats[day][hour]>stats[maxDay][maxHour]):
            maxDay = day         #if a value higher was found
            maxHour = hour

#print in 2 different way
print("The busiest time on the network was on", days[maxDay], "at", times[maxHour])
# or print(f"busiest day on the networkk was on {days[maxDay]} at {times[maxHour]}")

#Question 2: Find the day with the highest total users

maxTotal = 0
busiestDay = 0

for day in range(7):
    dayTotal = sum(stats[day])#sum users for that day

    if dayTotal > maxTotal:
        maxTotal = dayTotal
        busiestDay = day

print("The day with the highest total users is", days[busiestDay],
      "with", maxTotal, "users")

#Question 3: Find the busiest hour
maxTotal = 0
busiestHour = 0

for hour in range(7):
    hourTotal = sum(stats[hour])#sum users for that day

    if hourTotal > maxTotal:
        maxTotal = hourTotal
        busiestHour = hour

print("The hour with the highest total users is", hour ,
      "with", maxTotal, "users")