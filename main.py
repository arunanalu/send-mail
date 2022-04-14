import codecs
import os
import dotenv
from emails_list import emails
from mailer import Mailer


file = codecs.open("email.html", 'r', "utf-8")
html_body = file.read()

dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")
MY_EMAIL = os.getenv("MY_EMAIL")

mayuMail = Mailer(MY_EMAIL, PASSWORD, emails())

mayuMail.send_email_html("Mayu está testando um código para enviar emails!", html_body)