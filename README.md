# Simple Q&A Chatbot Using Django and ChatterBot

## Overview
This project implements a simple question-and-answer chatbot using **Django** and **ChatterBot**.  
It allows users to interact with an AI-powered conversational bot either through a terminal interface or a web-based HTML interface.

## Features
- Interactive chatbot using ChatterBot library  
- Web interface built with Django and HTML  
- Terminal-based chat option  
- Basic natural language processing using spaCy  
- Session reset for a fresh chat on every page reload  

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/simple_chatbot_django.git
cd simple_chatbot_django
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

## Running the Project

### Option 1 – Web Interface
Run the Django development server:
```bash
python manage.py runserver
```
Then open your browser and go to:
```
http://127.0.0.1:8000/
```

### Option 2 – Terminal Chatbot
```bash
python manage.py terminal_bot
```

## Project Structure
```
simple_chatbot_django/
│
├── chatbot_app/
│   ├── templates/chatbot_app/
│   │   └── chat.html
│   ├── views.py
│   ├── urls.py
│   └── chat_engine.py
│
├── qabot_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```
