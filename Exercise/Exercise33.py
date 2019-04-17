from sys import argv

i = 5
num = []

print("Add number to variable num:")

while i > 0:
    print(">num got: %d" %i)
    num.append(i)
    i -= 1

for i in num:
    print("Number in num:%d" %i)

print("%d" %num[4])

