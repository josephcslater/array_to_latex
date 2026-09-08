"""
Return numpy arrays and Pandas dataframes as LaTeX.

Provides `to_ltx` and `to_clp` which convert numpy arrays and Pandas dataframes
arrays to LaTeX form.
"""

from typing import Optional, Union

import numpy as _np
import pandas as _pd

# Note- version must also be set in setup.py
__version__ = '1.0.1'
__all__ = ['to_clp', 'to_ltx', '__version__']

_VALID_ARRAYTYPES = frozenset({
    'bmatrix', 'pmatrix', 'vmatrix', 'Vmatrix', 'Bmatrix', 'matrix',
    'array', 'coords', 'tabular',
})

__author__ = 'Joseph C. Slater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Joseph C. Slater'


def to_clp(
    a: Union[_np.ndarray, _pd.DataFrame],
    frmt: str = '{:1.2f}',
    arraytype: str = 'bmatrix',
    imstring: str = 'j',
) -> None:
    r"""
    Return a LaTeX array to the clipboard given a numpy array.

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
    b = to_ltx(a, frmt=frmt, arraytype=arraytype, imstring=imstring, print_out=False)
    try:
        import clipboard as _clipboard
    except ImportError:
        print("\nPackage 'clipboard' is not installed")
        print('pip install clipboard\nor install via other means to use this function')
        return
    try:
        _clipboard.copy(b)
    except Exception as exc:
        print(f"\nCould not copy to clipboard: {exc}")
        print("Your system may be missing a clipboard backend "
              "(e.g. xclip/xsel on Linux).")


def _format_cell(a, i, j, frmt, imstring, mathform):
    """Format a single array/DataFrame cell (a[i, j]) as a LaTeX-ready string.

    Handles string columns (padded to align on the widest entry in that
    column), real numbers, and complex numbers consistently for both
    `_numpyarraytolatex` and `_dataframetolatex`.
    """
    if isinstance(a[i, j], str):
        leadstr = ' '
        dot_space = (max(len(pet) for pet in a[:, j]) - len(a[i, j])) * ' '
        return leadstr + a[i, j] + dot_space
    leadstr = '' if _np.real(a[i, j]) < 0 else ' '
    dot_space = ' ' if '.' not in frmt.format(a[i, j]) else ''
    if _np.iscomplexobj(a[i, j]):
        real_str = math_form(frmt.format(_np.real(a[i, j])), mathform=mathform)
        imag_str = math_form(frmt.format(_np.imag(a[i, j])), is_imaginary=True,
                             mathform=mathform)
        return leadstr + real_str + ' + ' + imag_str + imstring + dot_space
    return leadstr + math_form(frmt.format(_np.real(a[i, j])), mathform=mathform) + dot_space


def _numpyarraytolatex(a, frmt='{:6.2f}', arraytype='bmatrix',
                       imstring='j', row=True, mathform=True):
    r"""Return a LaTeX array given a numpy array.

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
        If the array is 1-D, should the output be
            a row (True) or column (False)

    Returns
    -------
    out: str
        LaTeX array

    Raises
    ------
    ValueError
        If `a` has more than two dimensions, `a` is empty (unless
        `arraytype` is ``'coords'``), or `arraytype` is not one of the
        supported LaTeX array/matrix environment names.

    See Also
    --------
    to_clp

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')
    \begin{array}{ c, c}
        1.23 &   23.46\\
      456.23 &    8.24
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:6.2e}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23\times 10^{+00} &  2.35\times 10^{+01}\\
      4.56\times 10^{+02} &  8.24\times 10^{+00}
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:.3g}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23 &  23.5\\
      456  &  8.24
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:1.2f}', arraytype = 'coords')
    {(1.23,23.46),(456.23,8.24)}

    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')

    if len(a.shape) == 1:
        a = _np.array([a])
        if row is False:
            a = a.T

    if arraytype == "coords":
        coords = ['(' + ','.join([frmt.format(x) for x in r]) + ')' for r in a]
        return '{' + ','.join(coords) + '}'

    if a.size == 0:
        raise ValueError('Cannot format an empty array as a LaTeX '
                         f"'{arraytype}' environment.")

    arrayformat = ''

    if arraytype == 'array':
        arrayformat = '{ ' + ', '.join(['c'] * a.shape[1]) + '}'

    out = r'\begin{' + arraytype + '}' + arrayformat + '\n'
    for i in range(a.shape[0]):
        out = out + ' '
        for j in range(a.shape[1]):
            out += _format_cell(a, i, j, frmt, imstring, mathform) + ' & '

        out = out[:-3]
        out = out + '\\\\\n'

    out = out[:-3] + '\n' + r'\end{' + arraytype + '}'

    return out


