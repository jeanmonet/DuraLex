from setuptools import setup

setup(
    name='DuraLex',
    version='0.2',
    install_requires=[
        'html5lib',
        'simplejson',
        'beautifulsoup4'
    ],
    packages=[
        'duralex'
    ],
    scripts=[
        'bin/duralex'
    ]
)
