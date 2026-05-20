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

        boss_msg = build_boss_message(BOSSES)

        self.health.update(len(BOSSES))
        dashboard_msg = self.health.build()

        final_msg = boss_msg + "\n\n" + dashboard_msg

        send_message(final_msg)

        return boss_msg, dashboard_msg
