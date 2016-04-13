import telepot
import sys
import time
import pprint
import random
from random import randint 

#credit for the skeleton for this code and the framework it is based off of: https://github.com/nickoala/telepot
#telepot is pretty cool, check it out.

#This is the first rough draft code for the stupid bot I have made.

TOKEN = 'Your Token Here' #It would be better to take this as an arguement. 

bot = telepot.Bot(TOKEN)

#bot.getUpdates()

def handle(msg):
	
	Tupac = open('2pac.jpg', 'rb')
	
	pprint.pprint(msg)
	chatid = msg['chat']['id']
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	if(content_type == 'text'):
		
		text = msg['text'].lower()
		
		if(text == '/memes'):
			x = random.randint(1,138) #there are 138 pictures in the folder,named 1.png to 138.png that it chooses from at random.
			pic = str(x) + '.png'
			y = open(pic, 'rb')
			bot.sendPhoto(chatid, y)
			
			
		elif (text.find('weed') != -1 or text.find('420') != -1 or text == '/weed'):
			bot.sendMessage(chatid, " Get on the roof, let's get smoked out and blaze with me.")
			bot.sendPhoto(chatid, Tupac)
			
		elif (text.find('harry') != -1 and (text.find('stupid') != -1 or text.find('dumb') != -1 or text.find('fucker') != -1)):
			bot.sendMessage(chatid, "Why don't you make like a tree and fuck off, fucker!")
			
		elif (text.find('vape') != -1):
			bot.sendSticker(chatid, 'BQADBAADbgADqpW-A-5eRYGeubOIAg')
			
		elif (text == '/suggest'):
			bot.sendMessage(chatid, 'https://github.com/HarrySaqs/BasicBitchBot/issues')
			
		elif (text == '/tits'):
			y = open('CornPorn.png', 'rb')
			bot.sendPhoto(chatid, y)
			
			
#	elif(content_type == 'sticker'):
	#	bot.sendSticker(chatid, msg['sticker']['file_id'])
	#	bot.sendMessage(chatid, 'nice sticker nerd')
		
	
	
bot.notifyOnMessage(handle)



while 1:
	time.sleep(10)
	
	
