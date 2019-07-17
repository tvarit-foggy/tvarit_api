workflow "Publish" {
  resolves = ["publish-to-pypi"]
  on = "release"
}

action "publish-to-pypi" {
  uses = "mariamrf/py-package-publish-action@master"
  secrets = ["TWINE_PASSWORD", "TWINE_USERNAME"]
  env = {
    BRANCH = "master"
    PYTHON_VERSION = "3.7.0"
  }
}
