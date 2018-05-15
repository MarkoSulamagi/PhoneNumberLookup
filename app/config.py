from smart_getenv import getenv

config = {
    'debug': getenv('DEBUG', type=bool, default=False),

    'messente': {
        'username': getenv('MESSENTE_USERNAME'),
        'password': getenv('MESSENTE_PASSWORD'),
    }
}


def debug():
    return config['debug']
