from datetime import datetime
from datetime import timedelta

today = datetime.strptime(input(), '%Y %m %d')
print(datetime.strftime(today, '%m/%d/%Y'))

tomorrow = today + timedelta(days=1)
print(datetime.strftime(tomorrow, '%m/%d/%Y'))

