from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def build_bot():
    bot = ChatBot(
        "QABot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///db.sqlite3",
        logic_adapters=[
            "chatterbot.logic.BestMatch",
            "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.MathematicalEvaluation",
        ],
        read_only=False,
        tagger_language=None,
    )

    # Training pairs for basic conversation
    seed_pairs = [
        "Hi", "Hello. How can I help you today?",
        "Good morning. How are you doing?", "I am doing very well. Thank you for asking.",
        "You are welcome.", "Do you like hats?",
        "What is this project?", "This is a simple question and answer chatbot made with Django and ChatterBot.",
        "Goodbye", "Goodbye. Have a nice day."
    ]

    trainer = ListTrainer(bot)
    trainer.train(seed_pairs)

    return bot

# create a single shared bot instance
chatbot_instance = build_bot()
