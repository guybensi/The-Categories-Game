def test_valid_city_cairo() -> None:
    """
    Params: none.
    Returns: None.
    Description: Accept a valid city with correct letter.
    Examples:
        Input: answer="Cairo", letter="C", category="City"
        Output: valid=True
    """
    pass


def test_invalid_city_country() -> None:
    """
    Params: none.
    Returns: None.
    Description: Reject a country when category is city.
    Examples:
        Input: answer="Chile", letter="C", category="City"
        Output: valid=False
    """
    pass


def test_correction_applied() -> None:
    """
    Params: none.
    Returns: None.
    Description: Accept a misspelling corrected by Groq.
    Examples:
        Input: answer="Caihiro", letter="C", category="City"
        Output: corrected="Cairo", valid=True
    """
    pass
