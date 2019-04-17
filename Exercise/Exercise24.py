
from sys import argv 


def formula_count(num):
    a = num/2
    b = a*num
    c = a + b
    return a, b, c

def print_all_file(f):
    print(f.read())

def write_to_file(f):
    data = input('>')
    f.write("\n%s" %data)

file_name = input(">")

num_tmp = 36
print("Let calculate first:")
x, y, z = formula_count(num_tmp)
print("Number was calculated: %r %r %r" %(x,y,z))

print("Print content of file first:")
file_open = open(file_name)
print_all_file(file_open)

print("Modify file:")
file_open = open(file_name,'a+')
write_to_file(file_open)

print("Print file again:")
file_open = open(file_name,'r')
print_all_file(file_open)



