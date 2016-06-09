name = input("Name: ")
age = int(input("Age: "))

import datetime
year = datetime.datetime.now().year - age + 100

print("Dear {}, you should turn 100 in the year {}.".format(name, year))
