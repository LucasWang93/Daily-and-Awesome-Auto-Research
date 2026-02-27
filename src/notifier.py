"""Send daily report via email (SMTP)."""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import markdown

from .utils import get_logger

LOGGER = get_logger(__name__)


def send_email(report_path, email_cfg):
    """Read a Markdown report and send it as an HTML email."""
    if not email_cfg.get("enabled"):
        LOGGER.info("Email notifications disabled, skipping.")
        return False

    smtp_server = email_cfg.get("smtp_server", "")
    smtp_port = email_cfg.get("smtp_port", 587)
    sender = email_cfg.get("sender", "")
    recipient = email_cfg.get("recipient", "")
    password = os.environ.get("EMAIL_PASSWORD", "")

    if not all([smtp_server, sender, recipient, password]):
        LOGGER.warning("Email config incomplete, skipping.")
        return False

    report_path = Path(report_path)
    if not report_path.exists():
        LOGGER.warning("Report file not found: %s", report_path)
        return False

    md_text = report_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    subject = f"Daily Papers Report - {report_path.stem}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    msg.attach(MIMEText(md_text, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, [recipient], msg.as_string())
        LOGGER.info("Email sent to %s", recipient)
        return True
    except Exception as exc:
        LOGGER.error("Failed to send email: %s", exc)
        return False
