from .base import Base


class Handler(Base):
    def __init__(self, api):
        super(Handler, self).__init__(api)
        self.api = api
        self.path = '/org/handlers'

    def create_handler(self, name, handler_type, data, description=""):
        if not isinstance(name, str) or not name:
            raise ValueError("Handler name is required!")
        if not isinstance(description, str):
            raise ValueError("Handler description has to be string!")
        if handler_type not in ("fetch", "batch", "step"):
            raise ValueError(
                "Handler type '%s' is invalid!" %
                str(handler_type))
        if not isinstance(data, str) or not data:
            raise ValueError("Handler data is required!")

        response = self.api.POST(self.path, json=dict(
            name=name,
            description=description,
            type=handler_type,
            data=data,
        ))
        return response

    def update_handler(self, id, name, data, description="", **kwargs):
        if not isinstance(id, int) or not id:
            raise ValueError("Handler id is invalid!")
        if not isinstance(name, str) or not name:
            raise ValueError("Handler name is invalid!")
        if not isinstance(description, str):
            raise ValueError("Handler description has to be string!")
        if not isinstance(data, str) or not data:
            raise ValueError("Handler data is invalid!")

        response = self.api.PUT(self.path + "/%d" % id, json=dict(
            name=name,
            description=description,
            data=data,
        ))
        return response

    def list_handlers(self, handler_type="", limit=100, page=0):
        if handler_type not in ("fetch", "batch", "step", ""):
            raise ValueError(
                "Handler type '%s' is invalid!" %
                str(handler_type))
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("limit is invalid!")
        if not isinstance(page, int) or page < 0:
            raise ValueError("page is invalid!")

        response = self.api.GET(self.path, json=dict(
            type=handler_type,
            limit=limit,
            page=page
        ))
        return response

    def get_handler(self, id, depends=False):
        if not isinstance(id, int) or not id:
            raise ValueError("Handler id is invalid!")

        response = self.api.GET(self.path + "/%d" % id, json=dict(
            depends=depends
        ))
        return response

    def delete_handler(self, id):
        if not isinstance(id, int) or not id:
            raise ValueError("Handler id is invalid!")

        response = self.api.DELETE(self.path + "/%d" % id)
        return response
