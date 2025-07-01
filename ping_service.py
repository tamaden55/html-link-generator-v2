#!/usr/bin/env python3
"""
External service to keep Streamlit app alive
Run this on a different server or your local machine
"""
import requests
import time
import schedule
from datetime import datetime

APP_URL = "https://html-link-generator-v2-kcvfgrkbanmavsgykshgga.streamlit.app/"

def ping_app():
    try:
        response = requests.get(APP_URL, timeout=30)
        print(f"[{datetime.now()}] Ping successful: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Ping failed: {e}")
        return False

def main():
    print(f"Starting keep-alive service for: {APP_URL}")
    print("Pinging every 10 minutes...")
    
    # Schedule pings every 10 minutes
    schedule.every(10).minutes.do(ping_app)
    
    # Initial ping
    ping_app()
    
    # Keep running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    if "YOUR_STREAMLIT_APP_URL_HERE" in APP_URL:
        print("Please update APP_URL with your actual Streamlit app URL")
    else:
        main()