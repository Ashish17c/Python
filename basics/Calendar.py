import calendar

year  = int(input("Enter year:"))
month = int(input("Enter Month:"))

calendar = calendar.month(year,month)
print(calendar)