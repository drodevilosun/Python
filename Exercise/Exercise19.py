def Check_print_of_function(num1,num2):
    print("Print number 1: %d" %num1)
    print("Print number 2: %d" %num2)
    print("End")

print("Give function nunber directly:")
Check_print_of_function(10,20)

print("Use variable from out script:")
tmp1 = 20
tmp2 = 30
Check_print_of_function(tmp1, tmp2)

print("Do match inside function:")
Check_print_of_function(10+20,23+58)

print("Combine the two: variable and math:")
Check_print_of_function(tmp1 + 10, tmp2 + 40)