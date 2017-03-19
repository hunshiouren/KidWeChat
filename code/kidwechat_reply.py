#! python3
# -*- coding:utf-8 -*-
from wxpy import *


bot = Bot(cache_path=True)
KEY = '042c8822f369426aa4ff5396880c84ad'
HELP = """
    输入"帮助"，获取帮助文档
    输入"寻找xx"，则寻找好友并创建群聊
    输入"查找xx"，则查找公众号并返回二维码
    输入"添加xx"，则向微信号'xx'发送好友请求
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
            reply = """
                {}还不是我的好友呢？                推荐图图给他;或发送"添加xx",将他添加为图图的好友（仅支持微信号哦~）""".format(friend_name)

        msg.reply(reply)      
        
    elif msg.text[:2] == '查找' and msg.text[2:]:
        msg.reply('查找公众号功能暂未上线，请耐心等待哦。')
        
    elif msg.text[:2] == '添加' and msg.text[2:]:
        user_id = msg.text[2:]
        friend_name = msg.text[2:]
        verify_info = '{}派我来的。'.format(msg.sender) 
        bot.add_friend(user_id, verify_info)
        msg.reply('对{}的好友请求已经发送，请稍后寻找他哦。'.format(friend_name))
        
    elif msg.text == '帮助' and not msg.text[2:]:
        msg.reply(HELP)
     
    else:
        Tuling(api_key=KEY).do_reply(msg)
        
@bot.register([Group],TEXT)
def reply(msg):
    if isinstance(msg.sender, Group) and msg.is_at:
        Tuling(api_key=KEY).do_reply(msg)
        
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = bot.accept_friend(msg.card)
    new_friend.send('我是图图，输入"帮助"了解我吧。')

bot.start(block=True)