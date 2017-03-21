#! python3
# -*- coding:utf-8 -*-
from wxpy import *
from kidwechat_reply_text import reply_text


bot = Bot(cache_path=True)

@bot.register(msg_types='Text')
def reply(msg):
    reply = reply_text(msg)
    return reply
        
@bot.register([Group],TEXT)
def reply(msg):
    if isinstance(msg.sender, Group) and msg.is_at:
        Tuling(api_key=KEY).do_reply(msg)
        
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = bot.accept_friend(msg.card)
    reply = '我是TuTu，输入"帮助"了解我吧。'
    new_friend.send(reply)

bot.start(block=True)