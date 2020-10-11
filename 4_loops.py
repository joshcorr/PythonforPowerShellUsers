#Only for and while loops

#Importing a builtin Library
import webbrowser
# create an array
testsites = ['https://python.org','https://powershell.org']

# look over the file
for website in testsites:
    webbrowser.open_new(website)

c = 5
while c != 0:
    print(c)
    c -= 1
