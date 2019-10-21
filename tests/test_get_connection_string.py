""" Test database source schema role access """
import pytest
from helpers import get_connection_string # pylint: disable=wrong-import-position
from helpers.errors import InvalidArguments

class TestHelpersFormatConnectionString():
    """ Test database source schema role access """
    @staticmethod
    def test_get_connection_string_with_name():
        """ Test connection string with database name """
        assert get_connection_string(
            protocol='test',
            name='aistest'
        ) == 'test:///aistest'

    @staticmethod
    def test_get_connection_string_with_name_and_host():
        """ Test connection string with database name and host """
        assert get_connection_string(
            protocol='test',
            host='localhost',
            name='aistest'
        ) == 'test://localhost/aistest'

    @staticmethod
    def test_get_connection_string_with_name_and_host_and_port():
        """ Test connection string with database name, host and port """
        assert get_connection_string(
            protocol='test',
            host='localhost',
            port='5433',
            name='aistest'
        ) == 'test://localhost:5433/aistest'

    @staticmethod
    def test_get_connection_string_with_name_and_port():
        """ Test connection string with resource name and port """
        assert get_connection_string(
            protocol='test',
            port='5433',
            name='aistest'
        ) == 'test://localhost:5433/aistest'

    @staticmethod
    def test_get_connection_string_handles_first_url_slash():
        """ Test that connection string handles the possible first slash in a URL """
        assert get_connection_string(
            protocol='test',
            port='5433',
            name='/aistest'
        ) == 'test://localhost:5433/aistest'

    @staticmethod
    def test_get_connection_string_with_name_and_host_and_port_and_username():
        """ Test connection string with resource name, host, port and username """
        assert get_connection_string(
            protocol='test',
            username='foo',
            host='localhost',
            port='5433',
            name='aistest'
        ) == 'test://foo@localhost:5433/aistest'

    @staticmethod
    def test_get_connection_string_with_query():
        """ Test connection string with query """
        assert get_connection_string(
            protocol='test',
            username='foo',
            password='bar',
            host='localhost',
            port='5433',
            name='aistest',
            query={
                'query_key': 'query_value'
            }
        ) == 'test://foo:bar@localhost:5433/aistest?query_key=query_value'

    @staticmethod
    def test_get_connection_string_with_all_details():
        """ Test connection string with all details """
        assert get_connection_string(
            protocol='test',
            username='foo',
            password='bar',
            host='localhost',
            port='5433',
            name='aistest'
        ) == 'test://foo:bar@localhost:5433/aistest'

        assert get_connection_string(
            protocol='test',
            username='foo',
            name='aistest'
        ) == 'test://foo@localhost/aistest'

    @staticmethod
    def test_get_connection_string_failing_with_password_without_username():
        """ Test exception handling when there is a password without username """
        with pytest.raises(InvalidArguments):
            get_connection_string(
                protocol='test',
                password='bar',
                host='localhost'
            )

    @staticmethod
    def test_get_connection_string_raises_assertation_error_without_protocol():
        """ Test that get_connection_string raises an AssertionError without protocol """
        with pytest.raises(AssertionError):
            get_connection_string(host='localhost')

    @staticmethod
    def test_get_connection_string_relative_returns_relative():
        """ Test that get_connection_string can return a relative string """
        assert get_connection_string(
            name='/test/relative',
            relative=True
        ) == '/test/relative'
