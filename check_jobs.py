import requests
from bs4 import BeautifulSoup
import smtplib
import os
import sys
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_template import build_html_email, build_weekly_summary_email, build_error_email
from stats_tracker import update_stats, get_stats, reset_stats

URL = "https://xello.applytojob.com/apply"
QA_KEYWORDS = ["qa", "quality assurance", "quality enjjjgineer", "test engineer", "sdet", "automation engineer"]
# QA_KEYWORDS = ["principal", "software"]
MAX_RETRIES = 3
RETRY_DELAY = 10

def fetch_jobs():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Attempt {attempt}/{MAX_RETRIES} — fetching jobs...")
            res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            jobs = []
            for link in soup.select("a[href*='/apply/']"):
                title = link.get_text(strip=True)
                href = link.get("href", "")
                if title and href and href != URL:
                    jobs.append({"title": title, "url": href})
            print(f"Successfully fetched {len(jobs)} total job(s).")
            return jobs
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt} timed out.")
        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt} failed — connection error.")
        except requests.exceptions.HTTPError as e:
            print(f"Attempt {attempt} failed — HTTP error: {e}")
        except Exception as e:
            print(f"Attempt {attempt} failed — unexpected error: {e}")

        if attempt < MAX_RETRIES:
            print(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)

    raise Exception(f"Failed to fetch jobs after {MAX_RETRIES} attempts. The page may be unreachable.")

def filter_qa_jobs(jobs):
    return [j for j in jobs if any(kw in j["title"].lower() for kw in QA_KEYWORDS)]

def send_email(subject, html_content):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_PASS"]
    recipient = os.environ["NOTIFY_EMAIL"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Job Alert Bot <{sender}>"
    msg["To"] = recipient
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, msg.as_string())
    print("Email sent!")

if __name__ == "__main__":
    run_mode = os.environ.get("RUN_MODE", "daily")
    run_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    try:
        if run_mode == "weekly":
            # Read real stats before resetting
            stats = get_stats()
            print(f"Weekly stats: {stats}")
            html = build_weekly_summary_email(URL, stats["checks_done"], stats["qa_jobs_found"])
            send_email("📋 Weekly Job Alert Summary — Xello", html)
            # Reset stats for the new week
            reset_stats()

        else:
            jobs = fetch_jobs()
            qa_jobs = filter_qa_jobs(jobs)
            print(f"Found {len(qa_jobs)} QA job(s).")

            # Always update stats after a successful check
            update_stats(len(qa_jobs))

            if qa_jobs:
                html = build_html_email(qa_jobs, URL)
                send_email(f"🎯 {len(qa_jobs)} QA Job(s) Found at Xello!", html)
            else:
                print("No QA jobs found. No email sent.")

    except Exception as e:
        print(f"ERROR: {e}")
        try:
            html = build_error_email(str(e), run_time)
            send_email("⚠️ Job Alert Bot Error — Action Required", html)
        except Exception as mail_err:
            print(f"Failed to send error email: {mail_err}")
        sys.exit(1)
