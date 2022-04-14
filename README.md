### About Project

This is a simple project where you can send emails
with a HTML page to a list of targets emails

----

#### What do you need ?
+ python
+ pip

#### How to use ?

1. Use this command to create a .venv ambient for python project
```
python3 -m venv .venv
```

2. Install dependencies
```
python3 -m pip install -r dev-requirements.txt
```

3. Add .env file with the email and password you want to use to send emails to everyone (you have .env.exemple as exemple)

4. Add target emails in `emails_list.py`.

5. Run project
```
python3 main.py
```
----

you can use a temporary email service to test, like [temp-mail](https://temp-mail.org)