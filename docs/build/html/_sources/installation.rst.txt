.. _installation:

Installation
============

Neo was written is written in python 3.10. It needs only the following libraries:

* Numpy v1.26.2 or higher: Numerical python
* openpyxl v3.1.2: Excel sheets reader
* matplotlib v3.8.1: Plotting library

Other libraries are used, but they are all part of the standard python library. As such no extra installations are needed.

1-from the python repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last neo version is v24.1.1 (1st version of January 2024) and is available in the main pypi repository. To install it::

     pip install neo_skills --user

Using this command will allow you not to have to install any other package. Pip will install what is missing for you.


2-From the github repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The installable package can be found in the github directory under the ''dist'' directory. Take the last version and run::

	pip install neo-X.Y.Z.tar.gz --user

This will install neo.

In the version number of neo, X is the year, Y is the month, and Z is the number of revisions in that month. Therefore 24.1.1 means, first revision of January 2024.



.. warning::

	**Licence**

	Neo is a free software: you can redistribute it and/or modify it under
	the terms of the GNU General Public License as published by the Free Software Foundation,
	version 3 of the License.

	dfitspy is distributed without any warranty; without even the implied warranty of merchantability
	or fitness for a particular purpose.  See the GNU General Public License for more details.

	You should have received a copy of the GNU General Public License along with the program.
	If not, see http://www.gnu.org/licenses/ .

