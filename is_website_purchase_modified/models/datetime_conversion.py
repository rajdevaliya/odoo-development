import pytz
from datetime import datetime, time
from pytz import timezone, UTC

user_input = "2023-01-30 10:00 AM"
local_tz = pytz.timezone('Asia/Calcutta')
print(local_tz)
local_time = datetime.strptime(user_input, "%Y-%m-%d %I:%M %p")
# local_time = local_tz.localize(local_time, is_dst=None)
# utc_time = local_time.astimezone(pytz.utc)
# print(utc_time)
# print(datetime.now().utcnow())
# new = local_tz.normalize(pytz.utc.localize(local_time))
# print(new)
# x = pytz.utc.localize(local_time).astimezone(local_tz)
# print(x)
# print(local_time.replace(tzinfo=timezone.utc))

# local to utc?

# new = timezone('Asia/Calcutta').localize(local_time).astimezone(UTC).replace(tzinfo=None)
# print(new)

print(pytz.utc.localize(local_time).astimezone(local_tz).replace(tzinfo=None))