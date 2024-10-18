#!/bin/bash
set -ex
rm -rf bin lib include parts .Python
for python in python3.11 python3.10 python3.9; do
	if which $python; then
		$python -m venv .
		break
	fi
done

./bin/pip install -r requirements.txt

