import datetime
'''x = datetime.datetime.now()
today = datetime.date.today()
print(x)
print(today)
print(x.strftime("%X"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%Y"))'''

'''x = datetime.datetime.now()
month = int(input('What is your birthday month?'))
current = int(x.strftime("%m"))
monthsAway = str((abs((current - month) - 12)) - 1)
daysAway = str(30 - (int(x.strftime("%d"))))
print("You have " + monthsAway + " months and " + daysAway + " days until it's your birthday month!")'''

x = datetime.date.today()
days = str(int(x.strftime("%d")))
months = str(int(x.strftime("%m")))
print("It has been " + months + " months and " + days + " days since your New Years resolution. How are you doing?")
