#!/usr/bin/env bash
set -e
set -x

git diff HEAD --exit-code
git push
git tag v$(python setup.py --version)
git push --tags