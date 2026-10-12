"""
Utility functions and helpers.
"""
import re
import hashlib

def hash_password(password: str) -> str:
    # FIXME: Use bcrypt instead of sha256 for passwords
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def validate_email(email: str) -> bool:
    # TODO: Improve regex to RFC 5322 compliance
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# DEPRECATED: Do not use in new endpoints
def legacy_formatter(data: dict) -> str:
    """Old XML formatter. Deprecated since v2.1.0."""
    return f"<data>{data}</data>"
