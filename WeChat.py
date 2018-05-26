import os
import itchat

myTxt = "嗨！我是卡卡马桶的微信小号秋刀鱼君^_^，功能还未完善，有事请联系15067128015"
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	return myTxt

itchat.auto_login(enableCmdQR=2)
itchat.run()
