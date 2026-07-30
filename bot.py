import os
from uwuzu import Uwuzu

print("BOT START")

DOMAIN = os.environ["UWUZU_DOMAIN"]
TOKEN = os.environ["UWUZU_TOKEN"]

client = Uwuzu(DOMAIN, TOKEN)

try:
    timeline = client.get_timeline(limit=5)

    print("件数:", len(timeline))

    for post in timeline:
        print("投稿発見")
        try:
            print(post.text_content)
        except Exception as e:
            print("投稿表示エラー:", e)

except Exception as e:
    print("エラー発生:", e)

print("BOT END")
