from django.shortcuts import render
from chatbot_app.chat_engine import chatbot_instance

def chat_view(request):
    """
    Web chat with short-term memory.
    - On GET: start a fresh conversation (history cleared).
    - On POST: append user and bot messages to history.
    """

    # If this is a fresh page load (GET request), clear chat history
    if request.method == "GET":
        request.session["chat_history"] = []
        request.session.modified = True

    # Retrieve the chat history (empty if just reset)
    history = request.session.get("chat_history", [])

    # If user submitted a new message (POST request)
    if request.method == "POST":
        user_input = request.POST.get("message", "").strip()
        if user_input:
            # Record user's message
            history.append({
                "role": "user",
                "text": user_input,
            })

            # Generate bot reply
            bot_reply = chatbot_instance.get_response(user_input)

            # Record bot's reply
            history.append({
                "role": "bot",
                "text": str(bot_reply),
            })

            # Save updated history in session
            request.session["chat_history"] = history
            request.session.modified = True

    # Render the page with the conversation history
    return render(request, "chatbot_app/chat.html", {
        "history": history,
    })
