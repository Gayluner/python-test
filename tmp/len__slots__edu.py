#/usr/bin/python3 env
#-*-coding:utf-8-*-
class students(object):
    pass


#给实例绑定一个属性
s=students()
s.name='Michal'
print(s.name)

#给实例绑定一个方法
from types import MethodType

def set_age(self,age):
    self.age=age
    print(self.age)
s.set_age=MethodType(set_age,s)

s.set_age(14)

#给class绑定一个方法

def set_score(self,score):
    self.score=score
    print(self.score)
students.set_score=set_score

s1=students()
s2=students()
s1.set_score(98)
s2.set_score(89)

#shiyo