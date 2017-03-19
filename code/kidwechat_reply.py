#! python3
# -*- coding:utf-8 -*-
from wxpy import *


bot = Bot(cache_path=True)
KEY = '042c8822f369426aa4ff5396880c84ad'
HELP = """
    输入"帮助"，获取帮助文档
    输入"寻找xx"，则寻找好友并创建群聊
    输入"查找xx"，则查找公众号并返回二维码
    输入其他，则开启自动聊天模式"""

@bot.register(msg_types='Text')
def reply(msg):
    if msg.text[:2] == '寻找' and msg.text[2:]:
        try:
            friend_name = msg.text[2:]
            search_friend = ensure_one(bot.friends().search(friend_name))
            users = [search_friend, msg.sender]
            group = bot.create_group(users, topic='小白屋')
            reply = '{}已经找到，去"小白屋"里聊天吧。'.format(friend_name)
            group.add_members(msg.sender, use_invitation=True)
            group.add_members(search_friend, use_invitation=True)
            group.send('Bingo!')
        except:
            reply = "{}还不是我的好友呢？快把我推荐给他吧。".format(friend_name)
            
        msg.reply(reply)      
        
    elif msg.text[:2] == '查找' and msg.text[2:]:
        msg.reply('查找公众号功能暂未上线，请耐心等待哦。')
        
    elif msg.text == '帮助':
        msg.reply(HELP)
     
    else:
        Tuling(api_key=KEY).do_reply(msg)

@bot.register([Group],TEXT)
def reply(msg):
    print(isinstance(msg.sender, Group))
    print(msg.is_at)
    if isinstance(msg.sender, Group) and msg.is_at:
        Tuling(api_key=KEY).do_reply(msg)
  
bot.start(block=True)