"""
Get recursive filelist

@author Arttu Manninen <arttu@kaktus.cc>
"""
import os
import re

def get_recursive_filelist(
        target_folder: str,
        filename_filter: str = None,
        filename_regex: re = None
) -> list:
    """ Get recursive filelist in the target folder with optional filename filter """
    matched_files = []
    for root_path, _directories, files in os.walk(target_folder):
        for file in files:
            full_path_to_file = os.path.join(root_path, file)

            if filename_filter is not None:
                if filename_filter in full_path_to_file:
                    matched_files.append(full_path_to_file)
                continue

            if filename_regex is not None:
                if isinstance(filename_regex, str):
                    filename_regex = re.compile(filename_regex)

                if filename_regex.search(full_path_to_file):
                    matched_files.append(full_path_to_file)
                continue

            matched_files.append(full_path_to_file)

    return matched_files
