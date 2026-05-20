from datetime import datetime
from bosses import BOSSES
from discord_formatter import build_boss_message
from webhook import send_message
from health import Health


class MIR4Engine:
    def __init__(self):
        self.health = Health()

    def run(self):
        now = datetime.utcnow()

        print("🔥 ENGINE RUN:", now)

        # 🚨 DEBUG FORÇADO
        upcoming = BOSSES

        print("🔥 UPCOMING:", len(upcoming))

        boss_msg = build_boss_message(upcoming)

        self.health.update(len(upcoming))
        dashboard_msg = self.health.build()

        final_msg = boss_msg + "\n\n" + dashboard_msg

        print(final_msg)

        # 🚨 FORÇA ENVIO
        send_message(final_msg)

        return boss_msg, dashboard_msg
