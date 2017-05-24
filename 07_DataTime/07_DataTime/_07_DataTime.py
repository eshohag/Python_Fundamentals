import datetime;

dateString=datetime.date.today();
print(dateString);
print(dateString.year);
print(dateString.month);
print(dateString.day);

#Using Strftime()
print(dateString.strftime('%d %b %y'))
print(dateString.strftime('%d %B %Y'))
print(dateString.strftime('%D'))
print(dateString.strftime('%D %b %y'))

#Using Strptime()
userInput=input("What is your BirthDay (mm-dd-yy)?\n");
birthDay=datetime.datetime.strptime(userInput,'%m-%d-%Y').date();
print(birthDay);

days=dateString-birthDay;
print("Total Days={}".format(days));

