import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(to_email, subject, content):
    message = Mail(
        from_email="yourname@savelife.com",  # use your verified sender email
        to_emails=to_email,
        subject=subject,
        plain_text_content=content
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(str(e))
        return None
