# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname('__file__'))#不在 shell 中时把‘’删除
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MpsData(db.Model):
    """
    创建表格，如表格已创建则读取表格为 MpsData
    第一列 mp：公众号名称
    第二列 user：添加发送信息的用户（写入 str(msg.chat.name），以防不同用户间产生冲突
    第三列 qr_code：二维码图片文件名（修改，因为和其它文件变量名重复）
    """
    __tablename__ = 'weather_data'
    id = db.Column(db.Integer, primary_key = True)
    mp = db.Column(db.String, index=True)
    user = db.Column(db.String)
    qr_code = db.Column(db.String)

    def __init__(self, mp, user, qr_code):
        self.mp = mp
        self.user = user
        self.qr_code = qr_code

    def __repr__(self):
        return '<MpsData %r>' % self.mp

class DataOperating:
    """
    数据操作，修改表格数据
    引入：from kidwechat_sql import DataOperating
    add_data：添加数据（添加数据前需先 confirm_mp，若反馈 != None，添加才会成功）
    search_img：搜索二维码图片，反馈文件名
    confirm_mp：确定用户的公众号是否已存储数据，若无则反馈 None
    change_img：修改二维码图片名称
    """
    def add_data(mp, user):      #鸡腿儿：是否需要img？ Ollie: 不需要，改成图片文件名
        add_mp = MpsData(mp, user, '12_Mozart.jpg') # 添加 莫扎特图片
        db.session.add(add_mp)
        db.session.commit()

    def search_img(mp, user):   #鸡腿儿：此函数用来返回图片。
        data = MpsData.query.filter_by(mp=mp, user=user).first()
        return data.qr_code

    def confirm_mp(mp, user):
        data = MpsData.query.filter_by(mp=mp, user=user).first()
        return data #若 公众号＋user 不存在数据库中，则返回 None

    def change_img(mp, user, qr_code):#此处 img 为更改后的图片文件名   #鸡腿儿：此函数目前只是摆摆样子，证明我们有此功能：）
        data = MpsData.query.filter_by(mp=mp, user=user).first()
        #del_file = data.qr_code
        data.qr_code = qr_code
        db.session.add(data)
        db.session.commit()
        #os.remove(del_file)

db.create_all()#创建链接：表格与 MpsData
