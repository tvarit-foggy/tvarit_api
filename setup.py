from setuptools import setup, find_packages
from tvarit_api.version import get_version

with open("README.md") as file:
    long_description = file.read()

setup(
    name="tvarit_api",
    version=get_version(),
    description="Python library for Tvarit API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tvarit-foggy/tvarit_api",
    author="Tvarit GmbH",
    author_email="info@tvarit.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests", "pyyaml"],
    tests_require=["requests-mock"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)
