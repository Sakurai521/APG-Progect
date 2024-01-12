import datetime

next_day = datetime.timedelta(days=1, hours=2)
today = datetime.datetime.now()
diff_days = today + next_day

print(diff_days)

print(datetime.datetime.now(datetime.timezone.utc))
print(datetime.timedelta(seconds=10).seconds)

print(datetime.datetime.now() + datetime.timedelta(seconds=10))