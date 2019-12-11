import logging
from models.settings.config import init_config


def init_app():
    try:
        init_config()
        pass
    except Exception as e:
        logging.error('Init app error {0}'.format(e))


if __name__ == '__main__':
    init_app()