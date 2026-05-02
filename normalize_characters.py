import unicodedata


# Decompose characters (e.g., í → i + combining accent)
def to_ascii(text):
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))
