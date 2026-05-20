from datetime import datetime, timedelta
from bosses import BOSSES
from webhook import send_message


class MIR4Engine:
    def run(self):
        now = datetime.utcnow()

        upcoming = self.get_upcoming_bosses(now)

        if not upcoming:
            print("🔥 SEM BOSSES NO MOMENTO")
            return "", ""

        message = self.build_message(upcoming)

        send_message(message)

        return message, ""

    def get_upcoming_bosses(self, now):
        alerts = []

        for b in BOSSES:
            h, m = map(int, b["time"].split(":"))
            boss_time = now.replace(hour=h, minute=m, second=0, microsecond=0)

            diff = (boss_time - now).total_seconds()

            if 0 <= diff <= 1800:
                alerts.append(b)

        return alerts

    def build_message(self, bosses):
        msg = "🔥 MIR4 BOSS ALERT (30 MIN)\n\n"

        grouped = {}

        for b in bosses:
            key = f"{b['world']}|{b['time']}"
            grouped.setdefault(key, []).append(b)

        for group, items in grouped.items():
            world, time = group.split("|")

            # 🌍 NOVO HEADER
            msg += f"🌍 {world} ⏰ {time}\n\n"

            for b in items:
                msg += f"⚔️ {b['boss']}\n"
                msg += f"📍 {b['location']}\n"
                msg += f"🏷️ {b['layer']}\n\n"

            msg += "----------------------\n\n"

        return msg
