#!/bin/bash
set -ex
rm -rf bin lib include parts .Python
for python in python3.9 python3.8 python3.7 python3.6; do
	if which $python; then
		$python -m venv .
		break
	fi
done

./bin/pip install --upgrade pip setuptools
bin/pip install zc.buildout
bin/buildout
