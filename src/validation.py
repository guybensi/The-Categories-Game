from __future__ import annotations

import json

from .models import ValidationResult


def build_groq_prompt(answer: str, letter: str, category: str) -> str:
    """
    Params: answer text, letter, category.
    Returns: Prompt string.
    Description: Build a strict JSON prompt for Groq.
    Examples:
        Input: answer="Caihiro", letter="C", category="City"
        Output: "Return strict JSON only: {...}"
    """
    return (
        "Return strict JSON only with keys: valid, corrected, reason, categoryMatch. "
        f'Answer: "{answer}". Letter: "{letter}". Category: "{category}". '
        "Rules: correct spelling if close; valid only if real and matches category and letter."
    )


def validate_answer_groq(answer: str, letter: str, category: str) -> ValidationResult:
    """
    Params: answer text, letter, category.
    Returns: ValidationResult with valid/corrected/reason.
    Description: Call Groq and parse response.
    Examples:
        Input: answer="Caihiro", letter="C", category="City"
        Output: ValidationResult(valid=True, corrected="Cairo", reason="...", category_match=True)
    """
    raise NotImplementedError("Call Groq API and parse JSON response.")


def parse_groq_response(text: str) -> ValidationResult:
    """
    Params: raw Groq response text.
    Returns: ValidationResult.
    Description: Parse and validate the strict JSON response.
    Examples:
        Input: text='{\"valid\": true, \"corrected\": \"Cairo\", \"reason\": \"...\", \"categoryMatch\": true}'
        Output: ValidationResult(valid=True, corrected="Cairo", reason="...", category_match=True)
    """
    data = json.loads(text)
    return ValidationResult(
        valid=bool(data.get("valid")),
        corrected=str(data.get("corrected", "")),
        reason=str(data.get("reason", "")),
        category_match=bool(data.get("categoryMatch")),
    )
