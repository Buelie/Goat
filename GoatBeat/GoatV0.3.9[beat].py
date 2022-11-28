import sys
import khl
import random
import os
import datetime
import keyword
import functools
import logging
from khl import Bot , Message , Event , api , bot , message
from os import system , popen
import copy
import code
@Bot.command(name='goat')
async def token(self):
    robtoken = ""
def rtoken(self):
    bottoken = ""
class wel:
    async def welcome(msg:Message):
        await msg.ctx.channel.send('欢迎使用基于GoatSDK的机器人')
        await msg.ctx.channel.send('Welcome to GoatSDK-based bots')
        Bot.run()
    def welsdk(self):
        print('欢迎使用GoatSDK')
        print('Welcome to GoatSDK')
class rndom:
    async def dice(six):
        a = random.randint(1,6)
        b = random.randint(1,6)
        Bot.run()
    async def brand(ptn):
        brand1 = ['方块','梅花','红心','黑桃']
        brand2 = ['方块','梅花','红心','黑桃']
        brand3 = ['方块','梅花','红心','黑桃']
        brand4 = ['方块','梅花','红心','黑桃']
        br1 = random.choice(brand1)
        br2 = random.choice(brand2)
        br3 = random.choice(brand3)
        br4 = random.choice(brand4)
        Bot.run()
    async def brand(nbm):
        brn1 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn2 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn3 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn4 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        bn1 = random.choice(brn1)
        bn2 = random.choice(brn2)
        bn3 = random.choice(brn3)
        bn4 = random.choice(brn4)
        Bot.run()
    async def captcha(digit):
        capdig = random.choice(1000-9999)
        Bot.run()
    async def captcha(letter):
        capletter = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        caplet = random.choice(capletter)
        Bot.run()
    async def captcha(symbol):
        capsymbol = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','"','<','>',',','.','?','/']
        capsym = random.choice(capsymbol)
        Bot.run()
    def dice(sx):
        a1 = random.choice(1,6)
        b1 = random.choice(1,6)
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
        capdigs = random.choice(1000-9999)
    def captcha(let):
        capletters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        caplets = random.choice(capletters)
    def captcha(sym):
        capsymbols = [' ','~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','"','<','>',',','.','?','/']
        capsyms = random.choice(capsymbols)
class load:
    async def loading(msg:Message):
        lad = 1
        while lad <= 100:
            await msg.ctx.channel.send(lad,'%')
            lad += 1
        Bot.run()
    def loadng(self):
        ld = 1
        while ld <= 100:
            print(ld,"%")
            ld += 1
class pykey:
    async def pkey(msg:Message):
        await msg.ctx.channel.send(keyword.kwlist)
        Bot.run()
    def pykey(self):
        print(keyword.kwlist)
class pyver:
    async def pyver(msg:Message):
        pyvr = system("python --version")
        pyer = popen("python --version").read()
        await msg.ctx.channel.send(pyer)
        Bot.run()
    def pyvr(self):
        pvr = system("python --version")
        per = popen("python --version").read()
        print(per)
def cals(self):
    def xlc(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a * b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        print(cas)
    def xlj(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a - b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        print(cas)
    def xla(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a + b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        print(cas)
    def xlu(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a / b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        print(cas)
async def cls(msg:Message):
    async def xaj(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a - b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        await msg.ctx.channel.send(cas)
    async def xac(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a * b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        await msg.ctx.channel.send(cas)
    async def xau(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a / b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        await msg.ctx.channel.send(cas)
    async def xad(self):
        maa = isinstance(a,float)
        mab = isinstance(b,float)
        if maa == True:
            if mab == True:
                cas = a + b
                a = ""
                b = ""
            elif mab == False:
                print('Error: The value of the second number')
            else:
                print('Error: Unknown error')
        elif maa == False:
            print('Error: The value of the first number')
        else:
            print('Error: Unknown error')
        await msg.ctx.channel.send(cas)
#land
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
        elif(opera == '**'):result = int(a ** b)
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
