from __future__ import annotations

from typing import Any


def build_application(token: str) -> Any:
    """
    Params: token (bot token).
    Returns: A python-telegram-bot Application.
    Description: Create and configure the PTB application.
    Examples:
        Input: token="123:ABC"
        Output: <Application>
    """
    raise NotImplementedError("Build PTB Application and configure defaults.")


def register_handlers(app: Any) -> None:
    """
    Params: app (Application).
    Returns: None.
    Description: Attach all command and message handlers from handlers.py.
    Examples:
        Input: app=<Application>
        Output: None
    """
    raise NotImplementedError("Register command and message handlers.")


def run_bot(app: Any) -> None:
    """
    Params: app (Application).
    Returns: None.
    Description: Start polling and keep the bot running.
    Examples:
        Input: app=<Application>
        Output: None
    """
    raise NotImplementedError("Call app.run_polling() or similar.")
