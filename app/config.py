from smart_getenv import getenv

config = {
    'debug': getenv('DEBUG', type=bool, default=False),

    'messente': {
        'username': getenv('MESSENTE_API_USERNAME'),
        'password': getenv('MESSENTE_API_PASSWORD'),
    }
}


def debug():
    return config['debug']
