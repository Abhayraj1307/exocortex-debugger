def extract_traceback(stderr: str) -> str:
    """
    Given the full stderr string from running code,
    return just the traceback part if it exists.
    Otherwise, return stderr unchanged.
    """
    marker = "Traceback (most recent call last):"
    if marker in stderr:
        idx = stderr.index(marker)
        return stderr[idx:]
    return stderr
