
# 定义函数
def print_two(*args):
    arg1,arg2 = args
    print("arg1:%s,arg2:%s" %(arg1,arg2))

def print_two(arg1,arg2):
    print("arg1:%s,arg2:%s",arg1,arg2)

def add(a,b):
    return a+b

print_two("hello","world")
print_two("hello","world")

print(add(1,2))
