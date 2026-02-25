
#E Barberis
#30/08/2025
#assigenemet 3 homework

print("hello! welcome to this program!")
print() #allows for space in between lines
temp1 = float(input("enter temperature for 12PM:"))
temp2 = float(input("enter temperatrure for 1PM:"))
temp3 = float(input("enter temperatrure for 2PM:"))
temp4 = float(input("enter temperatrure for 3PM:"))
temp5 = float(input("enter temperatrure for 4PM:"))
temp6 = float(input("enter temperatrure for 5PM:"))
temp7 = float(input("enter temperatrure for 6PM:"))

time = 12

max = temp1 #used to find highest number
if(temp2 > max):
    max = temp2
    time = 1
if(temp3 > max):
    max = temp3
    time = 2
if(temp4 > max):
    max = temp4
    time = 3
if(temp5 > max):
    max = temp5
    time = 4
if(temp6 > max):
    max = temp6
    time = 5
if(temp7 > max):
    max = temp7
    time = 6

print()
print("The highest temperature was" ,max, "! at" ,time, "PM!" )

coldtime = 12

min = temp1 #used to find highest number
if(temp2 < min):
    max = temp2
    coldtime = 1
if(temp3 < min):
    min = temp3
    coldtime = 2
if(temp4 < min):
    min = temp4
    coldtime = 3
if(temp5 < min):
    min = temp5
    coldtime = 4
if(temp6 < min):
    min = temp6
    coldtime = 5
if(temp7 < min):
    min = temp7
    coldtime = 6

print()
print("The coldest temperature was" ,min, "! at" ,coldtime, "PM!" )

