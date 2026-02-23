from __future__ import annotations

from typing import Any


def start_game(update: Any, context: Any) -> None:
    """
    Params: Telegram update/context.
    Returns: None.
    Description: Create a new game for the group chat and start round 1.
    Examples:
        Input: update=<Update>, context=<Context>
        Output: None
    """
    raise NotImplementedError("Create game state and call round start.")


def stop_game(update: Any, context: Any) -> None:
    """
    Params: Telegram update/context.
    Returns: None.
    Description: End the current game and display final stats.
    Examples:
        Input: update=<Update>, context=<Context>
        Output: None
    """
    raise NotImplementedError("Stop game and send final stats.")


def score(update: Any, context: Any) -> None:
    """
    Params: Telegram update/context.
    Returns: None.
    Description: Show the current leaderboard for the game.
    Examples:
        Input: update=<Update>, context=<Context>
        Output: None
    """
    raise NotImplementedError("Show current leaderboard.")


def handle_message(update: Any, context: Any) -> None:
    """
    Params: Telegram update/context.
    Returns: None.
    Description: Treat incoming messages as answers during active rounds.
    Examples:
        Input: update=<Update>, context=<Context>
        Output: None
    """
    raise NotImplementedError("Collect answers while round is active.")


def continue_game_callback(update: Any, context: Any) -> None:
    """
    Params: Telegram update/context.
    Returns: None.
    Description: Handle the continue/stop prompt after 5 rounds.
    Examples:
        Input: update=<Update>, context=<Context>
        Output: None
    """
    raise NotImplementedError("Handle continue/stop decision.")
