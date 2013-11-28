try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'How much energy does your horse need per day?',
    'author': 'Anita',
    'url': 'localhost:8080',
    'download_url': 'None',
    'author_email': 'anitarn5@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'HorseEnergy'
}

setup(**config)