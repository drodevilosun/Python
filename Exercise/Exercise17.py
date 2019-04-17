from sys import argv
from os.path import exists

from_file = argv[1]
to_file = argv[2]
print("Copying from %r to %r" %(from_file,to_file))

txt = open(from_file,'r')

data = txt.read()

print("The input file is %d bytes long" %len(data))
print("Print input file:%r" %from_file)
print(data)

print("Does output file exist? %r" %exists(to_file))
print("Press ENTER to continue or Ctrl-C to exit")
input()

txt_copy = open(to_file,'w')
txt_copy.write(data)

print("Print output file to checking:%r" %to_file)
txt_copy = open(to_file,'r')
print(txt_copy.read())

print("Done!")

txt.close()
txt_copy.close()