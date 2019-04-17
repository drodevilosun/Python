
# this one is like your scripts with argv
def print_args(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1,arg2))
# ok, that *args is actually pointless, we can just do this
def print_args_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1,arg2))
# this just takes one argument
def print_1agrs(arg1):
    print("arg1: %r" %arg1)

print(print_args("Hoang","Dro"))
print(print_args_again("Hoang","Dro"))
print(print_1agrs("Hoang"))
