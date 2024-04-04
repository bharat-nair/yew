from setuptools import setup, find_packages

setup(
    name="yew",
    version="0.9.1-dev",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "idna==3.6",
        "requests==2.31.0",
        "urllib3==2.2.1",
    ],
    author="Bharat Nair",
    author_email="bharat@rubberducker.xyz",
    description="An OldSchool RuneScape API wrapper for Python",
    url="https://github.com/bharat-nair/yew",
)
