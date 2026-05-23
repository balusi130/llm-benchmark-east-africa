def evaluate_response(response: str, expected: str = None) -> float:
    """
    Score a model response against an expected answer.
    Returns a float between 0.0 and 1.0.
    """
    if not expected:
        # No ground truth — return neutral score for human review
        return 0.5

    response_clean = response.strip().lower()
    expected_clean = expected.strip().lower()

    if response_clean == expected_clean:
        return 1.0

    # Partial credit: check if key phrases are present
    expected_tokens = set(expected_clean.split())
    response_tokens = set(response_clean.split())
    overlap = expected_tokens & response_tokens

    if not expected_tokens:
        return 0.0

    return len(overlap) / len(expected_tokens)
