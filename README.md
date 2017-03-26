![小头像](https://github.com/hunshiouren/KidWeChat/blob/master/resources/%E5%B0%8F%E5%A4%B4%E5%83%8F.png)   
# KidWeChat Assistant 儿童微信助手 #  

基于Python，帮助家长管理儿童微信好友及公众号并可以和儿童自主交互的微信机器人


**具体来说：**  

- 目前，儿童使用家长的微信与好友联系，但是家长联系人太多，不方便儿童寻找到好友。  

- 家长添加微信助手为好友后，在微信助手交互界面：  

	- 通过添加命令，将儿童好友及公众号添加至微信助手后台。 
 
- 儿童通过与微信助手交互：  

	- 可查找父母筛选过的好友及公众号；  
	- 并且儿童还可与微信助手自主聊天。

   ![功能展示0](https://github.com/hunshiouren/KidWeChat/blob/master/resources/%E5%8A%9F%E8%83%BD%E6%BC%94%E7%A4%BA0.png)  ![功能展示1](https://github.com/hunshiouren/KidWeChat/blob/master/resources/%E5%8A%9F%E8%83%BD%E6%BC%94%E7%A4%BA1.png)

**轻松运行:**  

- 运行环境：  
Python 3.6  
wxpy==0.2.6   
Flask-SQLAlchemy==2.1  
Daocloud服务器(可选) 

**简单上手:**

- 将仓库clone至本地，命令行界面运行kidwechat_reply.py, 此时电脑桌面会出现微信二维码图片，手机微信扫描二维码登录。登录成功说明已经将自己的微信号部署为微信助手。  
- 也可将仓库部署到Daocloud中（可选）。


**微信助手使用:**   

- 用另外一个微信帐号与部署成功的微信帐号交互：  

	0. 发送"帮助"，获取帮助文档；  
	1. 发送"添加xx"，向微信号'xx'发送好友请求；  
	2. 发送公众号名片，添加公众号存储二维码；  
	3. 发送"寻找xx"，寻找好友并创建群聊；  
	4. 发送"查找xx"，查找公众号并返回二维码；  
	5. 输入其他，开启自动聊天模式。

- 注：有的微信号部署成功后不能返回正常的信息，如果出现此种情况，请尝试换个微信号部署。  


**试用一下：**  
- 扫描下图二维码，来与微信助手交互吧。  
  （仅限项目演示阶段，后续请勿扫描） 
 
![TuTu](https://github.com/hunshiouren/KidWeChat/blob/master/resources/%E5%B0%8F%E4%BA%8C%E7%BB%B4%E7%A0%81.png)


**Change Log**  

  v1.0(2017/03/26)  

   - 初始上线