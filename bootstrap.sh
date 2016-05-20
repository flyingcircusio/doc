#!/bin/bash
set -ex
rm -rf bin lib include parts
virtualenv --python=python2 .
bin/pip install zc.buildout==2.5.0
bin/buildout
