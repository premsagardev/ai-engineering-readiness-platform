import re
import unicodedata

def clean_text(raw_text: str) -> str:
    """
    Clean the given text by removing all non-alphanumeric characters except spaces.

    Args:
        raw_text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text with only alphanumeric characters and spaces.
    """
    cleaned_text = raw_text

    # Pass 1: Strip leading/trailing whitespace from the entire document
    cleaned_text = cleaned_text.strip()

    # Pass 2: Remove junk characters (non-printable control characters)
    # Filter out control characters (Cc category) like \x00, \x01, etc.
    cleaned_text = ''.join(char for char in cleaned_text if unicodedata.category(char) != 'Cc')

    # Pass 3: Normalize bullet symbols (replace various symbols with a consistent one: '*')
    bullet_patterns = ['•', '–', '—', '●']
    for pattern in bullet_patterns:
        # Use '* ' for consistency in list items
        cleaned_text = cleaned_text.replace(pattern, '* ')

    # Pass 4: Ensure section headers are formatted reasonably
    # Crude heuristic: If a lowercase letter is followed immediately by an uppercase letter, 
    # it might be a run-on sentence or a header issue. Add a period and a space.
    cleaned_text = re.sub(r'([a-z])([A-Z])', r'\1. \2', cleaned_text)
    
    # Pass 5: Replace multiple newlines with max 2 (ensuring paragraphs are separated by one blank line)
    # The pattern r'\n{3,}' matches 3 or more consecutive newlines
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)
    
    # Pass 6: Normalize general excess whitespace within lines
    cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text).strip()

    return cleaned_text