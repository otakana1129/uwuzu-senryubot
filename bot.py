import os
from uwuzu import Uwuzu

DOMAIN = os.environ["UWUZU_DOMAIN"]
TOKEN = os.environ["UWUZU_TOKEN"]

client = Uwuzu(DOMAIN, TOKEN)

print("BOT START")

try:
    me = client.get_me()
    print("ログイン成功")
    print(me)

except Exception as e:
    print("ログイン失敗")
    print(e)

print("BOT END")
