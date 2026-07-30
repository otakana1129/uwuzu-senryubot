print("開始")2 3timeline = client.get_timeline(limit=50)
print("timeline:", timeline)
print("件数:", len(timeline))
import os
from uwuzu import Uwuzu

DOMAIN = os.environ["UWUZU_DOMAIN"]
TOKEN = os.environ["UWUZU_TOKEN"]

client = Uwuzu(DOMAIN, TOKEN)

# 既に処理した投稿IDを保存
SEEN_FILE = "seen.txt"

if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r", encoding="utf-8") as f:
        seen = set(f.read().splitlines())
else:
    seen = set()


def is_senryu(text):
    """
    超簡易版

    本格運用なら Janome や SudachiPy で
    読み仮名を取得して 5-7-5 判定する。
    """

    if not text:
        return False

    lines = [x.strip() for x in text.split("\n") if x.strip()]

    # 3行川柳
    if len(lines) == 3:
        return (
            len(lines[0]) == 5 and
            len(lines[1]) == 7 and
            len(lines[2]) == 5
        )

    # 1行17文字川柳
    text = text.replace(" ", "").replace("　", "")
    return len(text) == 17


timeline = client.get_timeline(limit=50)

new_seen = set(seen)

for post in timeline:
print("ループ実行")3   
print(post.text_content)
    post_id = str(post.id)

    if post_id in seen:
        continue

    new_seen.add(post_id)

    text = post.text_content

    if is_senryu(text):
        try:
            post.reply(
                "🍵 川柳を検出しました！\n"
                "いい一句ですね。"
            )
            print("川柳発見:", text)

        except Exception as e:
            print(e)

with open(SEEN_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(new_seen))
timeline = client.get_timeline(limit=50)
print("BOT START")2 3timeline = client.get_timeline(limit=50)4 5print("timeline =", timeline)6print("件数 =", len(timeline))7 8for post in timeline:9    print("投稿発見")10    print(post)11 12print("BOT END")

print("取得件数:", len(timeline))

for post in timeline:
    print("投稿:", post.text_content)
