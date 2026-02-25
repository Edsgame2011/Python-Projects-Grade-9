array = [34, 67, 21, 41, 90, 45, 100, 56, 76]
size = len(array)
pass_=0

for i in range(0,size):
    for j in range(0, size-i-1):
        if(array[j]>array[j+1]): #checking if array is in right order
            array[j], array[j+1] = array[j+1], array[j]
    pass_=pass_+1
    print("After pass", pass_)
    print(array)
print(array)