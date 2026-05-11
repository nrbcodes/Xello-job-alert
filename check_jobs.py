import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

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

    body = "🎯 QA Job Alert at Xello!\n\n"
    for job in qa_jobs:
        body += f"• {job['title']}\n  {job['url']}\n\n"
    body += f"\nFull listing: {URL}"

    msg = MIMEText(body)
    msg["Subject"] = f"[Job Alert] {len(qa_jobs)} QA Job(s) Found at Xello!"
    msg["From"] = sender
    msg["To"] = recipient

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
