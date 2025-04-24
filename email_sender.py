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

def send_confirmation_email(email):
    subject = "Please confirm your email"
    confirm_link = f"https://tgreward.shop/join.php?confirm={email}"
    html_body = f"""
        <h2>Welcome!</h2>
        <p>Thanks for signing up. Please confirm your email by clicking the link below:</p>
        <a href="{confirm_link}">Confirm My Email</a>
        <br><br>
        If you didn’t request this, you can ignore this email.
    """ + unsubscribe_template.format(email=email)

    msg = MIMEText(html_body, 'html')
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = email

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, email, msg.as_string())
