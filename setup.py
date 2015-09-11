from setuptools import setup, find_packages

setup(
    name="staccato",
    version="0.0.3",
    packages=find_packages(),
    install_requires = ['requests_oauthlib'],
    author = "minamorl",
    description = "Twitter API wrapper for python 3",
)
