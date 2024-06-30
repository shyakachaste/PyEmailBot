import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails(subject, body, recipients):
    # Email account credentials
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # SMTP server configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Create a SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Prepare email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email to each recipient
    for recipient in recipients:
        msg['To'] = recipient
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)

    # Terminate the SMTP session
    server.quit()

# Example usage
subject = "Hello from Your Email Bot"
body = "This is a test email sent by your Python email bot."
recipients = [
    "recipient1@example.com",
    "recipient2@example.com",
    # Add more email addresses as needed
]

send_emails(subject, body, recipients)