def _dataframetolatex(df,
                      frmt='{:6.2f}',
                      arraytype='tabular',
                      imstring='j',
                      mathform=True):
    r"""
    Return a LaTeX array given a Pandas DataFrame array.

    Parameters
    ----------
    a         : float array
    frmt      : string
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    arraytype : string
        latex array type- `bmatrix` default, optional
    imstring  : string (optional)
        Character for square root of -1. Usually i or j
    mathform  : Boolean (optional: default True)
        Replace #E# with #\times10^{#}


    Returns
    -------
    out: str
        LaTeX array

    Raises
    ------
    ValueError
        If `df` is empty (unless `arraytype` is ``'coords'``), or
        `arraytype` is not one of the supported LaTeX array/table
        environment names.

    See Also
    --------
    to_clp

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')
    \begin{array}{ c, c}
        1.23 &   23.46\\
      456.23 &    8.24
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:6.2e}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23\times 10^{+00} &  2.35\times 10^{+01}\\
      4.56\times 10^{+02} &  8.24\times 10^{+00}
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:.3g}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23 &  23.5\\
      456 &  8.24
    \end{array}

    """
    columns = df.columns
    rows = df.transpose().columns
    a = _np.array(df)

    if arraytype == "coords":
        coords = ['(' + ','.join([frmt.format(x) for x in r]) + ')' for r in a]
        return '{' + ','.join(coords) + '}'

    if a.size == 0:
        raise ValueError('Cannot format an empty DataFrame as a LaTeX '
                         f"'{arraytype}' environment.")

    out = r'\begin{' + arraytype + '}'

    if arraytype == 'tabular':
        out += r'{l'
        for _ in columns:
            out += 'r'
        out += r'}'

    out += '\n'

    if arraytype == 'tabular':
        out += '\\toprule\n'

        out += '     '
        for column in columns:
            out += '& ' + column + ' '
        out += r'\\\n'

        out += '\\midrule\n'

    for i in range(a.shape[0]):
        out = out + ' ' + str(rows[i]) + ' & '
        for j in range(a.shape[1]):
            out += _format_cell(a, i, j, frmt, imstring, mathform) + ' & '

        out = out[:-3]
        out += '\\\\\n'

    if arraytype == 'tabular':
        out += '\\bottomrule\n'
        out += r'\end{' + arraytype + '}'
    else:
        out = out[:-3] + '\n' + r'\end{' + arraytype + '}'

    return out

def to_ltx(
    a: Union[_np.ndarray, _pd.DataFrame],
    frmt: str = '{:1.2f}',
    arraytype: Optional[str] = None,
    imstring: str = 'j',
    row: bool = True,
    mathform: bool = True,
    print_out: bool = True,
) -> Optional[str]:
    r"""
    Print or return a LaTeX array given a numpy array or Pandas dataframe.

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
    row        : Boolean (optional: default True)
        If the array is 1-D, should the output be
            a row (True) or column (False)
    mathform  : Boolean (optional: default True)
        Replace #E# with #\times10^{#}


    Returns
    -------
    out: str
        LaTeX array

    Raises
    ------
    ValueError
        If `a` has more than two dimensions, `a` is empty (unless
        `arraytype` is ``'coords'``), or `arraytype` is not one of the
        supported LaTeX array/table environment names.
    TypeError
        If `a` is neither a numpy array nor a Pandas DataFrame.

    See Also
    --------
    to_clp

    Examples
    --------
    >>> import numpy as np
    >>> import array_to_latex as a2l
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> a2l.to_ltx(A, frmt = '{:6.2f}', arraytype = 'array')
    \begin{array}{ c, c}
        1.23 &   23.46\\
      456.23 &    8.24
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:6.2e}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23\times 10^{+00} &  2.35\times 10^{+01}\\
      4.56\times 10^{+02} &  8.24\times 10^{+00}
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:.3g}', arraytype = 'array')
    \begin{array}{ c, c}
      1.23 &  23.5\\
      456  &  8.24
    \end{array}
    >>> a2l.to_ltx(A, frmt = '{:1.2f}', arraytype = 'coords')
    {(1.23,23.46),(456.23,8.24)}

    """
    if isinstance(a, _np.ndarray):

        if arraytype is None:
            arraytype = 'bmatrix'
        if arraytype not in _VALID_ARRAYTYPES:
            raise ValueError(
                "Invalid arraytype {!r}. Must be one of: {}".format(
                    arraytype, ', '.join(sorted(_VALID_ARRAYTYPES))))
        latex = _numpyarraytolatex(a, frmt=frmt, arraytype=arraytype,
                                   imstring=imstring,
                                   row=row, mathform=mathform)

    elif isinstance(a, _pd.core.frame.DataFrame):

        if arraytype is None:
            arraytype = 'tabular'
        if arraytype not in _VALID_ARRAYTYPES:
            raise ValueError(
                "Invalid arraytype {!r}. Must be one of: {}".format(
                    arraytype, ', '.join(sorted(_VALID_ARRAYTYPES))))
        latex = _dataframetolatex(a, frmt=frmt, arraytype=arraytype,
                                  imstring=imstring)
    else:
        raise TypeError("Argument should be a "
                        "numpy array or a pandas DataFrame.")
    if print_out is True:
        print(latex)
        return

    return latex


def math_form(number, is_imaginary=False, mathform=True):
    if 'e' in number:
        if mathform:
            number = number.replace('e', '\\times 10^{') + '}'
        else:
            number = number.replace('e', '\\mathrm{e}{') + '}'
    return number
