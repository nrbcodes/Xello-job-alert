import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email_template import build_html_email

URL = "https://xello.applytojob.com/apply"
QA_KEYWORDS = ["qa", "quality assurance", "quality engineer", "test engineer", "sdet", "automation engineer"]


def fetch_jobs():
    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []
    for link in soup.select("a[href*='/apply/']"):
        title = link.get_text(strip=True)
        href = link.get("href", "")
        if title and href and href != URL:
            jobs.append({"title": title, "url": href})
    return jobs

def filter_qa_jobs(jobs):
    return [j for j in jobs if any(kw in j["title"].lower() for kw in QA_KEYWORDS)]

def send_email(qa_jobs):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_PASS"]
    recipient = os.environ["NOTIFY_EMAIL"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🎯 {len(qa_jobs)} QA Job(s) Found at Xello!"
    msg["From"] = f"Job Alert Bot <{sender}>"
    msg["To"] = recipient

    html_content = build_html_email(qa_jobs, URL)
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, msg.as_string())
    print("Email sent!")

if __name__ == "__main__":
    jobs = fetch_jobs()
    qa_jobs = filter_qa_jobs(jobs)
    print(f"Found {len(qa_jobs)} QA job(s): {qa_jobs}")
    if qa_jobs:
        send_email(qa_jobs)
    else:
        print("No QA jobs found today.")
