from datetime import datetime, timedelta
from bosses import BOSSES
from discord_formatter import build_boss_message
from webhook import send_message
from health import Health
from state import State


class MIR4Engine:
    def __init__(self):
        self.health = Health()
        self.state = State()

    def run(self):
        now = datetime.utcnow()

        print("🔥 ENGINE RUN:", now)

        upcoming = self.get_upcoming_bosses(now)

        boss_msg = build_boss_message(upcoming)

        self.health.update(len(upcoming))
        dashboard_msg = self.health.build()

        final_msg = ""

        if boss_msg:
            final_msg += boss_msg + "\n\n"

        final_msg += dashboard_msg

        # 🚀 só envia se existir boss
        if upcoming:
            send_message(final_msg)

        return boss_msg, dashboard_msg

    # ⏱️ lógica alerta 15 min antes
    def get_upcoming_bosses(self, now):
        alerts = []

        for b in BOSSES:
            boss_time = self.parse_time(b["time"], now)

            # 15 minutos antes
            alert_time = boss_time - timedelta(minutes=15)

            # tolerância github cron
            diff = abs((now - alert_time).total_seconds())

            # aceita até 90 segundos
            if diff <= 90:

                key = f"{b['boss']}_{b['time']}"

                # evita duplicados
                if not self.state.is_sent(key):
                    alerts.append(b)
                    self.state.mark_sent(key)

        return alerts

    def parse_time(self, t, now):
        h, m = map(int, t.split(":"))

        return now.replace(
            hour=h,
            minute=m,
            second=0,
            microsecond=0
        )
