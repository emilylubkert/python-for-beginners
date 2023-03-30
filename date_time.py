from datetime import datetime, timedelta

today = datetime.now()
print("today is: " + str(today))

#timedelta
one_day = timedelta(days=1)
yesterday = today - one_day
print("yesterday was: " + str(yesterday))

current_date = datetime.now()
print('Day: ' + str(current_date.day))

birthday = input("When is your birthday? (dd/mm/yyyy)")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print("Birthday: " + str(birthday_date))