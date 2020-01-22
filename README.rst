Convert NumPy/SciPy arrays and Pandas Dataframes to formatted LaTeX arrays
==========================================================================

.. image:: https://badge.fury.io/py/array-to-latex.png/
    :target: http://badge.fury.io/py/array-to-latex

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/josephcslater

.. image:: http://pepy.tech/badge/array-to-latex
   :target: http://pepy.tech/project/array-to-latex
   :alt: PyPi Download stats

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb

The module ``array_to_latex`` converts a NumPy/SciPy array or Pandas Numerical DataFrame to a LaTeX array or table using `Python 3.x style`_ formatting of the result.

Play with it on `mybinder.org`_!

Recent updates follow, with a more complete list towards the end of this document. If you don't see the current version in this list it's likely because I (again) forgot to update it when pushing out a new version. Please see the `readme`_ on GitHub.

| *0.80*: Return to previous interface while still enabling returned
|         LaTeX string.
| *0.81*: Bug fixes in requirements and to_clp
| *0.82*: Raise ImportError exception when incorrect datatype used.

Install using ``pip install --user array_to_latex`` from your command prompt, **not the Python prompt**.

Please read the help. It explains all options. To try it, see `the online mybinder.org demo <https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb>`_. It documents illustrates application to numerical Pandas DataFrames.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')

will print the LaTeX code to your output.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    latex_code = a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')

will put the LaTeX code into variable ``latex_code``.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    a2l.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

will put the array onto your clipboard.

If you will be using the same conversion over and over, you can define your own by using a ``lambda`` function:

.. code:: python

    to_tex = lambda A : a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array', mathform=True)
    to_tex(A)

so you can now use your function ``to_tex`` repeatedly with your specified settings. More detailed information on usage is in the help.

.. code:: python

    import array_to_latex as a2l
    help(a2l.to_ltx)

Interesting alternative approaches are `np_array_to_latex <https://github.com/bbercovici/np_array_to_latex>`_ and `tab2latex (convert numpy array to longtable file) <https://pypi.org/project/tab2latex/>`_.

Like this module, `buy me a coffee! <https://www.buymeacoffee.com/s6BCSuEiU>`_

| *New in* 0.37: Now handles complex arrays.
| *New in* 0.38: Aligns columns neatly.
| **0.40: Critical upgrade- 0.37-0.38 formatted incorrectly.**
| **0.41: Critical upgrade- 0.37-0.40 formatted incorrectly.**
| *New in* 0.43: Now handles 1-D Arrays. See new option ``row``
| *New in* 0.50: Now works with Pandas DataFrames
| *0.51*: Bug fix- remove extra blank lines in DataFrame tabular output
| *0.52*: A few documentation typos fixed. No code changed.
| *0.60*: Now handles strings in Pandas Dataframes. Fixes bug in exponentials and handling of exponentials. Please report errors!
| *0.61*: Minor documentation improvements. No code changed.
| *0.70*: Added ``mathform``. When set to ``True`` (default), returns 10 to superscript form.
| *0.71*: Line breaks broke ``readme.rst`` on ``pypi``. No code change.
| *0.72*: Line breaks broke ``readme.rst`` on ``pypi``. No code change.
| *0.73*: pypi won't handle mathjax. It makes me sad. No code change.
| *0.74*: Not released
| *0.75*: output improvements (short-lived release)
| *0.76*: Printing made better, allows outputs, added ``print_out``
|         boolean to turn off printing
| *0.80*: Return to previous interface while still enabling returned
|         LaTeX string.
| *0.81*: Bug fixes in requirements and to_clp
| *0.82*: Raise ImportError exception when incorrect datatype used.

.. _`Python 3.x style`: https://docs.python.org/3.7/library/string.html
.. _`mybinder.org`: https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb
.. _`readme`: https://github.com/josephcslater/array_to_latex/blob/master/README.rst
