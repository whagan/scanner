import os.path
import setuptools
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="statement-scanner",
    version="1.0.0",
    description="Scan statements and extract data",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/whagan/scanner",
    author="Will Hagan",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["whagan=scanner.__main__:main"]},
)