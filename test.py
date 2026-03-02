
import asyncio
from telegram import send_telegram_message

async def run():

    # send notification to Telegram
    message = f"O bloqueio de internet foi ativado/desativado com sucesso! Data: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')}"
    await send_telegram_message(message)

if __name__ == "__main__":
    asyncio.run(run())
