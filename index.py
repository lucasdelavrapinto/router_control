
import asyncio
from time import sleep
from playwright.async_api import async_playwright
from credentials import load_credentials
from telegram import send_telegram_message
import argparse
import datetime

LOGIN_URL_ROUTER = "http://192.168.1.1/"  # depois você troca pelo seu

async def run():
    
    now = datetime.datetime.now()
    creds = load_credentials()
    
    parser = argparse.ArgumentParser(description="Ativar ou desativar o bloqueio de internet.")
    parser.add_argument("switch", choices=["on", "off"], help="Ação para ativar ('on') ou desativar ('off') o bloqueio de internet.")
    args = parser.parse_args()
    if not args:
        print("Por favor, forneça um argumento: 'on' para ativar o bloqueio ou 'off' para desativar.")
        return

    async with async_playwright() as p:
        browser_context = await p.chromium.launch(
            headless=False
        )
        page = await browser_context.new_page()

        # Acessar página de login
        await page.goto(LOGIN_URL_ROUTER)

        # Preencher campos de login (ajustar os seletores depois)
        await page.fill("#Frm_Username", creds["user_router"])
        await page.fill("#Frm_Password", creds["password_router"])
        sleep(1)
        await page.click("#LoginId")

        # Esperar redirecionamento (ajustar conforme necessário)
        await page.wait_for_load_state("networkidle")

        await page.click("#internet")
        sleep(1)
        await page.click("#security")
        sleep(1)
        await page.click("#filterCriteria")
        sleep(1)
        
        if args.switch == "on":
            await page.click("#MacFilterEnable1") #LIGAR BLOQUEIO DE INTERNET
        else:
            await page.click("#MacFilterEnable0") #DESLIGAR BLOQUEIO DE INTERNET
            
        sleep(2)
        await page.click("#Btn_apply_FirewallConf")
        
        is_blocking = "ativado" if args.switch == "on" else "desativado"
        
        # send notification to Telegram
        message = f"O bloqueio de internet foi {is_blocking} com sucesso! Data: {now.strftime('%d/%m/%Y %H:%M')}"
        try:
            await send_telegram_message(message)
        except Exception as e:
            print(f"Failed to send Telegram message: {e}")
      
        await browser_context.close()

if __name__ == "__main__":
    asyncio.run(run())
