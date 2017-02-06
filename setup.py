# -*- coding: utf-8 -*-

from setuptools import setup


entry_points = {
    'console_scripts': [
        'rbd = rbd:main',
    ]
}


requires = ['docopt', 'requests', 'six']

setup(
    # General Information
    name='rubberduck',
    version='0.0.8',
    author='Liling Tan',
    author_email='',
    description='Yet another DuckDuckGo Python API',
    url='https://github.com/alvations/rubberduck',
    license='MIT',

    # Add packages, scripts, and other data
    packages=['rubberduck'],
    scripts=['rbd.py'],

    #define requirements and entry points
    install_requires=requires,
    entry_points=entry_points,

    #pypi classifiers
    classifiers=[
         'Development Status :: 4 - Beta',
         'Environment :: Console',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3.5',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
