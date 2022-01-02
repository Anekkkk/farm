import datetime 
import time
from keep_alive import keep_alive
import os
from replit import tkn
from essential_generators import DocumentGenerator
import random
import discum     
gen = DocumentGenerator()
keep_alive()

i = 


rawchannel = [
"927091635593027595",
"927091647332905010",
"927091653729206283",
"927091664567296000",
"927091671685013576",
"927091696481746985",
"927091706560663603",
"927091719726575636",
"927091734939320331"]
bot = discum.Client(token= tkn[i], log={"console":True, "file":False})
bot.sendMessage(str(927091635593027595), "Hello :)")

global dmcs
dmcs = True
while dmcs:
      list = [11,19,3]
      
      if int(datetime.datetime.now().hour) in list:
        for _ in range(4):
          channel = random.choice(rawchannel)
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
            channel = random.choice(rawchannel)
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
        channelx = random.choice(rawchannel)

        for _ in range(15):
          bot.sendMessage(channelx, gen.sentence())
          time.sleep(int(random.randrange(35, 55)))
        time.sleep(1000)

keep_alive()
bot.gateway.run(auto_reconnect=True)
