import smtplib 
from email.message import EmailMessage 
import ssl
import os

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

subject = 'PC is closed!'
body = 'Pinging the PC doesn\'t return a response!'



    
def sendEmail (email_sender, email_password, email_receiver, subject, body):
    em = EmailMessage ()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('gmail', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
