from wxpy import *

from kidwechat_sql_tuier import DataOperating

bot = Bot(cache_path=True)

KEY = '33768ec646c245528f9c86a429c4d564'
HELP = """
发送公众号名片，可将公众号加入小盆友的阅读架中
输入"查找xx"，查找公众号并返回二维码
输入其他，开启自动聊天模式"""


tuling = Tuling(api_key = KEY)

dic_mp_name = {} #存储用户名称和公众号名称的字典
dic_mp_qrcode = {} #存储公众号名称和二维码的字典

mozart = '12_Mozart.jpg'  #暂时以莫扎特代替 24小时审核公众号图

#第一步: 用户发来公众号卡片，将用户名key：sender和value：公众号名称存储为字典
#@bot.register([Friend], msg_types = CARD)
def friend_send_mp(msg):
    global dic_mp_name, dic_mp_qrcode
    #写入两个字典中
    dic_mp_name[msg.chat.name] = msg.card.name
    dic_mp_qrcode[msg.card.name] = mozart
    #print (msg.chat.name)
    #print (dic[msg.chat.name])

    #先查找公众号，如果为空值，则调用add函数，并显示莫扎特
    if DataOperating.confirm_mp(dic_mp_name[msg.chat.name], msg.chat.name) == None:
        #此时，需将mp，user,img写入数据库
        DataOperating.add_data(dic_mp_name[msg.chat.name], msg.chat.name)
        msg.reply ('%s 发送了名片 %s' % (msg.chat.name, dic_mp_name[msg.chat.name]))
        msg.reply_image(mozart)
        #测试是否写入字典
        #若不为空值，则说明该用户已经添加过此公众号，直接调用search函数显示公众号二维码
    else:
        image = DataOperating.search_img(dic_mp_name[msg.chat.name], msg.chat.name)
        msg.sender.send_image(image)


#第二步：用户查找公众号名称，返回图片
#@bot.register([Friend], msg_types = TEXT)
def friend_query_mp(msg):
    request_head = msg.text[:2]
    request_body = msg.text[2:]
    if request_head == '查找' and request_body:
        #查找数据库，如果已添加此公众号，则返回图片(默认返回莫扎特，手动添加二维码后返回二维码）)

        image = DataOperating.search_img(request_body, msg.chat.name)
        msg.sender.send_image(image)
    else:
        tuling.do_reply(msg)

#群聊，调戏机器人
#@bot.register([Group],TEXT)
def reply(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        tuling(api_key=KEY).do_reply(msg)
