from datetime import datetime, timedelta
from bosses import BOSSES
from discord_formatter import build_boss_message
from webhook import send_message
from health import Health


class MIR4Engine:
    def __init__(self):
        self.health = Health()

    def run(self):
        now = datetime.utcnow()

        now_minutes = now.hour * 60 + now.minute

        print("🔥 ENGINE RUN:", now, "MIN:", now_minutes)

        upcoming = self.get_upcoming_bosses(now_minutes)

        print("🔥 UPCOMING:", len(upcoming))

        boss_msg = build_boss_message(upcoming)

        self.health.update(len(upcoming))
        dashboard_msg = self.health.build()

        final_msg = ""

        if boss_msg:
            final_msg += boss_msg + "\n\n"

        final_msg += dashboard_msg

        if upcoming:
            send_message(final_msg)

        return boss_msg, dashboard_msg

    def get_upcoming_bosses(self, now_minutes):
        alerts = []

        for b in BOSSES:
            h, m = map(int, b["time"].split(":"))
            boss_minutes = h * 60 + m

            alert_minutes = boss_minutes - 15

            # 🔥 janela de tolerância
            if abs(now_minutes - alert_minutes) <= 2:
                alerts.append(b)

        return alerts
