Convert NumPy/SciPy arrays and Pandas Dataframes to formatted LaTeX arrays
==========================================================================

.. image:: https://github.com/josephcslater/array_to_latex/actions/workflows/test.yml/badge.svg
    :target: https://github.com/josephcslater/array_to_latex/actions/workflows/test.yml

.. image:: https://badge.fury.io/py/array-to-latex.png/
    :target: http://badge.fury.io/py/array-to-latex

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/josephcslater

.. image:: http://pepy.tech/badge/array-to-latex
   :target: http://pepy.tech/project/array-to-latex
   :alt: PyPi Download stats

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb

The module ``array_to_latex`` converts a NumPy/SciPy array or Pandas Numerical DataFrame to a LaTeX 
array or table using `Python 3.x style`_ formatting of the result or a format usable for plotting within LaTeX using pgfplots. Note that as of *0.83* it **does** add 
the column formatting arguments (for example, `{ccc...}`) when the user chooses to use `array`. I'm happy 
to have someone create a better solution but this at least makes a copied array immediately usable. I 
prefer `bmatrix` or similar. `

Play with it on `mybinder.org`_!

A NumPy-focused re-envisioned converter based, in part, on this is 
`numpyarray_to_latex <https://github.com/benmaier/numpyarray_to_latex>`_. Also, available 
*pip install*. It incorporates more sophisticated "sub" markup capabilities. Check it out!

| *1.0.1*: Fix empty-array/DataFrame LaTeX corruption bug, migrate packaging to
|          ``pyproject.toml``, add type hints, ``ruff`` linting, and coverage reporting.
| *1.0.0*: Validate ``arraytype``, fix docstring/doctest inaccuracies, remove unused
|          ``nargout`` parameter (breaking), make ``clipboard`` an optional install
|          extra, add unit tests and GitHub Actions CI.

See `CHANGELOG.md`_ for the full version history.

Install using ``pip install --user array_to_latex`` from your command prompt, **not the Python prompt**. If you want to use ``to_clp`` to copy results directly to your clipboard, install the optional extra with ``pip install --user array_to_latex[clipboard]``.

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
    latex_code = a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'bmatrix', print_out=False)

will put the LaTeX code into variable ``latex_code``.

.. code:: python

    import numpy as np
    import array_to_latex as a2l
    A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    a2l.to_clp(A, frmt = '{:6.2f}', arraytype = 'bmatrix')

will put the array onto your clipboard.

If you will be using the same conversion over and over, you can define your own by using a ``lambda`` function:

.. code:: python

    to_tex = lambda A : a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'bmatrix', mathform=True)
    to_tex(A)

so you can now use your function ``to_tex`` repeatedly with your specified settings. More detailed information on usage is in the help.

.. code:: python

    import array_to_latex as a2l
    help(a2l.to_ltx)

Interesting alternative approaches are `np_array_to_latex <https://github.com/bbercovici/np_array_to_latex>`_ and `tab2latex (convert numpy array to longtable file) <https://pypi.org/project/tab2latex/>`_.

Like this module, `buy me a coffee! <https://www.buymeacoffee.com/s6BCSuEiU>`_. 

.. _`Python 3.x style`: https://docs.python.org/3.7/library/string.html
.. _`mybinder.org`: https://mybinder.org/v2/gh/josephcslater/array_to_latex/master?filepath=Examples.ipynb
.. _`CHANGELOG.md`: https://github.com/josephcslater/array_to_latex/blob/master/CHANGELOG.md
