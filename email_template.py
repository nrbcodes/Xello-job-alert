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

        <!-- Header -->
        <div style="background:linear-gradient(135deg,#6c63ff 0%,#48c6ef 100%);padding:36px 32px;text-align:center;">
          <div style="font-size:40px;margin-bottom:8px;">🎯</div>
          <h1 style="margin:0;color:#ffffff;font-size:26px;font-weight:700;letter-spacing:-0.5px;">
            QA Job Alert
          </h1>
          <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">
            {len(qa_jobs)} new opening{'s' if len(qa_jobs) > 1 else ''} found at Xello · {today}
          </p>
        </div>

        <!-- Body -->
        <div style="background:#f7f8ff;padding:28px 28px 8px;">
          <p style="margin:0 0 20px;color:#555;font-size:14px;line-height:1.6;">
            Good news! The daily scan of <strong>Xello's job board</strong> found
            QA-related opening{'s' if len(qa_jobs) > 1 else ''} matching your alert:
          </p>
          {job_cards}
        </div>

        <!-- CTA -->
        <div style="background:#f7f8ff;padding:8px 28px 28px;text-align:center;">
          <a href="{url}" style="display:inline-block;padding:12px 32px;
             background:#1a1a2e;color:#fff;text-decoration:none;border-radius:25px;
             font-size:14px;font-weight:600;letter-spacing:0.3px;">
            View All Xello Jobs
          </a>
        </div>

        <!-- Footer -->
        <div style="background:#eef0ff;padding:18px 28px;text-align:center;
                    border-top:1px solid #dde1ff;">
          <p style="margin:0;color:#999;font-size:12px;line-height:1.6;">
            You're receiving this because you set up a daily QA job alert.<br>
            Powered by GitHub Actions · Runs daily at 2:30 PM IST
          </p>
        </div>

      </div>
    </body>
    </html>
    """
