from .base import Base


class Parameter(Base):
    def __init__(self, api):
        super(Parameter, self).__init__(api)
        self.api = api

    def get_parameter_by_id(self, parameter_id, model_id=0, brief=False, depends=False, rdepends=False, get_depends=False, resolve=None):

        if type(parameter_id) == list:
            parameter_id = ",".join([str(m) for m in parameter_id])

        params = dict(
            brief=brief,
            depends=depends,
            rdepends=rdepends,
            get_depends=get_depends,
            resolve=resolve or [],
        )

        endpoint = "/models/{}/parameters/{}".format(model_id, parameter_id)
        return self.api.GET(endpoint, params=params)

    def create_parameter(self, model_id, parameter, update_if_exists=False):

        params = dict(
            update_if_exists=update_if_exists,
        )

        endpoint = "/models/{}/parameters".format(model_id)
        return self.api.POST(endpoint, json=parameter, params=params)

    def update_parameter(self, parameter_id, parameter, model_id=0):

        endpoint = "/models/{}/parameters/{}".format(model_id, parameter_id)
        return self.api.PUT(endpoint, json=parameter)

    def upload_parameter_json(self, model_id, parameters, strict=False):

        params = dict(
            strict=strict,
        )

        endpoint = "/models/{}/parameters/json".format(model_id)
        return self.api.POST(endpoint, json=parameters, params=params)

    def list_parameters(self, model_id=0, detail=False, depends=False, rdepends=False, resolve=None):

        params = dict(
            detail=detail,
            models=model_id,
            depends=depends,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/parameters"
        return self.api.GET(endpoint, params=params)

    def delete_parameter_by_id(self, parameter_id, model_id=0):

        if type(parameter_id) == list:
            parameter_id = ",".join([str(m) for m in parameter_id])

        endpoint = "/models/{}/parameters/{}".format(model_id, parameter_id)
        return self.api.DELETE(endpoint)
