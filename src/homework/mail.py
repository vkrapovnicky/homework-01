import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from homework.config import *

def send_email(md5_hash: str, sha256_hash: str) -> bool:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = "Домашнее задание"

    text = f"""
ФИО: {STUDENT_NAME}

MD5:
{md5_hash}

SHA-256:
{sha256_hash}
"""

    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    server = None
    try:
        server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=10)
        server.login(EMAIL_FROM, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print("Message sent successfully")
        return True
    except Exception as e:
        print(f"Message not sent, got error: {e}")
        return False
    finally:
        if server:
            try:
                server.quit()
            except Exception:
                pass
