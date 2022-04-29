import random
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


class Mail:
    def __init__(self):
        self.email = None
        self.name = None
        self.MY_ADDRESS = 'techeye177@gmail.com'
        self.PASSWORD = 'abcDEF*123'

    def auth_mail(self, email, name):
        self.email = email
        self.name = name
        n = random.randint(500, 5000)
        m = n
        message_template = read_template('auth_template.txt')
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(self.MY_ADDRESS, self.PASSWORD)
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=self.name, NUMBER=n)
        msg['From'] = self.MY_ADDRESS
        msg['To'] = self.email
        msg['Subject'] = "Mail Verification"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
        s.quit()
        return m


if __name__ == '__main__':
    m = Mail()
    m.auth_mail('dipchakraborty71@gmail.com', 'dip')
