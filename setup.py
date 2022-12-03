from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in planning/__init__.py
from planning import __version__ as version

setup(
	name="planning",
	version=version,
	description="Sistema de planeacion con base en LTO, OKRs, FODA, mapa estrategico y demas herramientas",
	author="buzola",
	author_email="it@buzola.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
