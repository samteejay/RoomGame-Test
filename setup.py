try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Samuel Tijani',
	'url': 'No URL',
	'download_url': 'Just local',
	'author_email': 'omalitijanisam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': ['bin/testscript.txt'],
	'name': 'ex47'
}

setup(**config)