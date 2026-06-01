import os
import smtplib
import pandas
import datetime as dt
from pathlib import Path
from random import choice

MY_EMAIL = "kbbn2007@gmail.com"
MY_PASSWORD = "rtpa okkz wiid imgu"



# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("./birthdays.csv")
data_row = data.to_dict(orient="records")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

filtered_rows =  [row for row in data_row if row["month"] == current_month and row["day"] == current_day]

print(filtered_rows)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

def pick_random_file():
    folder_path = Path("./letter_templates")
    txt_files = list(folder_path.glob("*.txt"))
    random_file = choice(txt_files)
    return random_file

for row in filtered_rows:
    selected_file = pick_random_file()
    with open(selected_file, "r") as file:
        file_contents = file.read()

    recipient_name =  row["name"]
    recipient_email = row["email"]
    msg_body = file_contents.replace("[NAME]", recipient_name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg= f"Subject:Happy Birthday!\n\n{msg_body}"
        )
    print(msg_body)








