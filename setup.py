from setuptools import setup, find_packages
import os
import shutil

setup(
    name='mc-tools',
    version='0.0.2',
    author='Max Lobur',
    author_email='max_lobur@outlook.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        "pyyaml",
        "futures",
        "click",
        "YaDiskClient",
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mua=mc_tools.cli:cli',
        ],
    },
)

conf_sample = os.path.join(os.path.dirname(__name__), "mua-config.yml.sample")
shutil.copy(conf_sample, os.path.expanduser("~/"))
