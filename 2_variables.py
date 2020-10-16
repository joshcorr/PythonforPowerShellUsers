
# Variables are dynamically typed 
# Named reference to an object
# No $$$
# lowercase with underscores

None # is $null
# note: is keyword checks if objects refer to the same object
None == 0
0 is None

bool ()#  $True/$False
bool(0) # should be False
bool(1) # should be True



# Immutable reference to value
# $ps = '100'
x = '100'
# Reference to the same value
y = x

#id() can be used to determine the same object
# y is x
# can also be used.


#$ps =  New-Object System.Collections.Generic.List[string]
#$ps.add('something','anotherthing')

#Lists - Mutable
list_test = [4,5,6]
list_test = ['something','anotherthing']
dir(list_test)

list_test.append(7)
list_test[2] = 8
list_test.remove(8)



#$ps = @('something','anotherthing')
#Tuples - Immutable
tuple_test = (1,2,3)
type(tuple_test)



#$ps = @{'key'='something';'anotherkey'='somevalue'}
#Dictionaries - Mutable (as long as the keys are immutable - i.e. strings, tuples, ints, etc.)
dict_test = {'key':'value','user':'jam'}
dict_test['user']


#One other type called Sets, like math sets
set_test = set()
another_set_test = {1,2,3,3}
set_test in another_set_test