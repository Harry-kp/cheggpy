"""Setup file for Cheggbot package."""
from setuptools import setup, find_packages

setup(
    name='cheggbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
    ],
    author='Harry-kp',
    author_email='chaudharyharshit9@gmail.com',
    description='A Python package for interacting with Chegg API.',
    url='https://github.com/Harry-kp/cheggpy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
