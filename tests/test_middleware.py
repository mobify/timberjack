from unittest.mock import Mock

from timberjack.middleware import LoggingMiddleware


def test_logging_middleware_creates_logger(rf):
    request = rf.get('/')
    request.session = Mock(session_key='randomsessionkey')

    LoggingMiddleware().process_request(request)

    assert hasattr(request, 'log')
