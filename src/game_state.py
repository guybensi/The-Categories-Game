from __future__ import annotations

from typing import Dict, List

from .models import AnswerDraft, GameState, RoundResult, now_ms, new_game_state

_GAMES: Dict[int, GameState] = {}


def get_or_create_game(chat_id: int) -> GameState:
    """
    Params: chat_id (group chat id).
    Returns: In-memory GameState.
    Description: Fetch or initialize a game state for a chat.
    Examples:
        Input: chat_id=1001
        Output: GameState(chat_id=1001, game_id="...")
    """
    if chat_id not in _GAMES:
        _GAMES[chat_id] = new_game_state(chat_id)
    return _GAMES[chat_id]


def reset_game(chat_id: int) -> None:
    """
    Params: chat_id.
    Returns: None.
    Description: Clear game state for a chat.
    Examples:
        Input: chat_id=1001
        Output: None (game state removed)
    """
    _GAMES.pop(chat_id, None)


def is_round_active(chat_id: int) -> bool:
    """
    Params: chat_id.
    Returns: True if a round is active.
    Description: Check whether answers should be accepted.
    Examples:
        Input: chat_id=1001
        Output: False
    """
    game = _GAMES.get(chat_id)
    return bool(game and game.round_active)


def record_answer(chat_id: int, user_id: int, text: str, ts_ms: int) -> bool:
    """
    Params: chat_id, user_id, answer text, timestamp in ms.
    Returns: True if accepted, False if duplicate for this round.
    Description: Store the first answer per user per round.
    Examples:
        Input: chat_id=1001, user_id=7, text="Cairo", ts_ms=1700000000123
        Output: True
    """
    game = _GAMES.get(chat_id)
    if not game or not game.round_active:
        return False
    if user_id in game.answers:
        return False
    game.answers[user_id] = AnswerDraft(user_id=user_id, text=text, ts_ms=ts_ms)
    return True


def get_round_answers(chat_id: int) -> List[AnswerDraft]:
    """
    Params: chat_id.
    Returns: List of AnswerDraft objects for the round.
    Description: Read collected answers for validation and scoring.
    Examples:
        Input: chat_id=1001
        Output: [AnswerDraft(user_id=7, text="Cairo", ts_ms=...)]
    """
    game = _GAMES.get(chat_id)
    if not game:
        return []
    return list(game.answers.values())


def set_round_prompt(chat_id: int, letter: str, category: str) -> None:
    """
    Params: chat_id, letter, category.
    Returns: None.
    Description: Store current round letter/category in state and reset answers.
    Examples:
        Input: chat_id=1001, letter="C", category="City"
        Output: None
    """
    game = get_or_create_game(chat_id)
    game.current_round += 1
    game.round_active = True
    game.round_letter = letter
    game.round_category = category
    game.round_started_ms = now_ms()
    game.answers.clear()


def finalize_round(chat_id: int) -> RoundResult:
    """
    Params: chat_id.
    Returns: RoundResult object.
    Description: End the round and freeze current answers.
    Examples:
        Input: chat_id=1001
        Output: RoundResult(game_id="...", round_number=1, letter="C", category="City", answers=[...])
    """
    game = get_or_create_game(chat_id)
    game.round_active = False
    return RoundResult(
        game_id=game.game_id,
        round_number=game.current_round,
        letter=game.round_letter,
        category=game.round_category,
        answers=list(game.answers.values()),
    )
