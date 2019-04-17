# This exercise learn about seek() in python 
# Refs: https://python-reference.readthedocs.io/en/latest/docs/file/seek.html
from sys import argv

input_file = argv[0]

def print_all(f):
    print(f.read())

def print_a_line(time,f):
    print(time,f.readline())

def rewind(f):
    f.seek(2)

def close_file(f):
    f.close()

file_name = open(input_file)
print("Print whole file:\n")
print_all(file_name)

print("Let's rewind.")
rewind(file_name)

print("Print each line of file:")
i = 1
for i in range(0,3):
    print_a_line(i,file_name)

close_file(file_name)

