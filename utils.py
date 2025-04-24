def save_pending_email(email):
    with open("pending_emails.txt", "a") as f:
        f.write(email + "\n")
