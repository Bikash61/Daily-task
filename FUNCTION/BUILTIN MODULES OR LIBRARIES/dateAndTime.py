import datetime
print(datetime.datetime.now())

print(datetime.datetime(2022,9,7,11,45,0))

print(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"))

date1 = datetime.datetime(2022,9,7,11,45,0)

date2 = datetime.datetime.now()

print(date2 - date1)

