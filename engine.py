from datetime import datetime, timedelta
from bosses import BOSSES
from discord_formatter import build_boss_message
from webhook import send_message
from health import Health


class MIR4Engine:
    def __init__(self):
        self.health = Health()
        self.sent_cache = set()  # 🧠 anti dupe

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

    def get_upcoming_bosses(self, now):
        alerts = []

        for b in BOSSES:
            h, m = map(int, b["time"].split(":"))
            boss_time = now.replace(hour=h, minute=m, second=0, microsecond=0)

            diff = (boss_time - now).total_seconds()

            # 🎯 janela 30 minutos antes
            if 0 <= diff <= 1800:
                key = f"{b['world']}|{b['boss']}|{b['time']}"

                # 🧠 anti duplicação
                if key not in self.sent_cache:
                    self.sent_cache.add(key)
                    alerts.append(b)

        return alerts
