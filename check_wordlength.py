#E Barberis
#24/02/2026
#check's wordlength with functions

#function body
def countwrdlen(wordarray, length):
    counter = 0 #keep track of count of words
    #loop from 0 until whatever array size
    for i in range(0,len(wordarray)):
        if(len(wordarray[i])>= length):
            counter = counter + 1
    #end of loop
    return counter
#end of function

#call function
print(countwrdlen(["" , "Flash"  , "Captain America" ,"Superman", "Iron Man" , "Batman"], 5))

