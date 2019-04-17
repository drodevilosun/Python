string_tmp = "%r %r %r %r"

print (string_tmp % (1,2,3,4))
print (string_tmp % ("Machine", "Learning", "Artificial", "Intelligence"))
print (string_tmp%(string_tmp,string_tmp,string_tmp,string_tmp))
print (string_tmp % (True,False,True,False))