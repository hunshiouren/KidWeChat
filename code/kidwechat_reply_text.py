#! python3
# -*- coding:utf-8 -*-
from wxpy import *


bot = Bot(cache_path=True)

KEY = '042c8822f369426aa4ff5396880c84ad'
HELP = """输入"帮助"，获取帮助文档
输入"寻找xx"，寻找好友并创建群聊
输入"查找xx"，查找公众号并返回二维码
输入"添加xx"，向微信号'xx'发送好友请求
输入其他，开启自动聊天模式"""
NoFound = """{}还不是我的好友呢？
推荐TuTu给他;或发送"添加xx",将他添加为TuTu的好友（仅支持微信号哦~）"""
   
def reply_text(msg):  
    request_head = msg.text[:2] 
    request_body = msg.text[2:]
    if request_head == '寻找' and request_body:
        reply = request_friend(msg)
        msg.reply(reply)      
        
    elif request_head == '查找' and request_body:
        msg.reply('查找公众号功能暂未上线，请耐心等待哦。')
        
    elif request_head == '添加' and request_body:
        user_id = msg.text[2:]
        friend_name = msg.text[2:]
        verify_info = '{}派我来的。'.format(msg.sender) 
        bot.add_friend(user_id, verify_info)
        msg.reply('对{}的好友请求已经发送，请稍后寻找他哦。'.format(friend_name))
        
    elif msg.text == '帮助':
        msg.reply(HELP)
     
    elif '你的朋友验证请求' in msg.text:
        msg.reply('我是TuTu，输入"帮助"了解我吧。')
        
    else:
        Tuling(api_key=KEY).do_reply(msg)
        
def request_friend(msg):
    friend_name = msg.text[2:]
    search_friend = bot.friends().search(friend_name)
    if search_friend:
        try:
            search_friend = ensure_one(bot.friends().search(friend_name))
            users = [search_friend, msg.sender]
            group = bot.create_group(users, topic='小白屋')
            reply = '{}已经找到，去"小白屋"里聊天吧。'.format(friend_name)
            group.remove_members(search_friend)
            group.remove_members(msg.sender)
            group.add_members(msg.sender, use_invitation=True)
            group.add_members(search_friend, use_invitation=True)
        except:
            reply = '找到多个{}，重新寻找微信名或昵称试试吧。'.format(friend_name)
            
    else:
        reply = NoFound.format(friend_name)
        
    return reply