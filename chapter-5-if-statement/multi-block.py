from ast import Str


age = 12;
price = 0;
if age < 4:
    price = 0
elif age < 18:
    price = 5;
elif age < 65:
    price = 10;
else:
    price = 5;

price("Your admission cost is $" + str(price) + ".")