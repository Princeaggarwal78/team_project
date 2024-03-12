from setuptools import setup,find_packages
from typing import List

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "try" 
PKG_NAME = "first"
AUTHOR_USER_NAME = "Princeaggarwal78"   
AUTHOR_EMAIL="prince991151@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for database",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)