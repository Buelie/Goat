import sys
#out.py
Username = 'yyds'
Password = '321654'
uspa = 1
while uspa == 1:
    GoatBeatUsername = input("Please enter your username:")
    GoatBeatPassword = input("Please enter a password:")
    if GoatBeatUsername == Username:
        if GoatBeatPassword == Password:
            break
        else:
            print("密码错误")
    else:
        print("用户名错误")
    print("Registered account and password:","|Username|",GoatBeatUsername,"|Password|",GoatBeatPassword)
cnc = 1
while cnc == 1:
    GoatBeatIP = input("Please fill in the IP address (do not fill in randomly, at your own risk):")
    if GoatBeatIP == '127.0.0.1':
        break
    else:
        print("ip地址错误")
    continue
print("IP",GoatBeatIP)
cna  = 1
while cna == 1:
    GoatBeatSet = input("Please select a mode (1=Command Terminal 2=GoatBeat Extended Command Terminal):")
    if GoatBeatSet == '1':
        print("已启用命令终端模式")
        break
    elif GoatBeatSet == '2':
        print("已启用GoatBeat")
        GoatBeatSetting = input("请选择启动或关闭(close=关闭 open=开启):")
        if GoatBeatSetting == 'close':
            print("已关闭并且启用命令终端模式")
            break
        else:
            print("成功启动")
            GoatBeatInput = input("Please enter a command:")
            if GoatBeatInput == 'open all protocol':
                print("成功启动所有GoatBeat协议")
            elif GoatBeatInput == 'close GoatBeat':
                break
            else:
                print("命令库内没有该指令!!!")
    else:
        print("无法启动，请检查输入内容是否有误")
        continue
cnt = 1
while cnt == 1:
    GoatBeat = input("Please enter the execute command:")
    if GoatBeat == 'Launch the GoatBeat protocol':
        print("成功启动GoatBeat协议")
    elif GoatBeat == 'Start the LBV command protocol':
        print("成功启动LBV协议")
    elif GoatBeat == 'Start the Out-of-Zone Linking Protocol':
        print("成功启动外区链接协议")
    elif GoatBeat == 'Start the International Link Agreement':
        print("成功启动国际链接协议")
    elif GoatBeat == 'start VPN':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在启动Goat VPN-",b2,"%-")
                b2 += 1
            else:
                break
        print("成功启用VPN")
    elif GoatBeat == 'GitHub start':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在登入GitHub后台[",b2,"%]")
                b2 += 1
            else:
                break
        print("成功登入GitHub后台")
    
    elif GoatBeat == 'BliBli start':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在登入小破站后台[",b2,"%]")
                b2 += 1
            else:
                break
        print("成功登入小破站后台")
    elif GoatBeat == 'Register an empty class':
        print("成功注册一个空类")
        a = 1
        while a == 1:
            Register = input("is an empty class bin value for registration:")
            if Register == 'is an empty class +1':
                print("已给予空类初始值")
                b = 1
                while b == 1:
                    classes = input("Execute class commands:")
                    if classes == 'add class a':
                        print("已添加类属性")
                    elif classes == 'close':
                        break
                    else:
                        print("类命令库内没有该命令")
                    continue    
            elif Register == 'close':
                break
            else:
                print("无法识别此命令")
            continue
    elif GoatBeat == 'Register the Minecraft Online Rules class':
        print("成功注册MC联机规则类")
    elif GoatBeat == 'new file':
        f = open('new.txt','w')
        f.close()
        print("成功新建文本文件")
    elif GoatBeat == 'cofig file(json)':
        f = open('cofig.json','w')
        f.close()
        print("成功新建配置文件")
    elif GoatBeat == 'close':
        break
    elif GoatBeat == 'import C all to python':
        a2 = 1
        a1 = 1
        while a1 == 1:
            if a2 <= 100:
                print("正在导入扩展类-",a2,"%-")
                a2 += 1
            else:
                break
        print("成功引入适用于python的C++,C,C#类")
    elif GoatBeat == 'import java to python':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在导入扩展类-",b2,"%-")
                b2 += 1
            else:
                break
        print("成功引入适用于python的java类")
        d = 1
        while d == 1:
            java = input(">>>java command>>>")
            if java == 'import JFrame':
                print("已导入JFrame组件")
            elif java == 'close':
                break
            else:
                print("Java命令库内没有该命令")
            continue
    elif GoatBeat == 'import minecraft to the all':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在导入扩展类-",b2,"%-")
                b2 += 1
            else:
                break
        print("成功引入MC扩展类")
    elif GoatBeat == 'import minecraft java to the http':
        b2 = 1
        b1 = 1
        while b1 == 1:
            if b2 <= 100:
                print("正在导入扩展类-",b2,"%-")
                b2 += 1
            else:
                break
        print("成功引入MC扩展类附属-联机附属")
        c = 1
        while c == 1:
            mhttp = input (">>>Please enter a command:")
            if mhttp == 'start http':
                print("已成功启动http协议")
            elif mhttp == 'have 32k':
                print("已获取32k")
            elif mhttp == '#wd#':
                print("已获取OP权限")
            elif mhttp == 'close':
                break
            else:
                print("扩展库内没有此命令")
            print("命令库已更新")
            continue
    elif GoatBeat == '明月庄主':
        print("恭喜你获得了100,000,000美元")
    elif GoatBeat == 'minecraft':
        print("送你个网易开发者账号：[yydsfps@163.com 密码：找作者要]")
    elif GoatBeat == 'mc':
        print("送你个TDR服务器账号：[名字:wer 密码：321654 服务器地址:找作者要]")
    elif GoatBeat == 'blibli':
        print("小破站的大会员免费啦！！！")
    else:
        print("命令库内没有此命令！！！")   
    print("命令已初始化完成")
    continue
cloo = input("关闭")
