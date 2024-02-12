'''
The NEO module allows you to visualise a skills matrix
with polar diagrams and spider plots.
You can see the documentation at:

Author: R. Thomas
Place: U. of Sheffield
Year: 2023
Licence: GPLv3
Pylint v3.0.3 score: 10
'''


__all__ = ["GeneralMatrix", 'make_training', 'make_matrix_barplot', 'make_matrix_spiderplot']

from .read_skills_matrix import GeneralMatrix
from .plot_matrix import make_matrix_barplot, make_training, make_matrix_spiderplot
