from __future__ import annotations

import os

from .bot import build_application, register_handlers, run_bot


def get_settings() -> dict:
    """
    Params: none.
    Returns: A dict with TELEGRAM_BOT_TOKEN, GROQ_API_KEY, MONGODB_URI.
    Description: Read environment variables and validate required values.
    Examples:
        Input: none
        Output: {"TELEGRAM_BOT_TOKEN": "...", "GROQ_API_KEY": "...", "MONGODB_URI": "..."}
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    groq_key = os.getenv("GROQ_API_KEY", "")
    mongo_uri = os.getenv("MONGODB_URI", "")
    if not token:
        raise ValueError("Missing TELEGRAM_BOT_TOKEN")
    return {
        "TELEGRAM_BOT_TOKEN": token,
        "GROQ_API_KEY": groq_key,
        "MONGODB_URI": mongo_uri,
    }


def main() -> None:
    """
    Params: none.
    Returns: None.
    Description: Load config, build the bot application, and start polling.
    Examples:
        Input: none
        Output: None
    """
    settings = get_settings()
    app = build_application(settings["TELEGRAM_BOT_TOKEN"])
    register_handlers(app)
    run_bot(app)


if __name__ == "__main__":
    main()
