from datetime import datetime

def build_html_email(qa_jobs, url):
    today = datetime.now().strftime("%B %d, %Y")

    job_cards = ""
    for job in qa_jobs:
        job_cards += f"""
        <div style="background:#ffffff;border-radius:12px;padding:20px 24px;margin-bottom:16px;
                    border-left:4px solid #6c63ff;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
            <p style="margin:0 0 6px 0;font-size:17px;font-weight:600;color:#1a1a2e;">
                💼 {job['title']}
            </p>
            <a href="{job['url']}" style="display:inline-block;margin-top:10px;padding:8px 20px;
               background:linear-gradient(135deg,#6c63ff,#48c6ef);color:#fff;text-decoration:none;
               border-radius:20px;font-size:13px;font-weight:600;letter-spacing:0.5px;">
                View & Apply →
            </a>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:#f0f2ff;font-family:'Segoe UI',Arial,sans-serif;">
      <div style="max-width:560px;margin:40px auto;border-radius:20px;overflow:hidden;
                  box-shadow:0 8px 30px rgba(108,99,255,0.15);">
        <div style="background:linear-gradient(135deg,#6c63ff 0%,#48c6ef 100%);padding:36px 32px;text-align:center;">
          <div style="font-size:40px;margin-bottom:8px;">🎯</div>
          <h1 style="margin:0;color:#ffffff;font-size:26px;font-weight:700;">QA Job Alert</h1>
          <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">
            {len(qa_jobs)} new opening{'s' if len(qa_jobs) > 1 else ''} found at Xello · {today}
          </p>
        </div>
        <div style="background:#f7f8ff;padding:28px 28px 8px;">
          <p style="margin:0 0 20px;color:#555;font-size:14px;line-height:1.6;">
            Good news! The daily scan of <strong>Xello's job board</strong> found
            QA-related opening{'s' if len(qa_jobs) > 1 else ''} matching your alert:
          </p>
          {job_cards}
        </div>
        <div style="background:#f7f8ff;padding:8px 28px 28px;text-align:center;">
          <a href="{url}" style="display:inline-block;padding:12px 32px;
             background:#1a1a2e;color:#fff;text-decoration:none;border-radius:25px;
             font-size:14px;font-weight:600;">
            View All Xello Jobs
          </a>
        </div>
        <div style="background:#eef0ff;padding:18px 28px;text-align:center;border-top:1px solid #dde1ff;">
          <p style="margin:0;color:#999;font-size:12px;line-height:1.6;">
            Powered by GitHub Actions · Runs twice daily at 9:00 AM & 5:00 PM IST
          </p>
        </div>
      </div>
    </body>
    </html>
    """


def build_weekly_summary_email(url, checks_done):
    today = datetime.now().strftime("%B %d, %Y")

    return f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:#f0f2ff;font-family:'Segoe UI',Arial,sans-serif;">
      <div style="max-width:560px;margin:40px auto;border-radius:20px;overflow:hidden;
                  box-shadow:0 8px 30px rgba(108,99,255,0.15);">
        <div style="background:linear-gradient(135deg,#43b89c 0%,#2d6a4f 100%);padding:36px 32px;text-align:center;">
          <div style="font-size:40px;margin-bottom:8px;">✅</div>
          <h1 style="margin:0;color:#ffffff;font-size:26px;font-weight:700;">Weekly Check-In</h1>
          <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">
            Your job alert bot is alive and running · {today}
          </p>
        </div>
        <div style="background:#f7f8ff;padding:32px 28px;">
          <p style="margin:0 0 24px;color:#555;font-size:14px;line-height:1.6;">
            No QA jobs were found at Xello this week — but don't worry, your alert bot
            has been checking faithfully. You'll be the first to know when something shows up.
          </p>
          <div style="display:flex;gap:12px;justify-content:center;">
            <div style="background:#fff;border-radius:12px;padding:16px 24px;text-align:center;
                        border:1px solid #e0e4ff;flex:1;">
              <p style="margin:0;font-size:28px;font-weight:700;color:#6c63ff;">{checks_done}</p>
              <p style="margin:4px 0 0;font-size:12px;color:#888;">Checks this week</p>
            </div>
            <div style="background:#fff;border-radius:12px;padding:16px 24px;text-align:center;
                        border:1px solid #e0e4ff;flex:1;">
              <p style="margin:0;font-size:28px;font-weight:700;color:#43b89c;">0</p>
              <p style="margin:4px 0 0;font-size:12px;color:#888;">QA jobs found</p>
            </div>
          </div>
        </div>
        <div style="background:#f7f8ff;padding:8px 28px 28px;text-align:center;">
          <a href="{url}" style="display:inline-block;padding:12px 32px;
             background:#1a1a2e;color:#fff;text-decoration:none;border-radius:25px;
             font-size:14px;font-weight:600;">
            View Xello Jobs Board
          </a>
        </div>
        <div style="background:#eef0ff;padding:18px 28px;text-align:center;border-top:1px solid #dde1ff;">
          <p style="margin:0;color:#999;font-size:12px;line-height:1.6;">
            This weekly summary is sent every Sunday · Powered by GitHub Actions
          </p>
        </div>
      </div>
    </body>
    </html>
    """


def build_error_email(error_message, run_time):
    return f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:#fff0f0;font-family:'Segoe UI',Arial,sans-serif;">
      <div style="max-width:560px;margin:40px auto;border-radius:20px;overflow:hidden;
                  box-shadow:0 8px 30px rgba(220,53,69,0.15);">
        <div style="background:linear-gradient(135deg,#e63946 0%,#c1121f 100%);padding:36px 32px;text-align:center;">
          <div style="font-size:40px;margin-bottom:8px;">⚠️</div>
          <h1 style="margin:0;color:#ffffff;font-size:26px;font-weight:700;">Bot Alert: Something Went Wrong</h1>
          <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">
            Detected at {run_time}
          </p>
        </div>
        <div style="background:#fff8f8;padding:28px;">
          <p style="margin:0 0 16px;color:#555;font-size:14px;line-height:1.6;">
            Your Xello job alert bot encountered an error and <strong>could not complete its check</strong>.
            Please review the error below:
          </p>
          <div style="background:#fff;border-radius:10px;padding:16px 20px;border-left:4px solid #e63946;
                      font-family:monospace;font-size:13px;color:#c1121f;word-break:break-word;">
            {error_message}
          </div>
          <p style="margin:16px 0 0;color:#888;font-size:13px;line-height:1.6;">
            💡 This could be due to the page being temporarily unavailable or a network timeout.
            The bot will retry automatically on its next scheduled run.
          </p>
        </div>
        <div style="background:#eef0ff;padding:18px 28px;text-align:center;border-top:1px solid #dde1ff;">
          <p style="margin:0;color:#999;font-size:12px;">
            Powered by GitHub Actions · Check the Actions tab for full logs
          </p>
        </div>
      </div>
    </body>
    </html>
    """
