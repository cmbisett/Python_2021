#PRINT ALL INTERGERS FROM 0 TO 150

for i in range(0,151):
    print(i)

#PRINT ALL MULTIPLES OF 5 FROM 5 TO 1000

for x in range(5,1001):
    if (x%5 ==0):
        print(x)

#PRINT ALL INTERGERS 1 TO 100. IF DVISABLE BY 5, PRINT "Coding" INSTEAD. IF DIVISABLE BY 10, PRINT "Coding Dojo"

for i in range(1,101):
    if(i%10 ==0):
        print('Coding Dojo')
    elif(i%5 ==0):
        print('Coding')
    else:
        print(i)

#ADD ODD INTEGERS FROM 0 TO 500,000, AND PRINT THE FINAL SUM
#not sure how to print just the final sum. 
for i in range(0,500001):
    if(i%2 ==1):
        i+=i
        print(i)
    
#PRINT POSITIVE NUMBERS STARTING AT 2018, COUNTING DOWN BY FOURS

for i in range(2018,0,-4):
    print(i)

#SET THREE VARIABLES: lowNum, highNum, mult. STARTING AT lowNum AND GOING THORUGH highNum, 
# PRINT ONLY THE INTEGERS THAT ARE A MULTPLE OF mult. 

lowNum = 4
highNum = 32
mult = 4

for i in range(lowNum, highNum):
    if(i%mult ==0):
        print(i)

