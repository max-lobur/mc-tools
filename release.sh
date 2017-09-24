#!/usr/bin/env bash
git push
git tag v$(python setup.py --version)
git push --tags