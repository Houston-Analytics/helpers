"""
Tests to get relative Python path for imports

@author Arttu Manninen <arttu@kaktus.cc>
"""
import os
import pytest
from helpers import get_relative_module_path

project_path = os.getcwd()
current_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(current_path, os.pardir))
helpers_path = os.path.join(root_path, 'helpers')

test_directory = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'recursive_filelist'
)

class TestGetRelativePath():
    """ Unit tests to get the relative path """
    @staticmethod
    def test_get_relative_module_path_exists():
        """ Verify that there is a callable helper get_relative_module_path """
        assert callable(get_relative_module_path)

    @staticmethod
    def test_get_relative_module_path():
        """ Check that the relative path was resolved correctly """
        assert get_relative_module_path(helpers_path) == 'helpers'
        assert get_relative_module_path(helpers_path + '.py') == 'helpers'

    @staticmethod
    def test_get_relative_module_path_outside_scope():
        """ Test that get_relative_module_path raises an error when outside scope """
        with pytest.raises(FileNotFoundError):
            assert get_relative_module_path('/tmp')
