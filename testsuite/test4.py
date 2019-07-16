import sys

def a():
    print(sys._getframe().f_code.co_name)


a()