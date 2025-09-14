import logging
from unittest.mock import patch
from homework_10 import log_event


def test_log_event_success():
    with patch("homework_10.logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        log_event("test_user", "success")

        mock_logger.info.assert_called_once()
        message = mock_logger.info.call_args[0][0]
        assert "Login event" in message
        assert "test_user" in message
        assert "success" in message


def test_log_event_expired():
    with patch("homework_10.logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        log_event("test_user", "expired")

        mock_logger.warning.assert_called_once()
        message = mock_logger.warning.call_args[0][0]
        assert "Login event" in message
        assert "expired" in message


def test_log_event_failed():
    with patch("homework_10.logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        log_event("test_user", "failed")

        mock_logger.error.assert_called_once()
        message = mock_logger.error.call_args[0][0]
        assert "Login event" in message
        assert "failed" in message


def test_log_event_invalid_status():
    with patch("homework_10.logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        log_event("test_user", "something_weird")

        mock_logger.error.assert_called_once()
        message = mock_logger.error.call_args[0][0]
        assert "something_weird" in message