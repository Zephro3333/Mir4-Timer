import os
import requests

WEBHOOK_URL = os.getenv("WEBHOOK_URL")


def send_message(content: str):
    print("🔥 SEND MESSAGE TRIGGERED")

    if not WEBHOOK_URL:
        print("❌ WEBHOOK_URL missing")
        return

    try:
        r = requests.post(WEBHOOK_URL, json={"content": content})
        print("STATUS:", r.status_code)

        if r.status_code != 204:
            print("ERROR:", r.text)

    except Exception as e:
        print("ERROR:", str(e))
