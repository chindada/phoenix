from unittest.mock import MagicMock

import grpc
import provider_pb2


def test_login_success(service, mock_shioaji_client):
    # Setup mock
    mock_acc = MagicMock()
    mock_acc.account_type = "S"
    mock_acc.person_id = "A123456789"
    mock_acc.broker_id = "9A00"
    mock_acc.account_id = "1234567"
    mock_acc.username = "testuser"
    mock_acc.signed = True

    mock_shioaji_client.login.return_value = [mock_acc]

    # Execute
    request = provider_pb2.LoginRequest(api_key="key", secret_key="secret")
    context = MagicMock()
    response = service.Login(request, context)

    # Verify
    mock_shioaji_client.login.assert_called_once_with("key", "secret")
    assert len(response.accounts) == 1
    assert response.accounts[0].account_id == "1234567"
    assert response.accounts[0].person_id == "A123456789"


def test_login_failure(service, mock_shioaji_client):
    # Setup mock to raise exception
    mock_shioaji_client.login.side_effect = Exception("Login failed")

    # Execute
    request = provider_pb2.LoginRequest(api_key="key", secret_key="secret")
    context = MagicMock()
    service.Login(request, context)

    # Verify
    context.abort.assert_called_once_with(grpc.StatusCode.INTERNAL, "Login failed")


def test_list_accounts(service, mock_shioaji_client):
    mock_acc = MagicMock()
    mock_acc.account_type = "F"
    mock_acc.person_id = "A123456789"
    mock_acc.broker_id = "F000"
    mock_acc.account_id = "7654321"
    mock_acc.username = "testuser"
    mock_acc.signed = False

    mock_shioaji_client.list_accounts.return_value = [mock_acc]

    request = provider_pb2.Empty()
    context = MagicMock()
    response = service.ListAccounts(request, context)

    mock_shioaji_client.list_accounts.assert_called_once()
    assert len(response.accounts) == 1
    assert response.accounts[0].account_id == "7654321"
    assert response.accounts[0].account_type == "F"
