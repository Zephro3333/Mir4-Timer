import os
import requests


WEBHOOK_URL = os.getenv("WEBHOOK_URL")

print("🔥 WEBHOOK:", WEBHOOK_URL)


def send_message(content):
    if not WEBHOOK_URL:
        print("❌ WEBHOOK_URL NÃO EXISTE")
        return

    try:
        response = requests.post(
            WEBHOOK_URL,
            json={"content": content}
        )

        print("🔥 STATUS CODE:", response.status_code)
        print("🔥 RESPONSE:", response.text)

    except Exception as e:
        print("❌ WEBHOOK ERROR:", str(e))
