__author__ = 'zhu'

hash = {"name": "zhuwei", "age": 10}

print(hash)
print(hash.__class__)
print(hash["name"])

# 删除一个key
del hash["name"]
print(hash)

# 添加新的key
hash["address"] = "beijing"
print(hash)


def myFun(text):
    print(text)


# hash中可以value 类型可以是一个function
hash["fun"] = myFun
print(hash)

hash["fun"]("hello world")

