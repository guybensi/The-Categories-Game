from __future__ import annotations

from typing import List

_CATEGORIES = [
    "City",
    "Country",
    "Food",
    "Animal",
    "Movie",
    "Song",
    "Sports Team",
    "Famous Person",
    "Brand",
    "Car",
]


def load_categories() -> List[str]:
    """
    Params: none.
    Returns: list of categories.
    Description: Provide the base category list (static or from file).
    Examples:
        Input: none
        Output: ["City", "Country", "Food", "..."]
    """
    return list(_CATEGORIES)


def normalize_category(name: str) -> str:
    """
    Params: category name.
    Returns: normalized category string.
    Description: Normalize category comparisons.
    Examples:
        Input: "  City "
        Output: "city"
    """
    return name.strip().lower()
