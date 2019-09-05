from .base import Base


class Pipeline(Base):
    def __init__(self, api):
        super(Pipeline, self).__init__(api)
        self.api = api

    def get_pipeline_by_id(self, pipeline_id, brief=False, rdepends=False, resolve=None):

        if type(pipeline_id) == list:
            pipeline_id = ",".join([str(m) for m in pipeline_id])

        params = dict(
            brief=brief,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/pipelines/{}".format(pipeline_id)
        return self.api.GET(endpoint, params=params)

    def create_pipeline(self, pipeline, update_if_exists=False):

        params = dict(
            update_if_exists=update_if_exists,
        )

        endpoint = "/pipelines"
        return self.api.POST(endpoint, json=pipeline, params=params)

    def update_pipeline(self, pipeline_id, pipeline):

        endpoint = "/pipelines/{}".format(pipeline_id)
        return self.api.PUT(endpoint, json=pipeline)

    def upload_pipeline_json(self, pipelines, strict=False):

        params = dict(
            strict=strict,
        )

        endpoint = "/pipelines/json"
        return self.api.POST(endpoint, json=pipelines, params=params)

    def list_pipelines(self, detail=False, rdepends=False, resolve=None):

        params = dict(
            detail=detail,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/pipelines"
        return self.api.GET(endpoint, params=params)

    def delete_pipeline_by_id(self, pipeline_id):

        if type(pipeline_id) == list:
            pipeline_id = ",".join([str(m) for m in pipeline_id])

        endpoint = "/pipelines/{}".format(pipeline_id)
        return self.api.DELETE(endpoint)
