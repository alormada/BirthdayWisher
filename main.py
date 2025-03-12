import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
day = now.day
month = now.month

my_email = "example@gmail.com"
password = "password"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
today_birthday = data[(data["day"] == day) & (data["month"] == month)]
birthday_people = [name for name in today_birthday.name]

for person in birthday_people:
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt", mode="r") as letter_file:
        temp_letter = letter_file.read()
        temp_letter = temp_letter.replace("[NAME]", f"{person}")
        address = today_birthday[today_birthday.name == person].email.iloc[0]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=address,
                                msg=f"Subject:Happy birthday!\n\n{temp_letter}"
                                )
            connection.close()
        temp_letter = temp_letter.replace(f"{person}", "[NAME]")



