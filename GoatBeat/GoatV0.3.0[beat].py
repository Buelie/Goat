import sys
import khl
import random
from khl import Bot , Message , Event , api
@Bot.command(name='welcome')
class wel:
    async def welcome(msg:Message):
        await msg.ctx.channel.send('欢迎使用基于GoatSDK的机器人')
        await msg.ctx.channel.send('Welcome to GoatSDK-based bots')
    def welsdk():
        print('欢迎使用GoatSDK')
        print('Welcome to GoatSDK')
class rndom:
    async def dice(six):
        a = random.choice(1-6)
        b = random.choice(1-6)
    async def brand(ptn):
        brand1 = ['方块','梅花','红心','黑桃']
        brand2 = ['方块','梅花','红心','黑桃']
        brand3 = ['方块','梅花','红心','黑桃']
        brand4 = ['方块','梅花','红心','黑桃']
        br1 = random.choice(brand1)
        br2 = random.choice(brand2)
        br3 = random.choice(brand3)
        br4 = random.choice(brand4)
    async def brand(nbm):
        brn1 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn2 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn3 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brn4 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        bn1 = random.choice(brn1)
        bn2 = random.choice(brn2)
        bn3 = random.choice(brn3)
        bn4 = random.choice(brn4)
    async def captcha(digit):
        capdig = random.choice(1000-9999)
    async def captcha(letter):
        capletter = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        caplet = random.choice(capletter)
    async def captcha(symbol):
        capsymbol = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','"','<','>',',','.','?','/']
        capsym = random.choice(capsymbol)
    def dice(sx):
        a1 = random.choice(1-6)
        b1 = random.choice(1-6)
    def brand(pn):
        bran1 = ['方块','梅花','红心','黑桃']
        bran2 = ['方块','梅花','红心','黑桃']
        bran3 = ['方块','梅花','红心','黑桃']
        bran4 = ['方块','梅花','红心','黑桃']
        brs1 = random.choice(bran1)
        brs2 = random.choice(bran2)
        brs3 = random.choice(bran3)
        brs4 = random.choice(bran4)
    def brand(nm):
        brns1 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns2 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns3 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        brns4 = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        bns1 = random.choice(brns1)
        bns2 = random.choice(brns2)
        bns3 = random.choice(brns3)
        bns4 = random.choice(brns4)
    def captcha(dig):
        capdigs = random.choice(1000-9999)
    def captcha(let):
        capletters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        caplets = random.choice(capletters)
    def captcha(sym):
        capsymbols = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','"','<','>',',','.','?','/']
        capsyms = random.choice(capsymbols)
