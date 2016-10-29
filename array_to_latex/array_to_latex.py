
def to_clp(a, frmt='{:1.2f}', arraytype = 'bmatrix'):
    """
    Returns a LaTeX array the the clipboard given a numpy array

    Parameters
    ----------
    a         : array
    frmt      : python 3 formatter, optional
                https://mkaz.tech/python-string-format.html
    arraytype : latex array type- `bmatrix` default, optional

    Returns:
    --------
    out: str
        LaTeX array

    See Also
    --------
    array_to_latex

    Examples
    ________
    >>> import numpy as np
    >>> import array_to_latex as ar
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> ar.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

    Note that the output is in your clipboard, so you won't see any results.
    See `to_ltx` for further examples
    """

    b = to_ltx(a, frmt = frmt, arraytype = arraytype, nargout = 1)
    try:
        import clipboard
        clipboard.copy(b)
    except ImportError:
        print('\nPackage ''clipboard'' is not installed')
        print('pip install clipboard\nor install via other means to use this function')

    return

def to_ltx(a, frmt='{:1.2f}', arraytype='bmatrix', nargout = 0):
    """
    Returns a LaTeX array given a numpy array

    Parameters
    ----------
    a         : array
    frmt      : python 3 formatter, optional
                https://mkaz.tech/python-string-format.html
    arraytype : latex array type- `bmatrix` default, optional

    Returns:
    --------
    out: str
        LaTeX array

    See Also
    --------
    to_clp

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as ar
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> ar.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')
    \\begin{array}
      1.23 &  23.46\\\\
    456.23 &   8.24\\\\
    \\end{array}
    >>> ar.to_ltx(A, frmt = '{:6.2e}', arraytype = 'array')
    \\begin{array}
    1.23e+00 & 2.35e+01\\\\
    4.56e+02 & 8.24e+00\\\\
    \\end{array}
    >>> ar.to_ltx(A, frmt = '{:.3g}', arraytype = 'array')
    \\begin{array}
    1.23 & 23.5\\\\
    456 & 8.24\\\\
    \\end{array}
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    a = r'\begin{' + arraytype + '}\n'
    for l in lines:
        for i, num in enumerate(l.split()):
            if i is 0:
                a = a + frmt.format(float(num))
            else:
                a = a + ' ' + '& ' + frmt.format(float(num))
        a = a + r'\\' + '\n'
    a = a + r'\end{' + arraytype + '}'
    if nargout == 1:
        return a
    else:
        print(a)
        return

if __name__ == "__main__":
    import doctest
    import array_to_latex as ar

    doctest.testmod(optionflags=doctest.ELLIPSIS)
    """ What this does.
    python (name of this file)  -v
    will test all of the examples in the help.

    Leaving off -v will run the tests without any output. Success will return nothing.

    See the doctest section of the python manual.
    https://docs.python.org/3.5/library/doctest.html
    """
