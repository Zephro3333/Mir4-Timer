from datetime import datetime
from bosses import BOSSES
from webhook import send_message


class MIR4Engine:
    def run(self):
        print("🔥 ENGINE IS RUNNING")

        print("🔥 BOSSES TOTAL:", len(BOSSES))

        # 💣 FORÇA TOTAL (SEM FILTROS)
        msg = "🔥 FINAL DISCORD TEST\n\n"

        for b in BOSSES[:5]:
            msg += f"{b['world']} | {b['boss']} | {b['time']}\n"

        print("🔥 MESSAGE BUILT")

        send_message(msg)

        print("🔥 SENT")

        return msg, ""
