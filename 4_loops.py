#In PowerShell
"""
foreach ($v in $vars) {
    Get-Something $v
}

while ($somethingTrue){
    Get-Something
    break
}

do {
    Stop-Something.. #jk
} until ( -Not $somethingTrue)


Get-something | foreach-object { Get-Something -thething $psitem }
"""


#Only for and while loops


#region for

#Importing a builtin Library
import webbrowser
# create an list
testsites = ['https://python.org','https://powershell.org']

# look over the variables
for website in testsites:
    webbrowser.open_new(website)


count = 4
results = []
import uuid
for c in range(count):
    results.append(uuid.uuid4())
list(results)


#endregion

#region while


c = 5
while c != 0:
    print(c)
    c -= 1


#endregion

#region Somefunctions
#Iterator fucntion can create something similar to a foreach object
keys = {"user1":4,"user2":5,"user3":6}
iterable_test = keys.keys()
iterator_test = iter(iterable_test)
for i in iterator_test:
    print(i)


#enumerate function
american_football_teams = ["Patriots","Jaguars","Seahawks","Chiefs"]
for i,value in enumerate(american_football_teams):
    print(i,value)


#endregion