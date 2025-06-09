import math
import re


def is_number(txt):
    """
    Check if a string represents a valid number (integer, decimal, or with commas).
    """
    if not isinstance(txt, str):
        return False
    try:
        float(txt.replace(",", ""))
        return True
    except ValueError:
        return False


def round_to_two_significant_digits(number_str):
    """
    Round a number string to two significant digits.

    Args:
        number_str (str): String representing a number (e.g., "301,230", "1,836.4").

    Returns:
        float: The number rounded to two significant digits.
    """
    try:
        number = float(number_str.replace(",", ""))
        if number == 0:
            return 0.0
        p = math.floor(math.log10(abs(number)))
        d = 1 - p  # For 2 significant digits
        rounded = round(number, d)
        return rounded
    except (ValueError, OverflowError):
        return number_str  # Return original if conversion fails


def process_text_numbers(text):
    """
    Find all numbers in the text, round them to two significant digits, and replace them.

    Args:
        text (str): Input text containing numbers.

    Returns:
        str: Text with all numbers rounded to two significant digits.
    """
    # Regular expression to match numbers (integers, decimals, with optional commas)
    number_pattern = r'-?\b\d{1,3}(,\d{3})*(\.\d+)?\b'

    def replace_number(match):
        num_str = match.group(0)
        if is_number(num_str):
            rounded = round_to_two_significant_digits(num_str)
            # Format as integer if no decimal part, else keep as float
            if rounded.is_integer():
                return str(int(rounded))
            return str(rounded)
        return num_str

    # Replace all numbers in the text
    return re.sub(number_pattern, replace_number, text)