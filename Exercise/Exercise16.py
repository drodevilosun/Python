
from sys import argv

filename = argv[1]

print("Edit file txt: %r" %filename)
txt = open(filename,'r')
print("print file text:")
print(txt.read())

txt = open(filename,'w')
print("Empty file text.")
print("Press Cltr-C to exit or enter to continue")
input("?")
txt.truncate()

txt = open(filename,'r')
print("Print file text again:")
print(txt.read())
print("If you see nothing, file were emptied")

txt = open(filename,'w')
print("\nInput string which will be writed to file text:")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("Write to file text:")

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print("Done. We close file")
#txt.close()