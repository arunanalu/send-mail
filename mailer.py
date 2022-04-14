import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Mailer:
    def __init__(self, from_email, from_password, emails_to_send):
        self.from_email = from_email
        self.from_password = from_password
        self.emails_to_send = emails_to_send

    def send_email(self, subject, message):
        body = f"Subject:{subject}\n\n{message}".encode('utf-8')
        with smtplib.SMTP(
            "smtp-mail.outlook.com", 587
        ) as server:
            server.ehlo()
            server.starttls()
            server.login(self.from_email, self.from_password)
            for email in self.emails_to_send:
              try:
                  server.sendmail(self.from_email, email, body)
              except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                  raise ValueError

    def send_email_html(self, subject, html):
        with smtplib.SMTP(
            "smtp-mail.outlook.com", 587
        ) as server:
            server.ehlo()
            server.starttls()
            server.login(self.from_email, self.from_password)
            for email in self.emails_to_send:
              msg = MIMEMultipart('alternative')
              msg['Subject'] = subject
              part1 = MIMEText(html, 'html')
              msg.attach(part1)
              try:
                  server.sendmail(self.from_email, email, msg.as_string())
              except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                  raise ValueError
