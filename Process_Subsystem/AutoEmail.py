import smtplib
import schedule
import time

def send_email():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("shubhamborse0911@gmail.com", "cgxp qnya iogr hgpv")

    # message to be sent
    message = "An Automated Message from Shubham Borse"

    # sending the mail
    s.sendmail("shubhamborse0911@gmail.com", "borseshubhamsb@gmail.com", message)

    # terminating the session
    s.quit()

# Schedule the email sending every 10 seconds
schedule.every(2).seconds.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
