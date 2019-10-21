"""
Get a generic URL formatted connection string from the given arguments

@author Arttu Manninen <arttu@kaktus.cc>
"""
import re
import urllib
from helpers.errors import InvalidArguments

def get_connection_string( # pylint: disable=too-many-arguments
        protocol: str = '',
        username: str = '',
        password: str = '',
        host: str = '',
        port: 'Union(str, int)' = '',
        name: str = '',
        query: dict = None,
        relative: bool = False
) -> str:
    """ Format the database connection string """
    if not relative:
        assert protocol

    if username and password:
        authentication_string = '%s:%s@' % (username, password)
    elif username:
        authentication_string = '%s@' % (username)
    elif password:
        raise InvalidArguments('Cannot give password without username')
    else:
        authentication_string = ''

    if host or port or authentication_string:
        if port:
            hostname = '%s:%s' % (
                host or 'localhost',
                port
            )
        else:
            hostname = host or 'localhost'
    else:
        hostname = ''

    query_string = ''

    if query:
        query_string = '?' + urllib.parse.urlencode(query)

    url = '/' + re.sub(r'^\/', '', name) + query_string

    if relative:
        return url

    # url = context.get_x_argument(as_dictionary=True).get('url')
    connection_string = f'{protocol}://{authentication_string}{hostname}{url}'

    return connection_string
