"""
Provides `to_ltx` and `to_clp` which convert numpy arrays to
LaTeX form.
"""

# Note- version must also be set in setup.py
__version__ = 0.50
__all__ = ['to_clp', 'to_ltx', '__version__']

__author__ = u'Joseph C. Slater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Joseph C. Slater'

import numpy as _np
import pandas as _pd


def to_clp(a, frmt='{:1.2f}', arraytype='bmatrix', imstring='j'):
    r"""
    Return a LaTeX array the the clipboard given a numpy array.

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        Character for square root of -1. Usually i or j

    Returns
    -------
    out: str
        LaTeX array

    See Also
    --------
    array_to_latex

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_clp(A, frmt = '{:6.2f}', arraytype = 'array')

    Note that the output is in your clipboard, so you won't see any results.
    See `to_ltx` for further examples.

    """
    b = to_ltx(a, frmt=frmt, arraytype=arraytype, nargout=1, imstring=imstring)
    try:
        import clipboard as _clipboard
        _clipboard.copy(b)
    except ImportError:
        print('\nPackage ''clipboard'' is not installed')
        print('pip install clipboard\nor install via other ',
              'means to use this function')


def _numpyarraytolatex(a, frmt='{:1.2f}', arraytype='bmatrix', nargout=0,
                       imstring='j', row = True):
    r"""
    Print a LaTeX array given a numpy array.

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        Character for square root of -1. Usually i or j
    row      : Boolean
        If the array is 1-D, should the output be a row (True) or column (False)

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

    if len(a.shape) == 1:
        a = _np.array([a])
        if row is False:
            a = a.T

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
            if _np.iscomplexobj(a[i, j]):
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

    print(out)
    return


def _dataframetolatex(df, frmt='{:1.2f}', arraytype='tabular', nargout=0,
                       imstring='j', row = True):
    r"""
    Print a LaTeX array given a Pandas DataFrame array.

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        Character for square root of -1. Usually i or j
    row      : Boolean
        If the array is 1-D, should the output be a row (True) or column (False)

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
    columns = df.columns
    rows = df.transpose().columns
    a = _np.array(df)
    out = r'\begin{' + arraytype + '}'

    if arraytype is 'tabular':
        out += r'{l'
        for column in columns:
            out += 'r'
        out += r'}'

    out += '\n'

    if arraytype is 'tabular':
        out += '\\toprule\n'

        out = out + '     '
        for column in columns:
            out += '& ' + column + ' '
        out += r'\\'

    out +='\n'

    if arraytype is 'tabular':
        out += '\\midrule\n'

    for i in _np.arange(a.shape[0]):
        out = out + ' ' + str(rows[i]) + ' & '
        for j in _np.arange(a.shape[1]):
            if _np.real(a[i, j]) < 0:
                leadstr = ''
            else:
                leadstr = ' '
            if '.' not in frmt.format(a[i, j]):
                dot_space = ' '
            else:
                dot_space = ''
            if _np.iscomplexobj(a[i, j]):
                out = (out + leadstr + frmt.format(a[i, j])[:-1] + imstring
                       + dot_space + ' & ')
            else:
                out = (out + leadstr + frmt.format(a[i, j])[:-1]
                       + dot_space + ' & ')

        out = out[:-3]
        out += '\\\\\n'

    if arraytype == 'tabular':
        out += '\\bottomrule\n'
        out += r'\end{' + arraytype + '}'
    else:
        out = out[:-3] + '\n' + r'\end{' + arraytype + '}'

    return out


def to_ltx(a, frmt='{:1.2f}', arraytype=None, nargout=0,
           imstring='j', row=True):
    r"""
    Print a LaTeX array given a numpy array or Pandas dataframe.

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring : string (optional)
        Character for square root of -1. Usually i or j

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
    if isinstance(a, _np.ndarray):

        if arraytype is None:
            arraytype = 'bmatrix'
        latex = _numpyarraytolatex(a, frmt=frmt, arraytype=arraytype,
                                   nargout=nargout, imstring=imstring,
                                   row=row)
        if nargout == 1:
            return latex
        print(latex)
    if isinstance(a, _pd.core.frame.DataFrame):

        if arraytype is None:
            arraytype = 'tabular'

        latex = _dataframetolatex(a, frmt=frmt, arraytype=arraytype,
                                   nargout=nargout, imstring=imstring)
        if nargout == 1:
            return latex
        print(latex)

    return
