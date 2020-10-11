#Write-Host 'HelloWorld'
# echo 'bla'
# Write-Output 'Something'
print("Hello World")

testvar = 'Hello %s' % ('PowerShell')
print(testvar)

testvar = 'Hello {0}'.format('PowerShell')
print(testvar)

testvar = 'Hello {Var1}'.format(Var1='PowerShell')
print(testvar)