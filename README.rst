Convert Numpy/Scipy arrays to formatted LaTeX arrays
====================================================

The package ``array_to_latex`` converts a Numpy/Scipy array to a LaTeX
array including `Python 3.x
style <https://mkaz.tech/python-string-format.html>`__ formating of the
result.

Install using ``pip install --user array_to_latex``

Please read the help which explains usage.

.. code:: python

    import numpy as np
    import array_to_latex as ar
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    ar.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')

will print the LaTeX code to your ouput.

.. code:: python

    import numpy as np
    import array_to_latex as ar
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    ar.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

will put the array onto your clipboard.

More detailed information on usage is in the help.

.. code:: python

    import array_to_latex as ar
    help(ar.to_ltx)
