from .base import Base


class Model(Base):
    def __init__(self, api):
        super(Model, self).__init__(api)
        self.api = api

    def get_model_by_id(self, model_id, brief=False, depends=False, rdepends=False, get_depends=False, parameters=False, resolve=None):

        if type(model_id) == list:
            model_id = ",".join([str(m) for m in model_id])

        params = dict(
            brief=brief,
            depends=depends,
            rdepends=rdepends,
            get_depends=get_depends,
            parameters=parameters,
            resolve=resolve or [],
        )

        endpoint = "/models/{}".format(model_id)
        return self.api.GET(endpoint, params=params)

    def create_model(self, model, update_if_exists=False):

        params = dict(
            update_if_exists=update_if_exists,
        )

        endpoint = "/models"
        return self.api.POST(endpoint, json=model, params=params)

    def update_model(self, model_id, model):

        endpoint = "/models/{}".format(model_id)
        return self.api.PUT(endpoint, json=model)

    def upload_model_json(self, models, strict=False):

        params = dict(
            strict=strict,
        )

        endpoint = "/models/json"
        return self.api.POST(endpoint, json=models, params=params)

    def list_models(self, detail=False, depends=False, rdepends=False, parameters=None, resolve=None):

        params = dict(
            detail=detail,
            depends=depends,
            rdepends=rdepends,
            parameters=parameters,
            resolve=resolve or [],
        )

        endpoint = "/models"
        return self.api.GET(endpoint, params=params)

    def delete_model_by_id(self, model_id):

        if type(model_id) == list:
            model_id = ",".join([str(m) for m in model_id])

        endpoint = "/models/{}".format(model_id)
        return self.api.DELETE(endpoint)
