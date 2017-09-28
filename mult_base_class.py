<<<<<<< HEAD
# -*- coding: utf-8 -*-
# 继承多个超类

'a mult base class module example'  


__author__ = 'lmm'


class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'hi my value is ',self.value

class TalkingCalculator(Calculator,Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
=======
# -*- coding: utf-8 -*-
# 继承多个超类

'a mult base class module example'  


__author__ = 'lmm'


class Calculator:
    value = 0
    def calculate(self,expression):
        self.value = eval(expression)

class Talker:
    value = 1
    def talk(self):
        print 'hi my value is ',self.value

#
#class TalkingCalculator(Calculator,Talker):
class TalkingCalculator(Talker,Calculator):
    pass


tc = TalkingCalculator()
print(tc.value)
tc.calculate('1+2*3')
tc.talk()
print(tc.value)
>>>>>>> 7aeeaf3d607e377b01a1647554ed4bfd2b20463c
