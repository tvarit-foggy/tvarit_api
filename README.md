# tvarit_api [![CircleCI](https://img.shields.io/circleci/project/github/tvarit-foggy/tvarit_api.svg?style=flat-square&logo=circleci)](https://circleci.com/gh/tvarit-foggy/workflows/tvarit_api/tree/master) [![GitHub license](https://img.shields.io/github/license/tvarit-foggy/tvarit_api.svg?style=flat-square)](https://github.com/tvarit-foggy/tvarit_api/blob/master/LICENSE)  [![Codecov](https://img.shields.io/codecov/c/gh/tvarit-foggy/tvarit_api.svg?style=flat-square)](https://codecov.io/gh/tvarit-foggy/tvarit_api/)

[![PyPI](https://img.shields.io/pypi/v/tvarit_api.svg?style=flat-square)](https://pypi.org/project/tvarit-api/)

## What is this library for?

Tvarit API library for Python. Support both 2 and 3 Python versions.

## Requirements

You need either 2nd or 3rd version of Python and only the `requests` library installed.

## Quick start

Install the pip package:

```
pip install -U tvarit_api
```

And then connect to your Tvarit API endpoint:

```python
from tvarit_api import Tvarit

tvarit_api = Tvarit(auth='abcde....', host='cloud.tvarit.com')

# Search dashboards based on tag
tvarit_api.search.search_dashboards(tag='applications')

# Find a user by email
user = tvarit_api.users.find_user('test@test.com')

# Add user to team 2
tvarit_api.teams.add_team_member(2, user["id"])

# Create or update a dashboard
tvarit_api.dashboard.update_dashboard(dashboard={'dashboard': {...}, 'folderId': 0, 'overwrite': True})

# Delete a dashboard by UID
tvarit_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')
```

## Status of REST API realization

Work on API implementation still in progress.

| API | Status |
|---|---|
| Admin | + |
| Alerting | - |
| Annotations | - |
| Authentication | +- |
| Dashboard | + |
| Dashboard Versions | - |
| Dashboard Permissions | + |
| Data Source | + |
| Folder | + |
| Folder Permissions | + |
| Folder/Dashboard Search | +- |
| Organisation | + |
| Other | + |
| Preferences | + |
| Snapshot | - |
| Teams | + |
| User | + |

## Issue tracker

Please report any bugs and enhancement ideas using the `tvarit_api` issue tracker:

  https://github.com/tvarit-foggy/tvarit_api/issues

Feel free to also ask questions on the tracker.

## License

`tvarit_api` is licensed under the terms of the MIT License (see the file
[LICENSE](LICENSE)).
