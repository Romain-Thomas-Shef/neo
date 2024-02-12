from setuptools import setup

__version__ = '23.11.1'
__place__ = 'Sheffield University'
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__maintainer__ = "Romain Thomas"
__email__ = "romain.thomas@sheffield.ac.uk"
__status__ = "released"

setup(
   name = 'Neo',
   version = __version__,
   author = __credits__,
   packages = ['neo'],
   entry_points = {'gui_scripts': ['neo = neo.__main__:main',],},
   description = 'A simple RSE skills matrix reader and visualisation tool',
   license = __license__,
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.14.3",
       "openpyxl >= 1.26.2",
       "matplotlib >= 3.8.1",
   ],
   include_package_data=True,
)
