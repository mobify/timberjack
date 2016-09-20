import structlog


def get_logger(name=None, *args, **kwargs):
    """
    Get a new logger with a default name `brain` if none is specified.
    """
    if not name:
        name = 'brain'
    return structlog.get_logger(name, *args, **kwargs)
