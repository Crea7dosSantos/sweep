from pytz import timezone
from datetime import datetime


class Todo(object):
    def __init__(self, id, time):
        self.id = id
        self.time = time


todos = [
    Todo(1, datetime.now(timezone('UTC'))),
    Todo(2, datetime.now(timezone('UTC')))
]
print(todos[0].time)
print(datetime.utcnow().tzinfo)
hoge = datetime.utcnow()
print(hoge.replace(tzinfo=timezone.utc))

for todo in todos:
    todo.time = todo.time.astimezone(timezone('Asia/Tokyo'))
    print(todo.time)

# import pytz
# from datetime import datetime
# 定数を定義(1535763600 = September 1, 2018 1:00:00 AM UTC)
EPOCH = 1535763600
# timezoneを定義
UTC = timezone('UTC')
JST = timezone('Asia/Tokyo')
# epoch timeの読み込み
utc_time_naive = datetime.utcfromtimestamp(EPOCH)
# epoch timeにUTCのタイムゾーン情報を付与
utc_time_aware = UTC.localize(utc_time_naive)
# JSTのタイムゾーンへ変換
jst_time_aware = utc_time_aware.astimezone(JST)

print(jst_time_aware)
