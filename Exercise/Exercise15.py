from sys import argv

filename = argv[1]
script = argv[2]

txt = open(filename)
print("File name:%s" %script)
print("Content:")
print(txt.read())

print("Type file name again")
filename_again = input("> ")
txt_again = open(filename)
print("Print file name again")
print(txt_again.read())
