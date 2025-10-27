from django.core.management.base import BaseCommand
from chatbot_app.chat_engine import chatbot_instance

class Command(BaseCommand):
    help = "Run a simple terminal question and answer chatbot"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bot ready. Press Control+C to quit."))

        try:
            while True:
                user_text = input("user: ")
                response = chatbot_instance.get_response(user_text)
                print(f"bot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
