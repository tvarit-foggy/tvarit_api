__all__ = [
    "get_version"
]

import os
from subprocess import check_output


def get_version():

    version = None

    if os.path.isfile('PKG-INFO'):
        with open('PKG-INFO') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("Version: "):
                    version = line.strip()[9:]
    else:
        try:
            tag = check_output(
                ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
            )
            return tag.decode("utf-8").strip("\n")
        except Exception:
            pass

    if not version:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )

    return version


if __name__ == "__main__":
    print(get_version())
