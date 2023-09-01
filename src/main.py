import time
from email_module import sendEmail
from ping_module import pingPC
import os

hostIP = os.getenv("HOST_IP")

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

subject = 'PC is closed!'
body = 'Pinging the PC doesn\'t return a response!'

while True:
    try:
        if not pingPC(hostIP):
            sendEmail(email_sender, email_password, email_receiver, subject, body)
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(1)


