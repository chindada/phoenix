"""
Tests for signal handling in the Provider.
"""

import signal

from provider import serve


def test_serve_registers_signals(mocker):
    """
    Verify that serve() registers handlers for SIGINT, SIGTERM, and SIGQUIT
    and that the handler performs logout and stop.
    """
    # Patch dependencies
    mock_grpc_server = mocker.patch("provider.grpc.server")
    mock_server = mock_grpc_server.return_value

    mock_service_class = mocker.patch("provider.ShioajiService")
    mock_service = mock_service_class.return_value
    mock_service.logged_in = True

    mock_signal = mocker.patch("provider.signal.signal")

    # We want serve() to return immediately for testing registration
    mock_server.wait_for_termination.side_effect = KeyboardInterrupt

    try:
        serve()
    except KeyboardInterrupt:
        pass

    # 1. Verify signals registered
    expected_signals = [signal.SIGINT, signal.SIGTERM, signal.SIGQUIT]
    registered_handlers = {}
    for call in mock_signal.call_args_list:
        sig, handler = call.args
        registered_handlers[sig] = handler

    for sig in expected_signals:
        assert sig in registered_handlers, f"Signal {sig} was not registered"

    # 2. Verify shutdown_handler logic
    handler = registered_handlers[signal.SIGINT]
    handler(signal.SIGINT, None)

    # Verify logout called
    mock_service.client.logout.assert_called_once()
    # Verify server stopped
    mock_server.stop.assert_called_once_with(0)
