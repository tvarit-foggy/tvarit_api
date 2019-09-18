from .base import Base


class Output(Base):
    def __init__(self, api):
        super(Output, self).__init__(api)
        self.api = api

    def get_predictions(self, machine, label, start, end=None):

        params = dict(
            machine=machine,
            label=label,
        )

        params['from'] = start

        if end is not None:
            params['to'] = end

        endpoint = "/predictions"
        return self.api.GET(endpoint, params=params)

    def get_evaluations(self, machine, label, start=None, end=None, execution_id=None):

        params = dict(
            machine=machine,
            label=label,
        )

        if execution_id is not None:
            params['execution_id'] = execution_id

        if start is not None:
            params['from'] = start

        if end is not None:
            params['to'] = end

        endpoint = "/evaluations"
        return self.api.GET(endpoint, params=params)

    def get_scores(self, machine, label, start=None, end=None, execution_id=None):

        params = dict(
            machine=machine,
            label=label,
        )

        if execution_id is not None:
            params['execution_id'] = execution_id

        if start is not None:
            params['from'] = start

        if end is not None:
            params['to'] = end

        endpoint = "/scores"
        return self.api.GET(endpoint, params=params)

    def get_features(self, machine, label, start=None, end=None, execution_id=None):

        params = dict(
            machine=machine,
            label=label,
        )

        if execution_id is not None:
            params['execution_id'] = execution_id

        if start is not None:
            params['from'] = start

        if end is not None:
            params['to'] = end

        endpoint = "/features"
        return self.api.GET(endpoint, params=params)
