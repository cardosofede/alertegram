from scrapper import WebScrapper
from notifier import TelegramNotifier
from dotenv import dotenv_values
import time

if __name__ == '__main__':
    token = dotenv_values('.env')['token']
    a = WebScrapper(website='https://www.natividad.org.ar/turnos_enfermos.php', freq=30)
    notifier = TelegramNotifier(token=token)
    chats_id = ['481175164']
    while True:
        try:
            avaiable, text = a.avaiable()
            if avaiable:
                notifier.send_messages(
                    chats_id=chats_id,
                    message='Turno disponible')
            else:
                notifier.send_messages(
                    chats_id=chats_id,
                    message=text)
        except:
            time.sleep(60)
        time.sleep(a._freq)
