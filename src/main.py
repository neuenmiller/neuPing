import time
from email_module import sendEmail
from ping_module import pingPC

hostIP = "192.168.1.252"

email_sender = ''
email_password = ''
email_receiver = 'kansapat4921@gmail.com'

subject = 'PC is closed!'
body = 'Pinging the PC doesn\'t return a response!'

while True:
    try:
        if not pingPC(hostIP):
            sendEmail(email_sender, email_password, email_receiver, subject, body)
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(1)


