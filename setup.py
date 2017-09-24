from setuptools import setup, find_packages

setup(
    name='mc-tools',
    version='0.0.5',
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
    data_files=[('$HOME/', ['mua-config.yml.sample'])],
    entry_points={
        'console_scripts': [
            'mua=mc_tools.cli:cli',
        ],
    },
)
