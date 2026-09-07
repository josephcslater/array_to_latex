"""Unit tests for array_to_latex, complementing the module's doctests."""

import numpy as np
import pandas as pd
import pytest

import array_to_latex as a2l


class TestNumpyArrays:
    """Tests for numpy array conversion via to_ltx."""

    def test_bmatrix_default(self):
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        out = a2l.to_ltx(A, print_out=False)
        assert out.startswith(r'\begin{bmatrix}')
        assert out.endswith(r'\end{bmatrix}')
        assert '1.00' in out and '4.00' in out

    def test_array_type_column_spec(self):
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        out = a2l.to_ltx(A, arraytype='array', print_out=False)
        assert out.startswith(r'\begin{array}{ c, c}')

    def test_coords(self):
        A = np.array([[1.23456, 23.45678], [456.23, 8.239521]])
        out = a2l.to_ltx(A, frmt='{:1.2f}', arraytype='coords', print_out=False)
        assert out == '{(1.23,23.46),(456.23,8.24)}'

    def test_1d_row_default(self):
        A = np.array([1.0, 2.0, 3.0])
        out = a2l.to_ltx(A, arraytype='array', print_out=False)
        # A single row means only one '\\\\' free block (no row break)
        assert '\\\\' not in out

    def test_1d_column_when_row_false(self):
        A = np.array([1.0, 2.0, 3.0])
        out = a2l.to_ltx(A, arraytype='array', row=False, print_out=False)
        # Three rows means two row breaks ('\\\\')
        assert out.count('\\\\') == 2

    def test_string_array(self):
        A = np.array([['a', 'bb'], ['ccc', 'd']])
        out = a2l.to_ltx(A, print_out=False)
        assert 'a' in out and 'bb' in out and 'ccc' in out

    def test_complex_array(self):
        A = np.array([[1 + 2j, 3 - 4j]])
        out = a2l.to_ltx(A, print_out=False)
        assert 'j' in out
        assert '+' in out

    def test_complex_array_custom_imstring(self):
        A = np.array([[1 + 2j]])
        out = a2l.to_ltx(A, imstring='i', print_out=False)
        assert 'i' in out

    def test_mathform_true_converts_exponent(self):
        A = np.array([[1.23e10]])
        out = a2l.to_ltx(A, frmt='{:1.2e}', mathform=True, print_out=False)
        assert r'\times 10^{' in out

    def test_mathform_false_keeps_e_notation(self):
        A = np.array([[1.23e10]])
        out = a2l.to_ltx(A, frmt='{:1.2e}', mathform=False, print_out=False)
        assert r'\mathrm{e}{' in out

    def test_three_dimensional_raises(self):
        A = np.zeros((2, 2, 2))
        with pytest.raises(ValueError):
            a2l.to_ltx(A, print_out=False)

    def test_invalid_type_raises(self):
        with pytest.raises(TypeError):
            a2l.to_ltx([[1, 2], [3, 4]], print_out=False)

    def test_invalid_arraytype_raises(self):
        A = np.array([[1.0, 2.0]])
        with pytest.raises(ValueError):
            a2l.to_ltx(A, arraytype='bmatrx', print_out=False)

    def test_print_out_returns_none(self, capsys):
        A = np.array([[1.0, 2.0]])
        result = a2l.to_ltx(A)
        captured = capsys.readouterr()
        assert result is None
        assert r'\begin{bmatrix}' in captured.out


class TestDataFrame:
    """Tests for pandas DataFrame conversion via to_ltx."""

    def test_tabular_default(self):
        df = pd.DataFrame({'a': [1.0, 2.0], 'b': [3.0, 4.0]})
        out = a2l.to_ltx(df, print_out=False)
        assert out.startswith(r'\begin{tabular}')
        assert '\\toprule' in out
        assert '\\bottomrule' in out
        assert 'a' in out and 'b' in out

    def test_custom_arraytype(self):
        df = pd.DataFrame({'a': [1.0], 'b': [2.0]})
        out = a2l.to_ltx(df, arraytype='array', print_out=False)
        assert out.startswith(r'\begin{array}')
        assert '\\toprule' not in out

    def test_invalid_arraytype_raises(self):
        df = pd.DataFrame({'a': [1.0], 'b': [2.0]})
        with pytest.raises(ValueError):
            a2l.to_ltx(df, arraytype='not_a_type', print_out=False)


class TestClipboard:
    """Tests for to_clp; clipboard package may be unavailable in CI."""

    def test_to_clp_does_not_raise_without_clipboard(self):
        A = np.array([[1.0, 2.0]])
        # Should not raise even if the optional 'clipboard' package/backend
        # is unavailable in the test environment.
        a2l.to_clp(A)
