from setuptools import setup, find_packages
from subprocess import check_output


def get_version():
    try:
        tag = check_output(
            ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
        )
        return tag.decode('utf-8').strip("\n")
    except Exception:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )


with open('README.md') as file:
    long_description = file.read()

setup(name='tvarit_api',
      version=get_version(),
      description='Python library for Tvarit API',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/tvarit-foggy/tvarit_api/wiki',
      author='Tvarit GmbH',
      author_email='info@tvarit.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'pyyaml',
      ],
      tests_require=[
          'requests-mock',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False)
