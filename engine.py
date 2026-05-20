from datetime import datetime
import os

from bosses import BOSSES
from webhook import send_message
import state


class MIR4Engine:
    def __init__(self):
        print("🔥 ENGINE INIT")

    def run(self):
        now = datetime.utcnow()

        print("\n==============================")
        print("🔥 MIR4 ENGINE DEBUG START")
        print("==============================")

        # 📍 CONFIRMA ONDE O CÓDIGO ESTÁ A CORRER
        print("🔥 ENGINE FILE:", __file__)
        print("🔥 WORKING DIR:", os.getcwd())

        # 📦 CONFIRMA STATE IMPORTADO
        print("🔥 STATE FILE:", state.__file__)

        # 📊 BOSSES CHECK
        print("🔥 TOTAL BOSSES:", len(BOSSES))

        # 🧪 TESTE SIMPLES DE MENSAGEM
        test_msg = (
            "🔥 MIR4 ENGINE DEBUG TEST\n\n"
            f"Time: {now.isoformat()}\n"
            f"Bosses loaded: {len(BOSSES)}\n"
        )

        print("🔥 SENDING TEST MESSAGE...")

        send_message(test_msg)

        print("🔥 SEND COMPLETE")

        print("==============================\n")

        return "DEBUG", "DEBUG"
