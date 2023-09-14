import datetime

# 현재 날짜
now = datetime.date.today()
print(now)
print(now.year)
print(now.month)
print(now.day)

# 지정된 날짜
date = datetime.date(2023, 12, 4)
print(date)

# 현재 시간
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# 지정된 시간
date = datetime.datetime(2023, 12, 4, 12, 00, 00)
print(date)
