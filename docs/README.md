# Categories Game Bot — Planning (Tech Outline)

This document describes the next stage of the Telegram Categories Game bot.
You can use it as a checklist while you implement code later.

## Goals

- Run a full 5‑round Categories game in a Telegram group.
- Randomly pick a letter (A‑Z) and a category from a list each round.
- Give each player 30 seconds to answer.
- Validate answers with Groq (strict JSON) for correctness, spelling, and category match.
- Score based on correctness + response time.
- Store correct answers in MongoDB and reject repeats.
- After each round, show a live leaderboard.
- After 5 rounds, ask to continue; if no, show full stats and end.
- Track per‑player stats: correct %, avg response time, etc.

## Tech Stack (Assumed)

- Python
- `python-telegram-bot` (ptb) v21+
- Groq API for validation
- MongoDB for persistence

## Game Flow (High Level)

1. `/start_game` in a group creates a new game session.
2. For each round:
   - Pick a random letter and random category.
   - Open a 30‑second answer window.
   - Collect each user's first answer only.
   - Validate each answer with Groq.
   - Score and store valid answers.
   - Show round scores + total leaderboard.
3. After 5 rounds, ask “Continue?”:
   - Yes → start another set of rounds.
   - No → show final results and statistics.

## Data Model (MongoDB)

Collections (suggested):

- `games`
  - `game_id`, `chat_id`, `status`, `current_round`, `started_at`, `ended_at`
- `rounds`
  - `game_id`, `round_number`, `letter`, `category`, `started_at`, `ended_at`
- `answers`
  - `game_id`, `round_id`, `user_id`, `username`, `raw_text`, `corrected_text`,
    `valid`, `score`, `response_ms`
- `players`
  - `chat_id`, `user_id`, `username`, `total_score`, `correct_count`,
    `answer_count`, `avg_response_ms`

Indexes:

- Unique index on (`game_id`, `round_id`, `user_id`) to prevent multi‑answers.
- Unique index on (`game_id`, `category`, `letter`, `corrected_text`) to block repeats.

## Groq Validation (Strict JSON)

Goal: return a strict JSON object so the bot can parse it reliably.

Example response schema:

```
{
  "valid": true,
  "corrected": "Cairo",
  "reason": "Cairo is a city in Egypt and matches the letter C.",
  "categoryMatch": true
}
```

Rules:

- Must start with the round letter after correction.
- Must match the category (e.g., City vs Country).
- If spelling is close but correct, return `corrected` and `valid=true`.
- If wrong category or not real, return `valid=false`.

## Scoring Model (Suggested)

- Base: +10 for valid.
- Time bonus: +0 to +10 based on how fast they answered.
  - Example: `time_bonus = max(0, 10 - (response_ms / 3000))`
- Total per answer = base + time bonus.
- Invalid or repeated answers score 0.

## Stats to Track

Per player:

- Total score
- Correct %
- Average response time
- Best streak (optional)
- Category accuracy (optional)

## Telegram Commands / Messages

- `/start_game`: Create a new game for the group.
- `/stop_game`: End the game and show final stats.
- `/score`: Show current leaderboard.
- Messages during round: treated as answers.

## Implementation Steps (Checklist)

1. **Game state manager** - Haim
   - Keep in‑memory state per `chat_id`.
   - Track round start time and timer job.
2. **Round selection** - Haim
   - Random letter A‑Z.
   - Random category from a fixed list (config file or DB).
3. **Answer collection** - Haim
   - Accept one answer per user per round.
   - Store timestamp to compute response time.
4. **Groq validation** - Guy
   - Send answer, letter, category.
   - Parse strict JSON response.
5. **Scoring + storage** - Guy
   - Score valid answers.
   - Save to MongoDB and update player stats.
   - Reject repeated answers in this game (or global).
6. **Leaderboard + stats** - Guy
   - After round: show scores + totals.
   - End game: show full stats.
7. **Continue prompt** -Haim
   - After 5 rounds, ask if players want to continue.

## Environment Variables

- `TELEGRAM_BOT_TOKEN`
- `GROQ_API_KEY`
- `MONGODB_URI`

## Suggested Project Files (Example)

Use this as a simple, clean layout. Adjust names if you want.

```
The-Categories-Game/
  .gitignore
  .editorconfig
  README.md
  requirements.txt
  .env               # local only, never commit
  docs/
    README.md        # this plan
  src/
    __init__.py
    main.py          # bot entrypoint - Haim
    bot.py           # telegram setup, handlers register -Haim
    handlers.py      # commands + message routing -Haim
    game_state.py    # in-memory game state per chat - Guy
    round_logic.py   # round lifecycle + timers - Haim
    validation.py    # Groq validation client - Guy
    scoring.py       # scoring rules - Guy
    storage.py       # MongoDB client + queries - GUY
    models.py        # data models / helpers - Guy
    categories.py    # list of categories - Haim
  tests/
    test_validation.py
    test_scoring.py 
```

Notes:

- Keep `.env` local only.
- If you don’t want `src/`, you can put the Python files at project root.
