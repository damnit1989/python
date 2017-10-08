# -*- coding: utf-8 -*-

' a super function test module '

__author__ = 'lmm'

__metaclass__ = type

class Bird:
    name = 'lmm'
    def __init__(self):
        self.hungry = True
        # name = '234'
    def eat(self):
        if self.hungry:
            print 'Aaaah..'
            self.hungry = False
        else:
            print 'no thanks'
    def out(self):
        print 'bird out'

# 旧版python
# class SongBird(Bird):
    # def __init__(self):
        # Bird.__init__(self)
        # self.sound = 'Squawk!'
    # def sing(self):
        # print self.sound
    # def out(self):
        # super(SongBird,self).out()

# 新版python使用super调用父类的构造方法
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
# b = Bird()
# print b.name
sb = SongBird()
sb.sing()
print(sb.hungry)
sb.eat()

sb.eat()
print(sb.hungry)

sb.out()
print sb.name
