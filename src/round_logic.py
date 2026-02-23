from __future__ import annotations

import random
from typing import List, Any

from .categories import load_categories
from .game_state import finalize_round, set_round_prompt
from .models import RoundResult


def pick_letter() -> str:
    """
    Params: none.
    Returns: A single uppercase letter A-Z.
    Description: Randomly select the round letter.
    Examples:
        Input: none
        Output: "C"
    """
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def pick_category(categories: List[str]) -> str:
    """
    Params: list of category strings.
    Returns: One category.
    Description: Randomly select a category.
    Examples:
        Input: ["City", "Country"]
        Output: "City"
    """
    if not categories:
        raise ValueError("categories list is empty")
    return random.choice(categories)


def start_round(chat_id: int, app: Any) -> None:
    """
    Params: chat_id, PTB application.
    Returns: None.
    Description: Initialize round state and announce prompt.
    Examples:
        Input: chat_id=1001, app=<Application>
        Output: None
    """
    letter = pick_letter()
    category = pick_category(load_categories())
    set_round_prompt(chat_id, letter, category)
    # TODO: send a message to the chat and start a timer with PTB jobs.


def schedule_round_end(chat_id: int, app: Any, seconds: int) -> Any:
    """
    Params: chat_id, application, seconds.
    Returns: A PTB Job object.
    Description: Schedule the round end after N seconds.
    Examples:
        Input: chat_id=1001, app=<Application>, seconds=30
        Output: <Job>
    """
    raise NotImplementedError("Hook into PTB job queue to schedule round end.")


def end_round(chat_id: int, app: Any) -> None:
    """
    Params: chat_id, application.
    Returns: None.
    Description: Close the round, trigger validation, scoring, and leaderboard.
    Examples:
        Input: chat_id=1001, app=<Application>
        Output: None
    """
    _result: RoundResult = finalize_round(chat_id)
    # TODO: validate answers, score, store, and send leaderboard.
