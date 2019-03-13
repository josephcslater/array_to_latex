Convert NumPy/SciPy arrays to formatted LaTeX arrays
====================================================

.. image:: https://badge.fury.io/py/array_to_latex.png/
    :target: http://badge.fury.io/py/array_to_latex

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/josephcslater

.. image:: http://pepy.tech/badge/array-to-latex
   :target: http://pepy.tech/project/array-to-latex
   :alt: PyPi Download stats

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb


The package ``array_to_latex`` converts a NumPy/SciPy array to a LaTeX
array including `Python 3.x
style <https://mkaz.blog/code/python-string-format-cookbook/>`__ (or `alternatively <https://www.python-course.eu/python3_formatted_output.php>`__) formatting of the result.

Play with it on `mybinder.org <https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb>`_!

| *New in* 0.37: Now handles complex arrays.
| *New in* 0.38: Aligns columns neatly.
| **0.40: Critical upgrade- 0.37-0.38 formatted incorrectly.**
| **0.41: Critical upgrade- 0.37-0.40 formatted incorrectly.**
| *New in* 0.43: Now handles 1-D Arrays. See new option ``row``
| *New in* 0.50: Now works with Pandas DataFrames
| *0.51: Bug fix- remove extra blank lines in DataFrame tabular output

Install using ``pip install --user array_to_latex`` from your command prompt, **not the Python prompt**.

Please read the help. It explains all options. To try it, see `the online mybinder.org demo <https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb>`_. It documents illustrates application to numerical Pandas DataFrames.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')

will print the LaTeX code to your ouput.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    a2l.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

will put the array onto your clipboard.

More detailed information on usage is in the help.

.. code:: python

    import array_to_latex as a2l
    help(a2l.to_ltx)

An interesting alternative approach is `np array to latex <https://github.com/bbercovici/np_array_to_latex>`_.

Like this module, `buy me a coffee! <https://www.buymeacoffee.com/s6BCSuEiU>`_
