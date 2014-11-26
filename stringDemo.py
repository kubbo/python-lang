print("hello word")

# 字符串格式化
x = "hello %d" % 10
a = 1
b = 2
c = "hello"
d = " world"
print("hello %d,%d" % (a, b))
print(x)
# 字符串可以相加
print(c + d)

formatter = "%d,%d,%d,%d"
print(formatter % (1, 2, 3, 4))
# 三个引号中可以打印引号
str = """ hello "world" \n """
print(str)


