from .base import Base


class Machine(Base):
    def __init__(self, api):
        super(Machine, self).__init__(api)
        self.api = api
        self.path = '/org/machines'

    def create_machine(self, name, **kwargs):
        if type(name) != str or not name:
            raise ValueError("Machine name is required!")

        kwargs['name'] = name

        response = self.api.POST(
            self.path,
            json=kwargs
        )
        return response

    def update_machine(self, id, name, **kwargs):
        if type(id) != int or not id:
            raise ValueError("Machine id is invalid!")
        if type(name) != str or not name:
            raise ValueError("Machine name is invalid!")

        kwargs['id'] = id
        kwargs['name'] = name

        response = self.api.PUT(
            self.path + "/%d" % id,
            json=kwargs
        )
        response.raise_for_status()

        return response.json()

    def list_machines(self, limit=100, page=0):
        if type(limit) != int or limit < 0:
            raise ValueError("limit is invalid!")
        if type(page) != int or page < 0:
            raise ValueError("page is invalid!")

        response = self.api.GET(
            self.path,
            params=dict(
                limit=limit,
                page=page
            ))
        response.raise_for_status()

        return response.json()

    def get_machine(self, id, depends=False, get_depends=False, resolve=[]):
        if type(id) != int or not id:
            raise ValueError("Machine id is invalid!")

        response = self.api.GET(
            self.path + "/%d" % id,
            params=dict(
                depends=depends,
                get_depends=get_depends,
                resolve=resolve,
            ))
        response.raise_for_status()

        return response.json()

    def delete_machine(self, id):
        if type(id) != int or not id:
            raise ValueError("Machine id is invalid!")

        response = self.api.DELETE(
            self.path + "/%d" % id)
        response.raise_for_status()

        return response.json()

    def upload_machine_json(self, machines, replace=False, update_if_exists=False):

        response = self.api.POST(
            self.path + "/json",
            params=dict(
                replace=replace,
                update_if_exists=update_if_exists,
            ),
            json=machines
        )
        response.raise_for_status()

        return response.json()
