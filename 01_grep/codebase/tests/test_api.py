"""
Unit tests for API and utils.
"""
import pytest
from utils import validate_email, hash_password

def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("user.name+tag@sub.domain.org") is True

def test_validate_email_invalid():
    assert validate_email("plainaddress") is False
    assert validate_email("@missinguser.com") is False

# TODO: Write tests for database mock failures
@pytest.mark.skip(reason="Not implemented yet")
def test_db_timeout():
    pass
