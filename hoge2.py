import datetime

dt_naive = datetime.datetime.utcnow()
print(dt_naive)
# 2018-12-31 05:00:30.001000

print(dt_naive.tzinfo)
# None

dt_naive_to_utc_replace = dt_naive.replace(tzinfo=datetime.timezone.utc)

print(dt_naive_to_utc_replace)
# 2018-12-31 05:00:30.001000+00:00

print(dt_naive_to_utc_replace.tzinfo)
# UTC
