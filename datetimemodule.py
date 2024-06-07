import datetime

dt=datetime.datetime.now()
#print(dt,type(dt))
#print(dt)


dt1=datetime.datetime(2023,3,1,12,50,30,29)

print(dt1)
print(dt1.hour)
print(dt1.min)
print(dt1.second)
print(dt1.microsecond)


date=datetime.date.today()
print(date.month)
print(date.year)
print(date.day)

date_after_5days=dt+datetime.timedelta(days=5)
print("date after 5 days:",date_after_5days)

date_after_5days_3weeks=dt+datetime.timedelta(days=5,weeks=3)
print("date after 5 days and 3 weeks:",date_after_5days_3weeks)










