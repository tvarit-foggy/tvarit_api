from .base import Base


class Snapshot(Base):
    def __init__(self, api):
        super(Snapshot, self).__init__(api)
        self.api = api

    def create_snapshot(self, snapshot):
        """
        Method to create a new snapshot
        :param snapshot: snapshot json dict
        :return: response
        """
        path = '/snapshots'
        r = self.api.POST(path, json=snapshot)
        return r

    def list_snapshots(self, query=None, limit=None):
        """
        Method to get list of dashboard snapshots
        :param query: query parameter
        :param limit: limit parameter
        :return: response
        """
        path = '/dashboard/snapshots'

        params = []
        if query:
            params.append('query=%s' % query)

        if limit:
            params.append('limit=%s' % limit)

        if params:
            path += '?'
            path += '&'.join(params)

        r = self.api.GET(path)
        return r


    def get_snapshot(self, snapshot_key):
        """
        Method to get snapshot by key
        :param snapshot_key: snapshot key or id
        :return: response
        """
        path = '/snapshots/%s' % snapshot_key
        r = self.api.GET(path)
        return r

    def delete_snapshot(self, snapshot_key):
        """
        Method to delete snapshot by key
        :param snapshot_key: snapshot key or ID
        :return: response
        """
        path = '/snapshots/%s' % snapshot_key
        r = self.api.DELETE(path)
        return r

    def delete_snapshot_by_delete_key(self, snapshot_delete_key):
        """
        Method to delete snapshot by delete key
        :param snapshot_delete_key: snapshot key or ID
        :return: response
        """
        path = '/snapshots-delete/%s' % snapshot_delete_key
        r = self.api.DELETE(path)
        return r
