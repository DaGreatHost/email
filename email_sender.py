import smtplib
from email.mime.text import MIMEText
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

unsubscribe_template = "\n\nTo unsubscribe, click here: https://tgreward.shop/join.php?unsubscribe={email}"

def send_bulk_email(subject, html_body):
    with open("confirmed_emails.txt", "r") as f:
        recipients = [line.strip() for line in f.readlines() if line.strip()]

    for email in recipients:
        full_html = html_body + unsubscribe_template.format(email=email)
        msg = MIMEText(full_html, 'html')
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = email

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, email, msg.as_string())
