# simple setup script, that installs the package

from setuptools import setup, find_packages

setup(
    name='skfcl',
    version='0.1',
    packages=['skfcl'],
    install_requires=['ply', 'scikit-fuzzy'],
    package_dir={
        'skfcl': '.',
    },

)
