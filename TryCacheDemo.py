from pip.status_codes import ERROR

__author__ = 'zhu'
import sys

try:
    file = open("D:\\nginx.conf","r")
    print(file.read())
except EOFError:
    print("error")
    exit(1)
finally:
    print("release")







