x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
print(x)

#Change the last_name of the first student from 'Jordan' to 'Bryant'
# students['last_name'] = 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'andres'
print(sports_directory)

#Change the value of 20 in z to 30
z[0]['y'] = 30
print(z)




#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function 
#loops through each dictionary in the list and prints each key and the associated value. 
#For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")

iterateDictionary(students)


#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and 
#a key name, the function prints the value stored in that key for each dictionary. 
#For example, iterateDictionary2('first_name', students)
def iterateDictionary2(key_name, students):
    for i in range(len(students)):
        print(students[i][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)

#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
#prints the name of each key along with the size of its list, and then prints the associated 
#values within each key's list. 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(key_name, dojo):
    print(f"{len(dojo[key_name])} {key_name}") 
    for i in range(len(dojo[key_name])):
        print(dojo[key_name][i])

printInfo('locations', dojo)
printInfo('instructors', dojo)



