# email_reminder.py

"""
Sends payment reminder emails to recruiters via Gmail SMTP.

Author: Om Vairagade
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Replace with your Gmail (use App Passwords for security)
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "your-app-password"  # Do NOT use your main password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_payment_reminder(recruiter_row):
    """
    Sends a payment reminder email to a recruiter.

    Parameters:
    - recruiter_row: Pandas Series with keys:
        'name', 'email', 'subscription'
    """

    recipient_email = recruiter_row.get("email")
    name = recruiter_row.get("name", "Recruiter")
    plan = recruiter_row.get("subscription", "Basic").capitalize()

    if not recipient_email:
        print("❌ Missing recruiter email, cannot send reminder.")
        return

    subject = f"[Emper.ai] Payment Reminder for Your {plan} Plan"
    body = f"""
Dear {name},

This is a gentle reminder to complete your payment for the Emper.ai {plan} Plan.

Your AI-powered job matching will resume once the subscription is confirmed.

Please complete payment by this weekend to ensure delivery of your next candidate list.

For help, reply to this email or contact us via WhatsApp.

Best regards,  
Team Emper.ai  
📧 support@emper.ai  
📱 +91-XXXX-XXXXXX  
"""

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"📧 Payment reminder sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
