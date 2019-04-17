from sys import exit

def test_number():
    k = input(">")
    num = int(k)
    #if "0" in next or "1" in next:
    #    print("number of k:%d" %k)
    #else:
    #    print("???")
    if "0" in next():
        print("num is:%d" %num)

test_number()