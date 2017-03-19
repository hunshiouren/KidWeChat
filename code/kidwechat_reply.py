#! python3
# -*- coding:utf-8 -*-
from wxpy import *

bot = Bot(cache_path=True)
help_info = """
    帮助文档：
    输入"帮助"，获取帮助文档
    输入"寻找xx"，则寻找好友并创建群聊
    输入"查找xx"，则查找公众号并返回二维码
    输入其他，则开启自动聊天模式"""
tuling = Tuling(api_key='042c8822f369426aa4ff5396880c84ad')

@bot.register(msg_types='Text')
def reply(msg):
    if msg.sender in bot.friends(): 
        if msg.text[:2] == '寻找' and msg.text[2:]:
            try:
                friend_name = msg.text[2:]
                search_friend = bot.friends().search(friend_name)[0]
                users = [search_friend, msg.sender]
                group = bot.create_group(users, topic='小白屋')
                msg.reply('{}已经找到，去"小白屋"里聊天吧。'.format(friend_name))
                group.add_members(msg.sender, use_invitation=True)
                group.add_members(search_friend, use_invitation=True)
                group.send('Bingo!')
            except:
                return "{}还不是我的好友呢？".format(friend_name)
            
        elif msg.text[:2] == '查找' and msg.text[2:]:
            return '查找公众号功能暂未上线'
            
        elif msg.text == '帮助':
            return help_info
        
        else:
            tuling.do_reply(msg)
    else:
        pass
        
bot.start(block=True)