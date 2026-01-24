"""
Tests for signal handling in the Provider.
"""

import signal
from unittest.mock import MagicMock, patch

from provider import serve


@patch("provider.grpc.server")
@patch("provider.ShioajiService")
@patch("provider.signal.signal")
def test_serve_registers_signals(mock_signal, mock_service_class, mock_grpc_server):
    """
    Verify that serve() registers handlers for SIGINT, SIGTERM, and SIGQUIT.
    """
    mock_server = mock_grpc_server.return_value
    mock_service_class.return_value = MagicMock()

    # We want serve() to return immediately for testing registration
    mock_server.wait_for_termination.side_effect = KeyboardInterrupt

    try:
        serve()
    except KeyboardInterrupt:
        pass

    # Verify signals registered
    expected_signals = [signal.SIGINT, signal.SIGTERM, signal.SIGQUIT]
    registered_signals = [call.args[0] for call in mock_signal.call_args_list]
    for sig in expected_signals:
        assert sig in registered_signals, f"Signal {sig} was not registered"
