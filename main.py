
import os
from webserver import keep_alive
import requests
import time
import random

keep_alive()

# rifle,fishing rod,shovel 
TOKENS = [os.environ['TOKEN1'],os.environ['TOKEN2'],os.environ['TOKEN3'],os.environ['TOKEN4'],os.environ['TOKEN5']]
COINS = ['beg','hunt','fish','dig']
print('Bot Started')
USER = os.environ['USER']
TRADE = ['horseshoe','lifesaver','candy','alc','spinner','padlock','tidepod']
SELL = ['ant','cookie','corncob','corndog','potato','skunk','rabbit','duck','deer','boar','dragon','seaweed','fish','rarefish','exoticfish','jellyfish','legendaryfish','kraken','junk','garbage','trash','worm','ladybug','stickbug','spider','coinbomb','laptop','padlock','landmine','sand','bread']
CHANNEL = os.environ['CHANNEL']
# while 1:
def kno():
  for token in TOKENS:
        header = {
                'authorization': token
            }   

        payload = {
            'content': f"pls trade 1 kno , 1 coin {USER}"
        }
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'
        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(10)
def sell():
    for x in SELL:
        
        
      for token in TOKENS:
        header = {
                'authorization': token
            }   

        payload = {
            'content': f"pls sell {x} all"
        }
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'
        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(2)
        
        

def gift():
  
  for x in TRADE:
    for token in TOKENS:
        header = {
                'authorization': token
            }
        # for x in TRADE:
            
            
        
        payload = {
            'content': f"pls gift 1 {x} {USER}"
        }
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'
        r = requests.post(
        url, data=payload, headers=header)

        
        payload = {
            'content': f"pls give {USER} 100k"
        }
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'
        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(3)



def tide():
    for token in TOKENS:
        header = {
            'authorization': token
        }

        
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'

        payload = {
            'content': "pls buy tide"
        }
        

        r = requests.post(
        url, data=payload, headers=header)
        time.sleep(4)


def buy():
    for token in TOKENS:
        header = {
            'authorization': token
        }

        
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'

        payload = {
            'content': "pls buy fishingpole"
        }
        

        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(randomgen(7, 13))
        payload = {
            'content': "pls buy rifle"
        }

        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(randomgen(7, 13))
        payload = {
            'content': "pls buy shovel"
        }

        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(randomgen(7, 13))


def start():
    for token in TOKENS:
        header = {
            'authorization': token
        }

        
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'

        payload = {
            'content': "pls use tide"
        }
        

        r = requests.post(
        url, data=payload, headers=header)

        time.sleep(2)


def coins():
  for command in COINS:
    for token in TOKENS:
        header = {
            'authorization': token
        }

        
        url = f'https://discord.com/api/v9/channels/{CHANNEL}/messages'

        payload = {
            'content': f"pls {command}"
        }

        r = requests.post(
        url, data=payload, headers=header)
        time.sleep(randomgen(3,5))
    time.sleep(randomgen(2,4))
        




def randomgen(num1, num2):
    return random.randint(num1, num2)

if __name__=='__main__':
    i = 0
    
    while True:
        
        x = 1
        for x in range(1,51):
            coins()
            print(x)
            x+=1
        # kno()
        
        sell()
        buy()
        gift()
        
        i += 1
        print('Cycle Completed: ', i)
   
        time.sleep(randomgen(55, 100))
 
        
    
