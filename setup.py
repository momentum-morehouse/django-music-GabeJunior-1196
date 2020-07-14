# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['music']

package_data = \
{'': ['*']}

install_requires = \
['django-debug-toolbar>=2.2,<3.0',
 'django-environ>=0.4.5,<0.5.0',
 'django-extensions>=2.2.9,<3.0.0',
 'django>=3.0.6,<4.0.0',
 'werkzeug>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'music',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
