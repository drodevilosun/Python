from sys import argv

user_name = argv[1]

prompt = '> '
print("Hi. My name is %s" %user_name)
print("Input string")
#use input in python 3 and raw_input in python 2 to input string
string = input(prompt)
print(string)

print("Where do you live")
live = input(prompt)
print("I live in:%s" %live)

print("What number do you like?")
num = input(prompt)
#input number, not string
print("I like number: %d" %int(num))
