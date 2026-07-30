import os
from uwuzu import Uwuzu

DOMAIN = os.environ["UWUZU_DOMAIN"]
TOKEN = os.environ["UWUZU_TOKEN"]

client = Uwuzu(DOMAIN, TOKEN)

me = client.get_me()

print("BOT:", me["userid"])
print("フォロワー数:", me["follower_cnt"])

print("フォロワー一覧:")
for f in me["follower"]:
    print("-", f)
