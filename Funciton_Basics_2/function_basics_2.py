#Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    list = []
    for i in range(num, 0, -1):
        list.append(i)  
    print(list)
countdown(10)

#Create a function that will receive a list with two numbers. Print the first value and return the second.
def  printReturn(arr): 
    print(arr[0])
    print(arr[1])
    return
printReturn([1, 2])

#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def fplusp(arr):
    i = arr[0]
    x = len(arr)
    print(i + x)

fplusp([1,2,3,4,5])

#Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def greaterThan(arr):
    list = []
    length = len(arr)
    for i in range(length):
        if (i> arr[1]):
            list.append(i)
        else:
            return
    print(list[i])

greaterThan([5,2,3,2,1,4])