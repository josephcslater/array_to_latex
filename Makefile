# This Makefile was created by transforming the one for oct2py
# The line #------------------ shows where editing to date has been completed
# for the first attempt.
# Note: This is meant for vibration_toolbox developer use only

.PHONY: all clean test cover release gh-pages docs

# I don't know what the following line means/does
#export TEST_ARGS=--exe -v --with-doctest
export NAME=array_to_latex

export GHP_MSG="Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
export BDR_MSG="Generated binder branch"
export VERSION=`python -c "import $(NAME); print($(NAME).__version__)"`

#all: clean
#	python setup.py install

#----------------------------------------------------

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  clean      to clear build files"
	@echo "  test    		to test all docstring examples"
	@echo "  cover      to test coverage (not working yet)"
	@echo "  release    to edit version, build docs and release"
	@echo "  wheel      build wheel file (for local use)"
	@echo "  wheel-dist build wheel and push to github"
	@echo "  docs       build docs using sphin"
	@echo "  html       alias for docs"
	@echo "  gh-pages   build and release docs"
	@echo "  binder     make binder branch"

clean:
	rm -rf build
	rm -rf dist
	find . -name "*.pyc" -o -name "*.py,cover"| xargs rm -f
#	killall -9 nosetests; true

test:

release: clean
	pip install --user readme_renderer
	#python setup.py check -r -s
	#python setup.py register
	rm -rf dist
	python setup.py bdist_wheel
	# python setup.py sdist
	git tag v$(VERSION)
	git push origin --all
	git push origin --tags
	twine upload dist/*
#	printf '\nUpgrade vibration toolbox with release and sha256 sum:'
#	printf '\nOK, no sha256 sum yet:'
#	shasum -a 256 dist/*.tar.gz

wheel:
	rm -rf dist
	python setup.py bdist_wheel

gh-pages:
	git checkout master
	git pull origin master
	git commit -a -m "Keep examples in sync"; true
	git push origin; true
	make docs
	ghp-import -n -p -m $(GHP_MSG) docs/_build/html

binder:
	git checkout master
	git pull origin master
	git commit -a -m "Keep examples in sync"; true
	git push origin; true
	ghp-import -n -p -b binder -m $(BDR_MSG) docs/tutorial
