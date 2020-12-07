import string
import random


def easy(x):
    length = int(x)
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
    return randomstr


def medium(x):
    length1 = int(x)
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length1))
    return randomstr


def hard(x):
    mylist = '!@#$%&'

    length1 = int(x)
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + mylist, k=length1))
    return randomstr

"""
print(easy(7))
print(medium(8))
print(hard(13))
"""