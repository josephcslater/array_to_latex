"""
Provides `to_ltx` and `to_clp` which convert numpy arrays to
LaTeX form.
"""

__all__ = ['to_clip', 'to_ltx', '__version__']

__author__ = u'Joseph C. Slater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Joseph C. Slater'

import numpy as _np

def to_clp(a, frmt='{:1.2f}', arraytype='bmatrix'):
    """
    Returns a LaTeX array the the clipboard given a numpy array

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        usually i or j

    Returns
    -------
    out: str
        LaTeX array

    See Also
    --------
    array_to_latex

    Examples
    ________
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

    Note that the output is in your clipboard, so you won't see any results.
    See `to_ltx` for further examples
    """

    b = to_ltx(a, frmt=frmt, arraytype=arraytype, nargout=1)
    try:
        import clipboard as _clipboard
        _clipboard.copy(b)
    except ImportError:
        print('\nPackage ''clipboard'' is not installed')
        print('pip install clipboard\nor install via other ',
              'means to use this function')
    return


def to_ltx(a, frmt='{:1.2f}', arraytype='bmatrix', nargout=0, imstring='j'):
    """
    Returns a LaTeX array given a numpy array

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        usually i or j

    Returns
    -------
    out: str
        LaTeX array

    See Also
    --------
    to_clp

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')
    \\begin{array}
        1.23 &   23.46\\\\
      456.23 &    8.24
    \\end{array}
    >>> a2l.to_ltx(A, frmt = '{:6.2e}', arraytype = 'array')
    \\begin{array}
      1.23e+00 &  2.35e+01\\\\
      4.56e+02 &  8.24e+00
    \\end{array}
    >>> a2l.to_ltx(A, frmt = '{:.3g}', arraytype = 'array')
    \\begin{array}
      1.23 &  23.5\\\\
      456 &  8.24
    \\end{array}
    """

    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')

    out = r'\begin{' + arraytype + '}\n'
    for i in _np.arange(a.shape[0]):
        out = out + ' '
        for j in _np.arange(a.shape[1]):
            if _np.real(a[i, j]) < 0:
                leadstr = ''
            else:
                leadstr = ' '
            if '.' not in frmt.format(a[i, j]):
                dot_space = ' '
            else:
                dot_space = ''
            if _np.iscomplexobj(a[i,j]):
                out = (out + leadstr + frmt.format(a[i, j])[:-1] + imstring
                    + dot_space + ' & ')
            else:
                out = (out + leadstr + frmt.format(a[i, j])[:-1]
                    + dot_space + ' & ')

        out = out[:-3]
        out = out + '\\\\\n'

    out = out[:-3] + '\n' + r'\end{' + arraytype + '}'

    if nargout == 1:
        return out
    else:
        print(out)
        return
