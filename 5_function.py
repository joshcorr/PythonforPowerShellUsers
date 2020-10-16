#In PowerShell
"""
function Get-Something {
    param (
        [string[]]$thing
    )
    foreach ($t in $things){
        Write-Host $t
    }
}
"""
#region functions
def powershell_python():
    print('This is a function')
    #return is key for returning values
    return

#positional arguments mandatory,
def powershell_python(name, optional=yes):
    if optional == 'yes':
        print('This uses an optional arguments')
    print('This is a function {var1}'.format(var1=name))
    return

#endregion