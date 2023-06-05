"""
--------------------------------------------------
-------------------- DateTime --------------------
--------------------------------------------------

The today() function returns the date of the current day.
The fromordinal() function returns the date corresponding to the day passed to it.
The fromisoformat() function returns the date corresponding to the string passed to it in YYYY-MM-DD format.

The now() method returns the current date and time.
The today() method returns the current date and time, with tzinfo as None.


For more information:
https://wiki.hsoub.com/Python/datetime

time:
https://wiki.hsoub.com/Python/datetime/time

DateTime:
https://wiki.hsoub.com/Python/datetime/datetime

TimeDelta:
https://wiki.hsoub.com/Python/datetime/timedelta
"""


from datetime import timedelta
from datetime import datetime
from datetime import time
from datetime import date
print('-'*50)
print(' DateTime '.center(50, '-'))
print('-'*50)
#
#
#
#
#
# Date
world_club = date(2022, 11, 21)


print(world_club)
today = date.today()
print(today)


some_day = date.fromordinal(738480)
print(some_day)

# frimisoformat("year-mounth,day")
another_day = date.fromisoformat('2022-11-21')
print(another_day)

days_to_world_club = world_club - today
print(days_to_world_club)

print(type(days_to_world_club))

print(today > world_club)
print(world_club.isoformat())
#
#
#
#
#
# Time

time1 = time()

print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)

time2 = time(hour=18, minute=24, second=55)
print(time2)
print(time2.hour)
print(time2.minute)
print(time2.second)
# fromisoformat('HH:MM:SS')
time3 = time.fromisoformat('18:26:55')

print(time3)
#
#
#
# DateTime

world_club_2022 = datetime(year=2022, month=11, day=21,
                           hour=13, minute=0, second=0)
print(world_club_2022)
print(world_club_2022.year)
print(world_club_2022.month)
print(world_club_2022.day)
print(world_club_2022.hour)
print(world_club_2022.minute)
print(world_club_2022.second)

now = datetime.now()
print(now)

today = datetime.today()
print(today)

# fromisoformat("year-month-day HH:MM:SS")

world_club_2022 = datetime.fromisoformat('2022-11-21 13:00:00')
print(world_club)

count_town = now - world_club_2022
print(f'Count town: {count_town}')

#
#
#
#
#
#
#
# timedelta

delta = timedelta(days=20, seconds=39, minutes=55, hours=4, weeks=3)
print(delta)

now = datetime.now()

print(now - delta)
print(now.strftime('%A, %d/%B/%Y'))
