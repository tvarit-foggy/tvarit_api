from .base import Base


class Model(Base):
    def __init__(self, api):
        super(Model, self).__init__(api)
        self.api = api
        self.path = '/org/models'

    def create_model(self, name, description=""):
        if not isinstance(name, str) or not name:
            raise ValueError("Model name is required!")
        if not isinstance(description, str):
            raise ValueError("Model description has to be string!")

        response = self.api.POST(self.path, json=dict(
            name=name,
            description=description
        ))
        return response

    def update_model(self, id, name, description="", **kwargs):
        if not isinstance(id, int) or not id:
            raise ValueError("Model id is invalid!")
        if not isinstance(name, str) or not name:
            raise ValueError("Model name is invalid!")
        if not isinstance(description, str):
            raise ValueError("Model description has to be string!")

        response = self.api.PUT(self.path + "/%d" % id, json=dict(
            name=name,
            description=description
        ))
        return response

    def list_models(self, limit=100, page=0):
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("limit is invalid!")
        if not isinstance(page, int) or page < 0:
            raise ValueError("page is invalid!")

        response = self.api.GET(self.path, json=dict(
            limit=limit,
            page=page
        ))
        return response

    def get_model(self, id, depends=False):
        if not isinstance(id, int) or not id:
            raise ValueError("Model id is invalid!")

        response = self.api.GET(self.path + "/%d" % id, json=dict(
            depends=depends
        ))
        return response

    def delete_model(self, id):
        if not isinstance(id, int) or not id:
            raise ValueError("Model id is invalid!")

        response = self.api.DELETE(self.path + "/%d" % id)
        return response
