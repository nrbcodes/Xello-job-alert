def build_weekly_summary_email(url, checks_done, qa_jobs_found):
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
            Here's a summary of what your job alert bot did this week:
          </p>
          <div style="display:flex;gap:12px;justify-content:center;">
            <div style="background:#fff;border-radius:12px;padding:16px 24px;text-align:center;
                        border:1px solid #e0e4ff;flex:1;">
              <p style="margin:0;font-size:28px;font-weight:700;color:#6c63ff;">{checks_done}</p>
              <p style="margin:4px 0 0;font-size:12px;color:#888;">Checks done</p>
            </div>
            <div style="background:#fff;border-radius:12px;padding:16px 24px;text-align:center;
                        border:1px solid #e0e4ff;flex:1;">
              <p style="margin:0;font-size:28px;font-weight:700;color:#43b89c;">{qa_jobs_found}</p>
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
