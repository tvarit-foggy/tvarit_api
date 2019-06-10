from .base import Base


class Model(Base):
    def __init__(self, api):
        super(Model, self).__init__(api)
        self.api = api
        self.path = '/org/models'

    def create_model(self, name, description=""):
        if type(name) != str or not name:
            raise ValueError("Model name is required!")
        if type(description) != str:
            raise ValueError("Model description has to be string!")

        response = self.api.POST(self.path, json=dict(
            name=name,
            description=description
        ))
        return response

    def update_model(self, id, name, description="", **kwargs):
        if type(id) != int or not id:
            raise ValueError("Model id is invalid!")
        if type(name) != str or not name:
            raise ValueError("Model name is invalid!")
        if type(description) != str:
            raise ValueError("Model description has to be string!")

        response = self.api.PUT(self.path + "/%d" % id, json=dict(
            name=name,
            description=description
        ))
        return response

    def list_models(self, limit=100, page=0):
        if type(limit) != int or limit < 0:
            raise ValueError("limit is invalid!")
        if type(page) != int or page < 0:
            raise ValueError("page is invalid!")

        response = self.api.GET(self.path, json=dict(
            limit=limit,
            page=page
        ))
        return response

    def get_model(self, id, depends=False):
        if type(id) != int or not id:
            raise ValueError("Model id is invalid!")

        response = self.api.GET(self.path + "/%d" % id, json=dict(
            depends=depends
        ))
        return response

    def delete_model(self, id):
        if type(id) != int or not id:
            raise ValueError("Model id is invalid!")

        response = self.api.DELETE(self.path + "/%d" % id)
        return response
