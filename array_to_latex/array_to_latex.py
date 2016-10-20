
def array_to_clipboard(a, frmt='{:1.2f}', arraytype='bmatrix'):
    """
    Returns a LaTeX array the the clipboard given a numpy array

    Parameters
    ----------
    a         : array
    frmt      : python 3 formatter, optional
    arraytype : latex array type- `bmatrix` default, optional

    Returns:
    --------
    out: str
        LaTeX array

    See Also
    --------
    array_to_latex

    See `array_to_latex` for examples 
    """

    b = array_to_latex(a, frmt = frmt, arraytype = arraytype)
    try:
        import clipboard
        clipboard.copy(b)
    except ImportError:
        print('\nPackage ''clipboard'' is not installed')
        print('pip install clipboard\nor install via other means to use this function')

    return

def array_to_latex(a, frmt='{:1.2f}', arraytype='bmatrix'):
    """
    Returns a LaTeX array given a numpy array

    Parameters
    ----------
    a         : array
    frmt      : python 3 formatter, optional
    arraytype : latex array type- `bmatrix` default, optional

    Returns:
    --------
    out: str
        LaTeX array

    See Also
    --------
    array_to_clipboard

    Examples
    --------
    >>> import numpy as np
    >>> from array_to_latex import *
    >>> A = np.array([[1.23456, 23.45678],[456.23, 8.239521]])
    >>> array_to_latex(A, frmt = '{:6.2f}', arraytype = 'array')
    \\begin{array}
      1.23 &  23.46\\\\
    456.23 &   8.24\\\\
    \\end{array}
    >>> array_to_latex(A, frmt = '{:6.2e}', arraytype = 'array')
    \\begin{array}
    1.23e+00 & 2.35e+01\\\\
    4.56e+02 & 8.24e+00\\\\
    \\end{array}
    >>> array_to_latex(A, frmt = '{:.3g}', arraytype = 'array')
    \\begin{array}
    1.23 & 23.5\\\\
    456 & 8.24\\\\
    \\end{array}
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    print(r'\begin{' + arraytype + '}')
    a = r'\begin{' + arraytype + '}\n'
    for l in lines:
        for i, num in enumerate(l.split()):
            if i is 0:
                print(frmt.format(float(num)), end="")
                #print('& ', end="")
                a = a + frmt.format(float(num))
            else:
                print(' ' + '& ' + frmt.format(float(num)), end="")
                a = a + ' ' + '& ' + frmt.format(float(num))
        print(r'\\')
        a = a + r'\\' + '\n'
    print(r'\end{' + arraytype + '}')
    a = a + r'\end{' + arraytype + '}'
    return a
