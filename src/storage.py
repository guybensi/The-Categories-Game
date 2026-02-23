from __future__ import annotations

from typing import Any

from .models import Answer, GameState, PlayerStats, Round


def get_db(uri: str) -> Any:
    """
    Params: MongoDB connection string.
    Returns: Database handle.
    Description: Connect to MongoDB and return a DB object.
    Examples:
        Input: uri="mongodb://localhost:27017"
        Output: <Database>
    """
    raise NotImplementedError("Implement MongoDB connection using pymongo.")


def ensure_indexes(db: Any) -> None:
    """
    Params: db handle.
    Returns: None.
    Description: Create required indexes for uniqueness.
    Examples:
        Input: db=<Database>
        Output: None
    """
    raise NotImplementedError("Create unique indexes on answers and rounds.")


def save_game(game: GameState) -> None:
    """
    Params: game object.
    Returns: None.
    Description: Insert or update a game record.
    Examples:
        Input: game=GameState(chat_id=1001, game_id="...")
        Output: None
    """
    raise NotImplementedError("Insert or update game in MongoDB.")


def save_round(round_obj: Round) -> None:
    """
    Params: round object.
    Returns: None.
    Description: Insert or update a round record.
    Examples:
        Input: round_obj=Round(game_id="g1", round_number=1, letter="C", category="City", started_at_ms=...)
        Output: None
    """
    raise NotImplementedError("Insert or update round in MongoDB.")


def save_answer(answer: Answer) -> None:
    """
    Params: answer object.
    Returns: None.
    Description: Insert answer record.
    Examples:
        Input: answer=Answer(game_id="g1", round_id="r1", user_id=7, raw_text="Cairo", corrected_text="Cairo", valid=True, score=18, response_ms=12000)
        Output: None
    """
    raise NotImplementedError("Insert answer in MongoDB.")


def upsert_player_stats(stats: PlayerStats) -> None:
    """
    Params: stats object.
    Returns: None.
    Description: Update player stats for the chat.
    Examples:
        Input: stats=PlayerStats(chat_id=1001, user_id=7, username="guy")
        Output: None
    """
    raise NotImplementedError("Upsert player stats in MongoDB.")


def has_answer_been_used(
    game_id: str, letter: str, category: str, corrected_text: str
) -> bool:
    """
    Params: ids and normalized answer.
    Returns: True if already used.
    Description: Enforce no-repeat rule.
    Examples:
        Input: game_id="g1", letter="C", category="City", corrected_text="Cairo"
        Output: False
    """
    raise NotImplementedError("Check answer uniqueness in MongoDB.")
