# variables are strongly typed
# Named reference to an object

None # is $null
bool # True/False

# Immutable reference to value
x = '100'
# Reference to the same value
y = x

#id() can be used to determine the same object
# y is x
# can also be used.

list_test = ['something','anotherthing']
list_test.append(7)
list_test[2] = 8

#Lists - Mutable
list_test = [4,5,6]

#Tuples - Immutable
tuple_test = (1,2,3)

#Disctionaries - Mutable
dict_test = {'key':'value','user':'jam'}
dict_test['user']