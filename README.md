# Gemini CLI Chatbot

A command-line chatbot built by **Masoumeh Ashrafi** using the Gemini API. It features an animated loading spinner and neatly formatted Markdown responses in the terminal.

## Features

- Chat with Gemini directly from the command line
- Animated spinner while Gemini is generating a response
- Markdown-formatted output rendered with `rich`
- API key loaded from a local `.env` file

## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `rich`
- A Gemini API key

## Setup

Install the dependencies:

```bash
pip install requests python-dotenv rich