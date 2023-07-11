# string join
#formating  s
#formating format
#formating f
#unpacking sequence characters into variables
#reverse string
#is numeric
#is digit 
#is lower
# join
# is numeric
#list
#append
#insert
#remove
#pop
#extend
#reverse
#sort
#clear
#del

firstname = 'Deepak'
lastname = 'Yadav'
middlename = 's'
name = firstname+' '+middlename+' '+lastname
print(name)
name_format = 'My name is {} {}'.format(firstname, lastname)
print(name_format)

name_string_format = f'My name is ###### {firstname} {lastname}'
print(name_string_format)

#unpacking sequence characters into variables
language = 'python'
a,b,c,d,e,f = language 
print(a,b,c,d,e,f)

#reverse the string
print(language[::-1])

number='123'
gender='MALE'
print(number.isnumeric())
print(number.isdigit())
print(middlename.islower())
print(gender.isupper())

fruits = ['Mango','Apple','Pineapple']
print(fruits)
fruits.insert(2,'Banana')
print(fruits)
vegetables = ['Potato','LadyFinger']
vegetables.extend(fruits)
print(vegetables)

print(vegetables.pop())
print(vegetables.pop())
fruits.sort()
print('sort fruits',fruits)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.clear()
print(cars)