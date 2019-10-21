"""
Test get_recursive_filelist

@author Arttu Manninen <arttu@kaktus.cc>
"""
import os
from helpers import get_recursive_filelist
current_path = os.path.dirname(os.path.realpath(__file__))

test_directory = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'recursive_filelist'
)

class TestGetRecursiveFilelist():
    """ Test get_recursive_filelist """
    @staticmethod
    def test_get_recursive_filelist_first_level_match():
        """ Test that get_recursive_filelist finds one of the targets from the root """
        files = get_recursive_filelist(test_directory, filename_filter='.txt')
        found_file = os.path.join(test_directory, 'file1.txt')
        assert found_file in files

    @staticmethod
    def test_get_recursive_filelist_first_level_filter_reject():
        """ Test that get_recursive_filelist rejects a mismatch from the root """
        files = get_recursive_filelist(test_directory, filename_filter='.conf')
        not_found_file = os.path.join(test_directory, 'file1.txt')
        assert not_found_file not in files

    @staticmethod
    def test_get_recursive_filelist_second_level_match():
        """ Test that get_recursive_filelist finds one of the targets from the dir """
        files = get_recursive_filelist(test_directory, filename_filter='.txt')
        found_file = os.path.join(test_directory, 'dir', 'file2.txt')
        assert found_file in files

    @staticmethod
    def test_get_recursive_filelist_second_level_mismatch():
        """ Test that get_recursive_filelist finds one of the targets from the dir """
        files = get_recursive_filelist(test_directory, filename_filter='.conf')
        not_found_file = os.path.join(test_directory, 'dir', 'file2.txt')
        assert not_found_file not in files

    @staticmethod
    def test_get_recursive_filelist_third_level_match():
        """ Test that get_recursive_filelist finds one of the targets from the sub dir """
        files = get_recursive_filelist(test_directory, filename_filter='.txt')
        found_file = os.path.join(test_directory, 'dir', 'subdir', 'file3.txt')
        assert found_file in files

    @staticmethod
    def test_get_recursive_filelist_third_level_mismatch():
        """ Test that get_recursive_filelist finds one of the targets from the sub dir """
        files = get_recursive_filelist(test_directory, filename_filter='.conf')
        not_found_file = os.path.join(test_directory, 'dir', 'subdir', 'file3.txt')
        assert not_found_file not in files

    @staticmethod
    def test_get_recursive_filelist_with_regular_expression():
        """ Test that get_recursive_filelist handles regular expressions """
        files = get_recursive_filelist(test_directory, filename_regex=r'\.txt$')
        found_file = os.path.join(test_directory, 'file1.txt')
        assert found_file in files

    @staticmethod
    def test_get_recursive_filelist_finds_all_files_when_no_filters_present():
        """ Test that get_recursive_filelist finds all files when no filters are present """
        all_files = get_recursive_filelist(test_directory)
        assert len(all_files) == 5
