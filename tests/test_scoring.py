def test_score_valid_fast() -> None:
    """
    Params: none.
    Returns: None.
    Description: Fast valid answer gets higher score.
    Examples:
        Input: valid=True, response_ms=1000
        Output: score > 15
    """
    pass


def test_score_valid_slow() -> None:
    """
    Params: none.
    Returns: None.
    Description: Slow valid answer gets lower score.
    Examples:
        Input: valid=True, response_ms=25000
        Output: score close to 10
    """
    pass


def test_score_invalid() -> None:
    """
    Params: none.
    Returns: None.
    Description: Invalid answer scores zero.
    Examples:
        Input: valid=False, response_ms=1000
        Output: 0
    """
    pass


def test_time_bonus_floor() -> None:
    """
    Params: none.
    Returns: None.
    Description: Bonus does not go below zero.
    Examples:
        Input: response_ms=60000
        Output: 0
    """
    pass
