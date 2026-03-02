import requests
from credentials import load_credentials

async def send_telegram_message(message_text):
    
    creds = load_credentials()
    
    """Sends a text message to a specified Telegram chat."""
    url = f"https://api.telegram.org/bot{creds['telegram_bot_token']}/sendMessage"
    params = {
        "chat_id": creds['telegram_chat_id'],
        "text": message_text,
        "parse_mode": "Markdown" # Optional: allows Markdown formatting
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an exception for bad status codes
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")