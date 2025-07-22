import pandas as pd
import datetime
import smtplib
import os
from config import *

os.chdir(r"F:\Educational\Pycharm\Auto Birthday Wisher")
# os.mkdir("checking") 




def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    subject = f"Subject: {sub}\n"
    body = f"\n{msg}"
    # Concatenate subject and body, and encode using UTF-8
    email_content = (subject + body).encode('utf-8')
    # Establish SMTP connection
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # Login to the SMTP server using your app password
    s.login(GMAIL_ID, GMAIL_PASSWORD)
    # Send the email
    s.sendmail(GMAIL_ID, to, email_content)
    # Close the SMTP connection
    s.quit()

    

if __name__ == "__main__":
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(today, yearNow)

    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['BirthDay'].strftime("%d-%m")
        # print(bday) 
        if(today == bday) and yearNow not in str(item['Year']):
            print("🎉 Happy Birthday! 🎉", item['Name'],'!' ,item['Message']) 
            sendEmail(item['Email'], "🎉 Happy Birthday! 🎉", item['Message']) 
            writeInd.append(index)

    print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        print(df.loc[i, 'Year'])

    print(df) 
    df.to_excel('data.xlsx', index=False)   