"""
Test get_value

@author Arttu Manninen <arttu@kaktus.cc>
"""
import pytest
from helpers import get_value

class TestGetValue():
    """ Test get_value """
    @staticmethod
    def test_get_value_is_callable():
        """ Test that get_value is callable """
        assert callable(get_value)

    @staticmethod
    def test_get_value_returns_original_value_when_no_path_provided():
        """ Test that get_value returns original value when path is not provided """
        assert get_value(123) == 123

    @staticmethod
    def test_get_value_returns_shallow_object_by_reference():
        """ Test that get_value returns a shallow object by reference """
        test_value = {
            'foo': {
                'bar': True
            }
        }

        assert get_value(test_value, 'foo') is test_value['foo']

    @staticmethod
    def test_get_value_returns_default_when_path_not_found():
        assert get_value({}, 'foo', default='bar') == 'bar'

    @staticmethod
    def test_get_value_returns_deep_path_value_by_reference():
        """ Test that get_value returns deep path value by reference """
        test_value = {
            'foo': {
                'bar': [
                    True,
                    False
                ]
            }
        }

        assert get_value(test_value, 'foo.bar') is test_value['foo']['bar']

    @staticmethod
    def test_get_value_returns_deep_path_by_reference_from_list():
        """ Test that get_value returns deep path value by reference from list """
        test_value = {
            'foo': {
                'bar': [
                    True,
                    False
                ]
            }
        }

        assert get_value(test_value, ['foo', 'bar']) is test_value['foo']['bar']

    @staticmethod
    def test_get_value_raises_exception_when_invalid_path_type():
        """ Test that get_value returns deep path value by reference from set """
        with pytest.raises(AssertionError):
            get_value({}, set(['foo', 'bar']))
