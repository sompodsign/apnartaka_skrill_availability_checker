from smtplib import SMTP

from decouple import config


def send_mail(message):
    """sends email to address"""
    try:
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(config('sender_email'), config('sender_password'))

        server.sendmail(config('sender_email'), config('to_email'), message)
        server.close()
    except Exception as e:
        print("Error {}".format(e))
