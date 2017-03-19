#! python3
# -*- coding:utf-8 -*-
from wxpy import *

bot = Bot()

#向与自己说话的好友，以及当群聊中有人@自己时，发送一张保存在本地的图片
@bot.register([Friend, Group], TEXT)
def auto_reply(msg):
        if not (isinstance(msg.sender, Group) and not msg.is_at):
            #回复一张保存在本地文件夹的图片
            msg.reply_image('12 Mozart.jpg')
            
bot.start()  

