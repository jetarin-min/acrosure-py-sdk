#!/bin/sh
python3 setup.py sdist bdist_wheel && pip install -e .