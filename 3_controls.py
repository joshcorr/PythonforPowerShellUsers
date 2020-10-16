# In PowerShell, 
"""
<#
if($ps -lt 5) {
    #Code
} elseif ($ps -eq 5) {
    if ($something) { 
        #Code
    } else {
        #Code
    }
} else {
    #Code
}
#>
"""
#PowerShell Also has Switch, but not in Python

#region if/elif/else

# if elif else
val = 4
if val == 5:
    # space characters are critical for
    # python interpreter
    print("This is something")
elif val == 3:
    print("Don't nest IF")
else:
    print("Default")



# Ternary flow control, i.e. one line if/else
val = None
"something" if val is (None or '') else val
#endregion

#region try/catch/finally
#In PowerShell
"""
try {
    Remove-SomethingThatCanBreak
} catch {
    throw
    Write-Host "Handling the exception"
} finally {
    Write-Host "Executed a function things"
}
"""

#More Importantly Try Catch Finally
try:
    value = 100 / 0
except ZeroDivisionError: 
    print("ummmm, shouldn't do that")
finally:
    print("finished testing some math")



#swollow the error
try:
    value = 100 / 0
except ZeroDivisionError: 
    pass #shouldn't do this it is not Zen
finally:
    print("finished testing some math")




#What happens if it works?
try:
    value = 100 / 1
except ZeroDivisionError:
    print("ummmm, shouldn't do that")
else:
    print("Division is {var1}".format(var1=value))
finally:
    value = None
    print("cleaning up the vars")
    print(value is None)


#endregion
