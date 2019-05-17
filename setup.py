from setuptools import setup, find_packages
from os import path
from amb_sdk.version import __version__

setup(
    name='amb_sdk',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='The AMB SDK is a python client for the AMB API.',

    # The project's main homepage.
    url='https://bitbucket.org/sparkcognition/amb-sdk',

    # Author details
    author='Sheila Cheng',
    author_email='scheng@sparkcognition.com',
    install_requires=[
        'validators==0.12.4',
        'urllib3==1.24.1',
        'pandas==0.24.2',
        'requests_toolbelt==0.9.1',
        'requests==2.21.0',
    ],
    packages=['amb_sdk']
)
