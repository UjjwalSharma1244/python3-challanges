import datetime

name=input("enter your name")
age=int(input("please enter your age"))

s=datetime.datetime.now()
u=95-age
print("you will be 95 year old by this year", u+s.year)
