from .base import Base


class Handler(Base):
    def __init__(self, api):
        super(Handler, self).__init__(api)
        self.api = api

    def get_handler_by_id(self, handler_id, brief=False, rdepends=False, resolve=None):

        if type(handler_id) == list:
            handler_id = ",".join([str(m) for m in handler_id])

        params = dict(
            brief=brief,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/handlers/{}".format(handler_id)
        return self.api.GET(endpoint, params=params)

    def create_handler(self, handler, update_if_exists=False):

        params = dict(
            update_if_exists=update_if_exists,
        )

        endpoint = "/handlers"
        return self.api.POST(endpoint, json=handler, params=params)

    def update_handler(self, handler_id, handler):

        endpoint = "/handlers/{}".format(handler_id)
        return self.api.PUT(endpoint, json=handler)

    def upload_handler_json(self, handlers, strict=False):

        params = dict(
            strict=strict,
        )

        endpoint = "/handlers/json"
        return self.api.POST(endpoint, json=handlers, params=params)

    def list_handlers(self, detail=False, rdepends=False, resolve=None):

        params = dict(
            detail=detail,
            rdepends=rdepends,
            resolve=resolve or [],
        )

        endpoint = "/handlers"
        return self.api.GET(endpoint, params=params)

    def delete_handler_by_id(self, handler_id):

        if type(handler_id) == list:
            handler_id = ",".join([str(m) for m in handler_id])

        endpoint = "/handlers/{}".format(handler_id)
        return self.api.DELETE(endpoint)
