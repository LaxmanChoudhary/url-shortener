import random
import string
from urllib.parse import urlparse

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def preprocess_url(url):
    """Ensure the URL has a valid scheme."""
    parsed = urlparse(url)
    if not parsed.scheme:
        return 'https://' + url
    return url
