import telepot
import sys
import time
import pprint
import random
from random import randint 

#credit for the skeleton for this code and the framework it is based off of: https://github.com/nickoala/telepot
#telepot is pretty cool, check it out.

#This is the first rough draft code for the stupid bot I have made.

TOKEN = 'Your Token Here' #It would be better to take this as an arguement when you call the script, rather than hardcoding it in. 

bot = telepot.Bot(TOKEN)

#bot.getUpdates()

def handle(msg):
	
	Tupac = open('2pac.jpg', 'rb')
	
	pprint.pprint(msg)
	
	#lets me know if the message is a pciture or sticker or text, etc. whether the chat is a group or private or channel
	#and gives me the id of teh chat so the bot can respond.
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	if(content_type == 'text'):
		
		text = msg['text'].lower() #puts the message in lowercase so I don't have to test for uppercase versions of words.
		
		if(text == '/memes'):
			x = random.randint(1,138) #there are 138 pictures in the folder,named 1.png to 138.png that it chooses from at random.
			pic = str(x) + '.png'
			y = open(pic, 'rb')
			bot.sendPhoto(chat_id, y)
			
			
		elif (text.find('weed') != -1 or text.find('420') != -1 or text == '/weed'):
			bot.sendMessage(chatid, " Get on the roof, let's get smoked out and blaze with me.")
			bot.sendPhoto(chat_id, Tupac)
			
		elif (text.find('harry') != -1 and (text.find('stupid') != -1 or text.find('dumb') != -1 or text.find('fucker') != -1)):
			bot.sendMessage(chat_id, "Why don't you make like a tree and fuck off, fucker!")
			
		elif (text.find('vape') != -1):
			bot.sendSticker(chat_id, 'BQADBAADbgADqpW-A-5eRYGeubOIAg')
			
		elif (text == '/suggest'):
			bot.sendMessage(chat_id, 'https://github.com/HarrySaqs/BasicBitchBot/issues')
			
		elif (text == '/tits'):
			y = open('CornPorn.png', 'rb')
			bot.sendPhoto(chat_id, y)
			
			
#	elif(content_type == 'sticker'):
	#	bot.sendSticker(chat_id, msg['sticker']['file_id'])
	#	bot.sendMessage(chat_id, 'nice sticker nerd')
		
	
	
bot.notifyOnMessage(handle)



while 1:
	time.sleep(10)
	
	
