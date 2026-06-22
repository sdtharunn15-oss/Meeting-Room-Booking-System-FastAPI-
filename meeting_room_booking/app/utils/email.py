import smtplib
from email.message import EmailMessage


def send_email(to_email, subject, message):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"


    email = EmailMessage()

    email["From"] = sender_email
    email["To"] = to_email
    email["Subject"] = subject

    email.set_content(message)


    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            sender_password
        )

        smtp.send_message(email)


    print("Email sent successfully")