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