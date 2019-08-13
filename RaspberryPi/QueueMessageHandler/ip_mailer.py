import smtplib
from email.mime.text import MIMEText
import datetime
import subprocess
import appSettings as settings


def send_ip():
    ip = subprocess.check_output(['hostname', '-I'])
    to = settings.TO_EMAIL_ADDRESS
    gmail_user = settings.FROM_EMAIL_ADDREESS
    gmail_password = settings.EMAIL_PASSWORD

    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)

    today = datetime.date.today()
    my_msg = '%s' % today.strftime('%b %d %Y')
    msg = MIMEText(my_msg)
    msg['Subject'] = 'Raspberry Pi IP: %s' % ip[:-2].decode("UTF-8")
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
