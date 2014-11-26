# path=raw_input("path:")
from pip.backwardcompat import raw_input

path = "D:\\nginx.conf"

# 以读取的方式打开文件
file = open(path, 'r')

# 读取文件内容,一次读取出所有内容
print(file.read())

# 读取到最后会返回 ""
print(file.readline() == "")

file = open(path, "w")
file.truncate()
file.write("hello world")
file.flush()

file.close()


#复制文件
src=raw_input("src file:")
dest=raw_input("dest file:")
srcFile = open(src)
destFile=open(dest,"w")
destFile.write(srcFile.read())
destFile.flush()
srcFile.close()
destFile.close()
#复制文件2
src=raw_input("src file:")
dest=raw_input("dest file:")
srcFile=open(src,"r")
destFile=open(dest,"w")


