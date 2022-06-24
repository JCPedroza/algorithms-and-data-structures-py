import re


def normalize(text: str) -> str:
    return re.sub(r"[\s.:,;!?]", "", text).casefold()


def is_palindrome(text: str) -> bool:
    """Check if the string is a palindrome.

    Time complexity:
    Space complecity:

    Args:
        text: String to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    normalized_text = normalize(text)
    return normalized_text == normalized_text[::-1]


algorithm = is_palindrome
name = "simple"
