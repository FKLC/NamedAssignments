import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='namedassignments',
    version='1.0.0',
    description='Really small library to implement NamedExpressions in Python 3.8 to older versions of Python.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/FKLC/NamedAssignments',
    author='Fatih Kılıç',
    author_email='m.fatihklc0@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=['namedassignments'],
    install_requires=[]
)
