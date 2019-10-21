"""
Get relative module path for a file path

@author Arttu Manninen <arttu@kaktus.cc>
"""
import os
import re

def get_relative_module_path(full_path: str) -> str:
    """ Get relative module path """
    full_path_without_suffix = re.sub(r'\.py$', '', full_path)

    project_root = os.getcwd()
    if project_root not in full_path_without_suffix:
        raise FileNotFoundError('Cannot get relative module path for %s' % (full_path))

    relative_path = re.sub('^/', '', full_path_without_suffix[len(project_root):])

    module_path_format = re.sub('/', '.', relative_path)
    return module_path_format
