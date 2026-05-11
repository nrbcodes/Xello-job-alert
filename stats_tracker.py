import json
import os
from datetime import datetime, timedelta

STATS_FILE = "stats.json"

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"week_start": "", "checks_done": 0, "qa_jobs_found": 0}
    with open(STATS_FILE, "r") as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

def get_week_start():
    today = datetime.now()
    # Week starts on Monday
    monday = today - timedelta(days=today.weekday())
    return monday.strftime("%Y-%m-%d")

def update_stats(qa_jobs_found_count):
    stats = load_stats()
    current_week = get_week_start()

    # Reset if it's a new week
    if stats["week_start"] != current_week:
        print(f"New week detected ({current_week}), resetting stats.")
        stats = {
            "week_start": current_week,
            "checks_done": 0,
            "qa_jobs_found": 0
        }

    stats["checks_done"] += 1
    stats["qa_jobs_found"] += qa_jobs_found_count
    save_stats(stats)
    print(f"Stats updated: {stats}")
    return stats

def get_stats():
    return load_stats()

def reset_stats():
    current_week = get_week_start()
    stats = {
        "week_start": current_week,
        "checks_done": 0,
        "qa_jobs_found": 0
    }
    save_stats(stats)
    return stats
