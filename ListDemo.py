__author__ = 'zhu'
str="hello are you"
list=str.split()
print(list)
print(len(list))

while len(list)!=0:
    print(list.pop())

list=["hello","world"]
print(" ".join(list))

print("#".join(list[0:2]))
