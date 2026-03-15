import smtplib
import pandas as pd
import datetime as dt
import random
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# the above is the app password, not google password
# This should be in the security settings of the account
df=pd.read_csv('birthdays.csv')
# print(df.head())
today=dt.datetime.now()
dd=today.day
mm=today.month
yy=today.year
print(dd,mm,yy)
filelist=['letter_1.txt','letter_2.txt','letter_3.txt']
for index,row in df.iterrows():
    if row['month']==mm and row['day']==dd:
        name=row['name']
        email=row['email']
        # randomfile = random.choice(filelist)
        randomfile='letter_'+str(random.randint(1,3))+'.txt'
        print(name)
        print(randomfile)
        file=open(randomfile)
        filecontent=file.read()
        modified=filecontent.replace('[NAME]', name)
        print(modified)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=fromemail,password=frompassword)

            connection.sendmail(from_addr=fromemail,
                                to_addrs='haribaskar.v@gmail.com',
                                msg=f'Subject:Happy Birthday\n\n {modified}')
