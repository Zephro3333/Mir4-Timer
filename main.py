import os
import requests


def main():
    webhook = os.getenv("WEBHOOK_URL")

    print("🔥 WEBHOOK =", webhook)

    response = requests.post(
        webhook,
        json={
            "content": "🔥 TESTE DIRETO DISCORD"
        }
    )

    print("🔥 STATUS =", response.status_code)
    print("🔥 RESPONSE =", response.text)


if __name__ == "__main__":
    main()
