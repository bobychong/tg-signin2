import os
import random
import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SESSION = os.environ['SESSION']
GROUP1 = os.environ['GROUP1']
GROUP2 = os.environ['GROUP2']

delay = random.randint(0, 5 * 3600)
print(f"随机等待 {delay//3600} 小时 {(delay%3600)//60} 分钟")
time.sleep(delay)

with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
    client.send_message(GROUP1, '/qd')
    print(f"{GROUP1} 签到成功！")
    
    time.sleep(random.randint(10, 60))
    
    client.send_message(GROUP2, '/sign')
    print(f"{GROUP2} 签到成功！")
