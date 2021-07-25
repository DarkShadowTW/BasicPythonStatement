import datetime

#original format
print(datetime.datetime.now())   #2021-07-25 11:23:38.132341

#format date time
datetime_now = datetime.datetime.today()                        # 獲得當地時間
datetime_now_str = datetime_now.strftime("%Y/%m/%d %H:%M:%S")    # 格式化日期
print(datetime_now_str)

#建議可縮減 import 的語法
from datetime import datetime as dt

print(dt.now())

datetime_now = dt.today()
datetime_now_str = datetime_now.strftime("%Y/%m/%d %H:%M:%S")
print(datetime_now_str)