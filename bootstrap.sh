#!/bin/bash
set -ex
rm -rf bin lib include parts .Python
python3 -m venv .
./bin/pip install --upgrade pip setuptools
bin/pip install zc.buildout==2.11.0
bin/buildout
