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

        print("🔥 ENGINE RUN:", now)

        upcoming = self.get_upcoming_bosses(now)

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

    # 💥 NOVA LÓGICA ROBUSTA
    def get_upcoming_bosses(self, now):
        alerts = []

        for b in BOSSES:
            boss_time = self.parse_time(b["time"], now)

            alert_time = boss_time - timedelta(minutes=15)

            # 🔥 janela de 5 minutos (ANTI CRON DRIFT)
            start = alert_time - timedelta(minutes=2)
            end = alert_time + timedelta(minutes=2)

            if start <= now <= end:
                alerts.append(b)

        return alerts

    def parse_time(self, t, now):
        h, m = map(int, t.split(":"))

        return now.replace(
            hour=h,
            minute=m,
            second=0,
            microsecond=0
        )
