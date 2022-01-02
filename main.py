import datetime 
import time
from keep_alive import keep_alive
import os
from essential_generators import DocumentGenerator
import random
import discum     
gen = DocumentGenerator()
bot = discum.Client(token=os.getenv("TOKEN"), log={"console":True, "file":False})

keep_alive()

channel = "882262153606860890"

bot.sendMessage(channel, "Hello :)")

global dmcs
dmcs = True
while dmcs:
      list = [11,19,3]
      
      if int(datetime.datetime.now().hour) in list:
        bot.sendMessage(channel, '!stop')
        time.sleep(5)
        bot.sendMessage(channel, 'owo daily')
        time.sleep(5)
        bot.sendMessage(channel, 'owo q')
        time.sleep(5)
        bot.sendMessage(channel, 'owo q rr 3')
        for _ in range(4):
          bot.sendMessage(channel, 'owo lb all')  
          time.sleep(19)   
          bot.sendMessage(channel, 'owo use 57 71 78')
          time.sleep(19)
          bot.sendMessage(channel, 'owo use 56 70 77')
          time.sleep(23)
          bot.sendMessage(channel, 'owo use 55 69 76')
          time.sleep(20)
          bot.sendMessage(channel, 'owo use 54 68 75')
          time.sleep(20)
          bot.sendMessage(channel, 'owo use 53 67 74')
          time.sleep(16)
          bot.sendMessage(channel, 'owo use 52 66 73')
          time.sleep(20)
          bot.sendMessage(channel, 'owo use 51 65 72')
          time.sleep(20)

          for _ in range(9):
            bot.sendMessage(channel, 'owoh')
            time.sleep(int(random.randrange(10, 20)))
            bot.sendMessage(channel, 'pls beg')
            bot.sendMessage(channel, 'owo sell all')
            time.sleep(int(random.randrange(1, 20)))
            bot.sendMessage(channel, 'owo cash')
            time.sleep(int(random.randrange(10, 20)))
            bot.sendMessage(channel, 'owoh')
            time.sleep(int(random.randrange(10, 20)))
            bot.sendMessage(channel, 'pls beg')
            bot.sendMessage(channel, 'owo sell all')
            time.sleep(int(random.randrange(10, 20)))
            bot.sendMessage(channel, 'owo cash')
            time.sleep(int(random.randrange(10, 20)))
          time.sleep(int(random.randrange(600, 1200)))
      
      else: 
        channel1 = "897809000236732416"
        channel2 = "897809009833283584"
        channel3 = "897809018351935538"
        channel4 = "897809026652438548"
        channel5 = "897809042284642334"
        channel6 = "897809053672149013"
        channel7 = "897809066703872080"
        channel8 = "897809077571293214"
        channel9 = "897809087255957565"
        channel10 ="897809095619379260"
        list1 = [channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8, channel9, channel10]

        channelx = random.choice(list1)

        for _ in range(15):
          bot.sendMessage(channelx, gen.sentence())
          time.sleep(int(random.randrange(35, 55)))
        time.sleep(1000)

keep_alive()
bot.gateway.run(auto_reconnect=True)
