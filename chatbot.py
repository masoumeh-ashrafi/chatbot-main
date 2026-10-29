

# py -m pip install requests python-dotenv rich
import itertools
import os
import threading
import time

import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

console = Console()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}"

HEADERS = {
    "Content-Type": "application/json"
}


def spinner(stop_event):
    for char in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        print(f"\rGemini is thinking... {char}", end="", flush=True)
        time.sleep(0.1)
    print("\r" + " " * 30 + "\r", end="", flush=True)


print("Gemini CLI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ("exit", "quit"):
        break

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    stop_event = threading.Event()
    loading_thread = threading.Thread(target=spinner, args=(stop_event,))
    loading_thread.start()

    try:
        response = requests.post(URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        stop_event.set()
        loading_thread.join()

        data = response.json()
        reply = data["candidates"][0]["content"]["parts"][0]["text"]

        console.print(f"\n[bold cyan]Gemini:[/bold cyan]")
        console.print(Markdown(reply))
        print()

    except Exception as e:
        stop_event.set()
        loading_thread.join()

        print("Error:", e)
        if "response" in locals():
            print(response.text)