def array_to_latex(a, frmt='{:1.2f}', arraytype='bmatrix'):
    """Returns a LaTeX array
    :a: numpy array
    :frmt: python 3 formatter
    :arraytype: latex array type- `bmatrix` default
    :returns: 
    :prints: LaTeX array

    Example:
    array_to_latex(Krm, frmt = '{:6.2f}', arraytype = 'array')
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    print(r'\begin{' + arraytype + '}')
    for l in lines:
        for num in l.split():
            print(frmt.format(float(num)) + ' ', end="")
            print('& ', end="")
        print(r'\\')
    print(r'\end{' + arraytype + '}')
    return
