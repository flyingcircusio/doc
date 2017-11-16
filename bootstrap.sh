#!/bin/bash
set -ex
rm -rf bin lib include parts .Python
python3 -m venv .
./bin/pip install --upgrade pip setuptools
bin/pip install zc.buildout==2.9.5
bin/buildout
