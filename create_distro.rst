
What I need to do to get this to install properly with pip
https://www.codementor.io/python/tutorial/host-your-python-package-using-github-on-pypi

http://peterdowns.com/posts/first-time-with-pypi.html

To test release
--------------------
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

To release
----------------
python setup.py register -r pypi
python setup.py sdist upload -r pypi
