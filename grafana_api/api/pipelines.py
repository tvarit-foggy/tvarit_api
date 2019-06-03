from .base import Base


class Pipeline(Base):
    def __init__(self, api):
        super(Pipeline, self).__init__(api)
        self.api = api
        self.path = '/org/pipelines'

    def create_pipeline(self, name, pipeline_type, data, description=""):
        if type(name) != str or not name:
            raise ValueError("Pipeline name is required!")
        if type(description) != str:
            raise ValueError("Pipeline description has to be string!")
        if pipeline_type not in ("fetch", "analyse", "tune", "fit", "predict"):
            raise ValueError("Pipeline type '%s' is invalid!" % str(pipeline_type))
        if type(data) != str or not data:
            raise ValueError("Pipeline data is required!")

        response = self.api.POST(self.path, json=dict(
            name=name,
            description=description,
            type=pipeline_type,
            data=data,
        ))
        return response


    def update_pipeline(self, id, name, data, description="", **kwargs):
        if type(id) != int or not id:
            raise ValueError("Pipeline id is invalid!")
        if type(name) != str or not name:
            raise ValueError("Pipeline name is invalid!")
        if type(description) != str:
            raise ValueError("Pipeline description has to be string!")
        if type(data) != str or not data:
            raise ValueError("Pipeline data is invalid!")

        response = self.api.PUT(self.path + "/%d" % id, json=dict(
            name=name,
            description=description,
            data=data,
        ))
        return response

    def list_pipelines(self, pipeline_type="", limit=100, page=0):
        if pipeline_type not in ("fetch", "analyse", "tune", "fit", "predict", ""):
            raise ValueError("Pipeline type '%s' is invalid!" % str(pipeline_type))
        if type(limit) != int or limit < 0:
            raise ValueError("limit is invalid!")
        if type(page) != int or page < 0:
            raise ValueError("page is invalid!")

        response = self.api.GET(self.path, json=dict(
            type=pipeline_type,
            limit=limit,
            page=page
        ))
        return response


    def get_pipeline(self, id, depends=False):
        if type(id) != int or not id:
            raise ValueError("Pipeline id is invalid!")

        response = self.api.GET(self.path + "/%d" % id, json=dict(
            depends=depends,
        ))
        return response

    def delete_pipeline(self, id):
        if type(id) != int or not id:
            raise ValueError("Pipeline id is invalid!")

        response = self.api.DELETE(self.path + "/%d" % id)
        return response