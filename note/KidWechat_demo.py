#需要安装wxpy模块
#需要两个微信号，一个用来做机器人，另一个帐号做测试
#两个帐号最好有一个共同好友，满足实现建群聊的功能


#在idle或python 3.x导入模块
from wxpy import *

#启动Bot
bot = Bot()


#电脑会出现二维码，用微信帐号1扫描二维码
#扫描完毕后，idle中会显示Logging successfully
#输入下述代码



user_account = bot.friends().search('老李')[0] 
#'老李' 微信帐号2的昵称，请自行更改！

@bot.register(user_account, msg_types='Text')
def reply(msg):
	if msg.text[:2] == '寻找' and msg.text[2:]:
        try:
            friend_name = msg.text[2:]
            search_friend = bot.friends().search(friend_name)[0]
            users = [search_friend, user_account]
            group = bot.create_group(users, topic='小白屋')
            group.add_members(user_account, use_invitation=True)
            group.add_members(search_friend, use_invitation=True)
            group.send('Bingo!')
        except:
            return "{}还不是我的好友呢？".format(friend_name)
        
	elif msg.text[:2] == '查找' and msg.text[2:]:
        return '查找公众号功能暂未上线'
        
	elif msg.text == '帮助':
        help_info = """
            帮助文档：
            帮助，获取帮助文档
            输入：寻找xx，则寻找好友并创建群聊
            输入：查找xx，则查找公众号并返回二维码
            输入其他，则开启自动聊天模式"""
        return help_info
    
    else:
        return '我听不懂你说什么呢？输入"帮助"试一下。'
        
bot.start()

#此时，就可以用微信帐号2跟微信帐号1聊天