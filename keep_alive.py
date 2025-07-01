import requests
import time
import threading
from datetime import datetime

class KeepAlive:
    def __init__(self, url, interval=300):  # Ping every 5 minutes
        self.url = url
        self.interval = interval
        self.running = False
        self.thread = None
    
    def ping(self):
        try:
            response = requests.get(self.url, timeout=10)
            print(f"[{datetime.now()}] Keep-alive ping: {response.status_code}")
        except Exception as e:
            print(f"[{datetime.now()}] Keep-alive failed: {e}")
    
    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
    
    def _run(self):
        while self.running:
            time.sleep(self.interval)
            self.ping()
            
    def stop(self):
        self.running = False