import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
STUDENT_NAME = os.environ.get("STUDENT_NAME")

REQUIRED_ENV_VARS = ["EMAIL_FROM", "EMAIL_TO", "SMTP_USER", "SMTP_PASSWORD", "SMTP_HOST", "SMTP_PORT", "STUDENT_NAME"]
MISSING_VARS = [var for var in REQUIRED_ENV_VARS if var not in os.environ]

if MISSING_VARS:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(MISSING_VARS)}")
