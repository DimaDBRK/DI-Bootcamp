# Daily Challenge GOLD : Happy Birthday
#
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
#
# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
#
# Bonus : If they were born on a leap year, display two cakes !


from datetime import date
user_birthday = input("birthdate (in format DD/MM/YYYY): ")
print(user_birthday)
user_birthday_year = int(user_birthday[-4:])
user_birthday_month = int(user_birthday[3:4])
user_birthday_month = int(user_birthday[0:2])
# change format to dd/mm/YY
# day_today = date.today().strftime("%d/%m/%Y")
today = date.today()

if today.month < user_birthday_month or (today.month == user_birthday_month and today.day < user_birthday_day):
    age = today.year - user_birthday_year - 1
else:
    age = today.year - user_birthday_year

first_string = "        ___________"

if age != 0:
    qty = age % 10
    if qty == 0: qty = 10
    for i in range(qty):
        first_string = first_string[:(8+int((12-qty)/2)+i)] + 'i' + first_string[(8+int((12-qty)/2)+i+1):]


print(f"{first_string}\n       |:H:a:p:p:y:|\n     __|___________|__\n    |^^^^^^^^^^^^^^^^^|\n    |:B:i:r:t:h:d:a:y:|\n    |                 |\n    ~~~~~~~~~~~~~~~~~~~")
if user_birthday_year % 4 == 0:
    print(f"{first_string}\n       |:H:a:p:p:y:|\n     __|___________|__\n    |^^^^^^^^^^^^^^^^^|\n    |:B:i:r:t:h:d:a:y:|\n    |                 |\n    ~~~~~~~~~~~~~~~~~~~")