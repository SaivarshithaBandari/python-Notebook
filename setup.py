from setuptools import setup,find_packages

setup(
    name='smartformatter',
    version='0.1',
    packages=find_packages(),
    install_requires=['inflect'],
    author='saivarshitha',
    description='Utility functions for smartformatting of names,phones,numbers.',
)