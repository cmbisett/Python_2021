#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#print the number 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#the first portion of the arguments if an undefined function


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#print number 5 because it is a return statement


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#print the number 5 because return statement, wont allow the rest of the function to coninure through


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#will print the number 5
#upon running it, it is also printing the word NONE


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#it will print the two seperate functions, 3 and 5


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#because they are stings it will just write 2 and 5 together in a new string. Not add the nums together


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#will print the num 100 and the print the num 10 because b is not less than 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#will print in order: 7, 14, 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#it will print 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#it will print 500, 500, 300, 500 because it is using the already defined value for b, not the local value inside the function
#when the argument b was put in


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#it should be the same as before because the print statement runs before the new return on b
#so it should be 500, 300, 500, 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#should be 500, 500, 300, 300 because the last print(b) is using the new value for b
#which is b=foobar()


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#should print in order: 1, 3, 2 because foo() calls the function bar inside which equals print(3)


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#because the fuction bar is being called inside foo() the numbers printed should be
#1, 3, 5, 10