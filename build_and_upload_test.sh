#!/bin/bash

# See also: https://packaging.python.org/en/latest/tutorials/packaging-projects/
if [ ! -f ~/.pypirc ] ; them
   echo Please create a ~/.pypirc file first, see:
   echo https://packaging.python.org/en/latest/specifications/pypirc/
   exit 1
fi
rm -rf dist
python3 -m build
python3 -m twine upload --repository testpypi dist/*

# FIXME Add gitlab tagging
echo Install:
echo python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps idoit_scaleup
