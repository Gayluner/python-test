import hashlib
from learn import date_type

md5=hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())
date_type(md5.hexdigest())


import random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

s=User('Michel','aaaa')
date_type(User('Michel','aaaa'))
date_type(s.password)