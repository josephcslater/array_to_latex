# Changelog

All notable changes to `array_to_latex` are documented here. Format loosely
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 1.0.1

- Fix a bug where empty arrays/DataFrames (e.g. shape `(0, 0)`) produced
  malformed LaTeX (missing closing brace); now raises `ValueError` instead
  (an empty matrix environment is not meaningful), except for `arraytype='coords'`
  where an empty result is valid.
- Add `Raises` docstring sections documenting `ValueError` conditions.
- Migrate packaging from `setup.py`/`setup.cfg` to `pyproject.toml` (PEP 621),
  update classifiers and add `python_requires` for Python 3.9-3.13.
- Add type hints to the public API (`to_ltx`, `to_clp`).
- Add `ruff` linting (CI-enforced) and `pytest-cov` coverage reporting to CI.
- Replace `np.arange(...)` loop-index idiom with plain `range(...)`.
- Extract full version history into `CHANGELOG.md`.
- Remove redundant `requirements.txt` (dependencies now declared in `pyproject.toml`).

## 1.0.0


- Validate `arraytype`, raising `ValueError` for unsupported/misspelled values.
- Fix `'coords'` arraytype for Pandas DataFrames (previously produced invalid LaTeX).
- Fix stale/incorrect doctest docstrings.
- **Breaking:** remove the unused, vestigial `nargout` parameter from
  `to_ltx`, `to_clp`, and `_numpyarraytolatex`.
- Remove the dead `row` parameter from `_dataframetolatex`.
- Broaden `to_clp` exception handling for missing/unavailable clipboard backends.
- Make `clipboard` an optional install extra (`pip install array_to_latex[clipboard]`).
- Add unit tests and migrate CI from Travis to GitHub Actions (Python 3.9-3.13).

## 0.92

- Allow `np.array` consisting of strings to be converted (thanks to Tesla2000).

## 0.91

- Improve the output for scientific `e` notation.

## 0.90

- Add `coords` format for use in plotting within LaTeX using pgfplots.

## 0.83

- Add formatting defaults when using `array` versus `bmatrix`, etc.

## 0.82

- Raise `ImportError` exception when incorrect datatype used.

## 0.81

- Bug fixes in requirements and `to_clp`.

## 0.80

- Return to previous interface while still enabling returned LaTeX string.

## 0.76

- Printing made better, allows outputs, added `print_out` boolean to turn off printing.

## 0.75

- Output improvements (short-lived release).

## 0.74

- Not released.

## 0.73

- pypi won't handle mathjax. No code change.

## 0.71 / 0.72

- Line breaks broke `readme.rst` on pypi. No code change.

## 0.70

- Added `mathform`. When set to `True` (default), returns 10 to superscript form.

## 0.61

- Minor documentation improvements. No code change.

## 0.60

- Now handles strings in Pandas DataFrames. Fixes bug in exponentials and
  handling of exponentials.

## 0.52

- A few documentation typos fixed. No code change.

## 0.51

- Bug fix: remove extra blank lines in DataFrame tabular output.

## 0.50

- Now works with Pandas DataFrames.

## 0.43

- Now handles 1-D arrays. See new option `row`.

## 0.40 / 0.41

- Critical upgrade: 0.37-0.40 formatted incorrectly.

## 0.38

- Aligns columns neatly.

## 0.37

- Now handles complex arrays.
