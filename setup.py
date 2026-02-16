# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rsa']

package_data = \
{'': ['*']}

install_requires = \
['pyasn1>=0.1.3']

entry_points = \
{'console_scripts': ['pyrsa-decrypt = rsa.cli:decrypt',
                     'pyrsa-encrypt = rsa.cli:encrypt',
                     'pyrsa-keygen = rsa.cli:keygen',
                     'pyrsa-priv2pub = rsa.util:private_to_public',
                     'pyrsa-sign = rsa.cli:sign',
                     'pyrsa-verify = rsa.cli:verify']}

setup_kwargs = {
    'name': 'rsa',
    'version': '4.9.1',
    'description': 'Pure-Python RSA implementation',
    'author': 'Sybren A. Stüvel',
    'author_email': 'sybren@stuvel.eu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://stuvel.eu/rsa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
