import json

CREDENTIALS_FILE = "credentials.json"

def load_credentials():
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        user = input("Usuário: ")
        password = input("Senha: ")
        creds = {"user_router": user, "password_router": password}
        with open(CREDENTIALS_FILE, "w") as f:
            json.dump(creds, f)
        return creds