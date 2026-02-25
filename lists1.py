
#23/09/2025
#E Barberis
#program to make a small list to hold temperatures

tempData = [] #empty list
dayTimelist = ["Mon 9AM", "Mon 9PM", "Tue 9AM", "Tue 9PM", "Wed 9AM", "Wed 9PM"]
total = 0
max = tempData[0]
min = tempData[0]

for idx in range(0,6):
    v= float(input(dayTimelist[idx]))
    tempData.append(v)

print(tempData)

for p in range(0,6):
    total = total + tempData[p]

Avg = total / 6
print("the average temperature is" ,Avg)



for num in range(1, 7):
    if tempData[num] > max:
        max = tempData[num]

print("Highest tempreature was" ,max)

for num in range(1,7):
    if tempData[num] < min:
        min = tempData[num]