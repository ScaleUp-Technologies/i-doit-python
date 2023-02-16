#!/bin/bash

rm -rf dist
python3 -m build
pip3 install --force idoit_scaleup --no-index --find-links file://$(pwd)/dist/

