from setuptools import setup, find_packages
import os
import shutil

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='mc-tools',
    version='0.0.1',
    author='Max Lobur',
    author_email='max_lobur@outlook.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=required,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mua=mc_tools.cli:cli',
        ],
    },
)

conf_sample = os.path.join(os.path.dirname(__name__), "mua-config.yml.sample")
shutil.copy(conf_sample, os.path.expanduser("~/"))
