"""
Miscellaneous helper functions

@author Arttu Manninen <arttu@kaktus.cc>
"""
import setuptools

description = 'Miscellaneous helpers'

with open('README.md', 'r') as readme:
    long_description = readme.read()

packages = setuptools.find_packages(
    '.',
    exclude=[
        'tests',
        'tests.*'
    ]
)

setuptools.setup(
    name='helpers',
    version='0.0.3',
    author='Arttu Manninen',
    author_email='arttu@kaktus.cc',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adrenalin/helpers',
    packages=packages,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)