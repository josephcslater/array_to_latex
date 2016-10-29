
Convert Numpy/Scipy arrays to formatted LaTeX arrays
------------------------------------------------------

`array_to_latex` converts a Numpy/Scipy array to a LaTeX array including
python (c) style formating of the result.

Install using `pip install --user array_to_latex`

Please read the help which explains usage.

.. code-block:: python:

  >>> import numpy as np
  >>> import array_to_latex as ar
  >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
  >>> ar.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')

will print the latex code to your ouput.

  .. code-block:: python:

>>> import numpy as np
  >>> import array_to_latex as ar
  >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
  >>> ar.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

will put the array onto your clipboard.

More detailed information on usage is in the help.
