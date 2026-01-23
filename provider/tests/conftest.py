"""
Pytest configuration and fixtures.
"""

import os
import sys

import pytest

# Ensure provider/src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# pylint: disable=wrong-import-position
from server import ShioajiService


@pytest.fixture
def mock_shioaji_client(mocker):
    """Fixture to patch ShioajiClient."""
    # Patch ShioajiClient in server.py
    # We use a lambda to return the mock, or patch it directly.
    # mocker.patch works on the name where it's imported.
    mock = mocker.patch("server.ShioajiClient", autospec=True)
    return mock.return_value


@pytest.fixture
def service(mock_shioaji_client):  # pylint: disable=redefined-outer-name, unused-argument
    """Fixture to create ShioajiService instance."""
    # Initialize ShioajiService which will use the mocked ShioajiClient
    return ShioajiService()
