from datetime import datetime
from bosses import BOSSES
from webhook import send_message


class MIR4Engine:
    def run(self):
        now = datetime.utcnow()

        print("🔥 ENGINE RUN:", now)

        msg = "🔥 ENGINE WORKS CONFIRMATION\n\n"

        # 🔥 SEM FILTRO NENHUM
        for b in BOSSES[:3]:
            msg += f"{b['world']} | {b['boss']} | {b['time']}\n"

        send_message(msg)

        print("🔥 SENT FROM ENGINE")

        return "", ""
