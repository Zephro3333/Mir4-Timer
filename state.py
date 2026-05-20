import json
import os


class State:
    def __init__(self):
        self.path = "state/data.json"

        os.makedirs("state", exist_ok=True)

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

        try:
            with open(self.path, "r") as f:
                self.data = json.load(f)
        except:
            self.data = {}

    def is_sent(self, key):
        return self.data.get(key, False)

    def mark_sent(self, key):
        self.data[key] = True

        try:
            with open(self.path, "w") as f:
                json.dump(self.data, f, indent=2)

            print("✅ STATE SAVED")

        except Exception as e:
            print("❌ STATE SAVE ERROR:", str(e))
