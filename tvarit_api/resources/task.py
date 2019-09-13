from .base import Base


class Task(Base):
    def __init__(self, api):
        super(Task, self).__init__(api)
        self.api = api

    def get_task_by_id(self, task_id, brief=False, rdepends=False, resolve=None):

        if type(task_id) == list:
            task_id = ",".join([str(m) for m in task_id])

        params = dict(
            brief=brief,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/tasks/{}".format(task_id)
        return self.api.GET(endpoint, params=params)

    def create_task(self, task, update_if_exists=False):

        params = dict(
            update_if_exists=update_if_exists,
        )

        endpoint = "/tasks"
        return self.api.POST(endpoint, json=task, params=params)

    def update_task(self, task_id, task):

        endpoint = "/tasks/{}".format(task_id)
        return self.api.PUT(endpoint, json=task)

    def upload_task_json(self, tasks, strict=False):

        params = dict(
            strict=strict,
        )

        endpoint = "/tasks/json"
        return self.api.POST(endpoint, json=tasks, params=params)

    def list_tasks(self, detail=False, rdepends=False, resolve=None):

        params = dict(
            detail=detail,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/tasks"
        return self.api.GET(endpoint, params=params)

    def delete_task_by_id(self, task_id):

        if type(task_id) == list:
            task_id = ",".join([str(m) for m in task_id])

        endpoint = "/tasks/{}".format(task_id)
        return self.api.DELETE(endpoint)
