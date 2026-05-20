from collections import defaultdict


def build_boss_message(bosses):
    if not bosses:
        return ""

    grouped = defaultdict(list)

    for b in bosses:
        grouped[b["time"]].append(b)

    msg = "🔥 MIR4 BOSS ALERT (15 MIN)\n\n"

    for time in sorted(grouped.keys()):
        msg += f"🕒 SERVER TIME: {time}\n\n"

        for b in grouped[time]:
            msg += (
                f"🌍 World: {b['world']}\n"
                f"🏷️ Layer: {b['layer']}\n"
                f"⚔️ Boss: {b['boss']}\n"
                f"📍 Location: {b['location']}\n"
                "----------------------\n"
            )

        msg += "\n"

    return msg
