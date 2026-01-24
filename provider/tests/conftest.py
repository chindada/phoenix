"""
Pytest configuration and fixtures.
"""

import pytest

from provider import ShioajiService


@pytest.fixture
def mock_shioaji_client(mocker):
    """Fixture to patch ShioajiClient."""
    # Patch ShioajiClient in server.py
    # We use a lambda to return the mock, or patch it directly.
    # mocker.patch works on the name where it's imported.
    mock = mocker.patch("provider.ShioajiClient", autospec=True)
    return mock.return_value


@pytest.fixture
def service(_mock_shioaji_client):  # pylint: disable=invalid-name
    """Fixture to create ShioajiService instance."""
    # Initialize ShioajiService which will use the mocked ShioajiClient
    return ShioajiService()
