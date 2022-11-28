import sys
import khl
import random
import os
import datetime
import keyword
import functools
import logging
import copy
import code
from os import system , popen
def xm(self):
    xmname = ""
    @Bot.command(name=xmname)
def token(self):
    robtoken = ""
class wel:
    def wel(self):
        print("Welcome to the goats")
class rndom:
    def dice(sx):
        a1 = random.randint(1,6)
        b1 = random.randint(1,6)
        Bot.run()
    def brand(pn):
        bran1 = ['方块','梅花','红心','黑桃']
        bran2 = ['方块','梅花','红心','黑桃']
        bran3 = ['方块','梅花','红心','黑桃']
        bran4 = ['方块','梅花','红心','黑桃']
        brs1 = random.choice(bran1)
        brs2 = random.choice(bran2)
        brs3 = random.choice(bran3)
        brs4 = random.choice(bran4)
        Bot.run()
    def brand(nm):
        brns1 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns2 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns3 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns4 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        bns1 = random.choice(brns1)
        bns2 = random.choice(brns2)
        bns3 = random.choice(brns3)
        bns4 = random.choice(brns4)
        Bot.run()
    def captcha(dig):
        capdigs = random.randint(1000,9999)
    def captcha(let):
        capletters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        caplets = random.choice(capletters)
    def captcha(sym):
        capsymbols = [' ','~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','"','<','>',',','.','?','/']
        capsyms = random.choice(capsymbols)
class load:
    def loadng(self):
        ld = 1
        while ld <= 100:
            print(ld,"%")
            ld += 1
            class pyver:
class pev:                
    def pyvr(self):
        pvr = system("python --version")
        per = popen("python --version").read()
        print(per)
def cal(opera,a,b,inter):
    A = copy.deepcopy(a)
    B = copy.deepcopy(b)
    _a = comp(a)
    _b = comp(b)
    if(_a[0] != 'error'):
        a = _a[0]
    else:
        return _a
    if(_b[0] != 'error'):
        b = _b[0]
    else:
        return _b
    if(isinstance(a,str) and a.startswith('{')):
        a = comp(a)[0]
    if(isinstance(a,str) and a.startswith('{')):
        b = comp(b)[0]
    opera = opera[1:]
    result = None
    try:
        if(opera == '+'):result = a + b
        elif(opera == '-'):result = a - b
        elif(opera == '/'):
            if(b != 0):
                result = a / b
            else:
                return ['error','ZeroDivisionError:division by zero']
        elif(opera == '*'):result = int(a * b)
        elif(opera == '<'):result = int(a < b)
        elif(opera == '<='):result = int(a <= b)
        elif(opera == '='):result = int(a == b)
        elif(opera == '>='):result = int(a >= b)
        elif(opera == '>'):result = int(a > b)
        elif(opera == '&'):result = int(a and b)
        elif(opera == '|'):result = int(a or b)
        elif(opera == '!'):result = int(not a)
        elif(opera == '^'):result = int(a ** b)
        elif(opera == '%'):result = int(a % b)
        else:return ['error','OperatorError:undefined operator']
        if(isinstance(result,list)):
            string = str(result)
            string = string.replace('[','{')
            string = string.replace(']','}')
            return [string]
        elif(inter and isinstance(result,mytype.stack)):
            return ['stack' + str(result._stack)]
        elif(inter and isinstance(result,mytype.queue)):
            return ['queue' + str(result._queue)]
        else:
            return [result]
    except:
        return ['error','TypeError: can\'t concatenate {0} to {1} with operater \'{2}\''.format(comp(A,inter=True)[0],comp(B,inter=True)[0],opera)]
