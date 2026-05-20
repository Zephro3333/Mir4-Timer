from datetime import datetime


class Health:
    def __init__(self):
        self.last_run = None
        self.events = 0
        self.status = "🟢 ONLINE"

    def update(self, events_count: int):
        self.last_run = datetime.utcnow().isoformat()
        self.events = events_count

    def build(self):
        return (
            "📊 MIR4 DASHBOARD\n\n"
            f"Status: {self.status}\n"
            f"Last run: {self.last_run}\n"
            f"Events: {self.events}"
        )
