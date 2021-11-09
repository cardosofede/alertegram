import telegram

class TelegramNotifier:
    def __init__(self, token: str):
        self._bot = telegram.Bot(token=token)
        
    def send_messages(self, chats_id: list, message: str):
        for chat_id in chats_id:
            self._bot.send_message(
                text=message,
                chat_id=chat_id
            )