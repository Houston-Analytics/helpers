"""
Get a value by path in a dictionary

@author Arttu Manninen <arttu@kaktus.cc>
"""
def get_value(obj, path=None, default=None):
    """ Get in dictionary """
    if not path:
        return obj

    if isinstance(path, str):
        path = path.split('.')

    if not isinstance(path, list):
        raise AssertionError('Path is not a string or a list')

    key = path.pop(0)
    if key not in obj:
        return default

    if not path:
        return obj[key]

    return get_value(obj[key], path=path, default=default)
