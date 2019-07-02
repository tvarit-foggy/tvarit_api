from .base import Base


class DashboardVersion(Base):
    def __init__(self, api):
        super(DashboardVersion, self).__init__(api)
        self.api = api

    def get_dashboard_versions(self, dashboard_id):
        """
        Method to get dashboard version of a dashboard
        :param dashboard_id: Dashboard ID
        :return: response
        """
        path = '/dashboards/id/%s/versions' % dashboard_id
        r = self.api.GET(path)
        return r

    def get_dashboard_version(self, dashboard_id, version_id):
        """
        Method to display version info of the dashboard version
        :param dashboard_id: Dashboard ID
        :param version_id: Version ID
        :return: response
        """
        path = '/dashboards/id/%s/versions/%s' % (dashboard_id, version_id)
        r = self.api.GET(path)
        return r

    def restore_dashboard(self, dashboard_id, json_body):
        """
        Method to restore dashboard
        :param dashboard_id: Dashboard ID
        :return: response
        """
        path = '/dashboards/id/%s/restore' % dashboard_id
        r = self.api.POST(path, json=json_body)
        return r

    def compare_dashboard_versions(self, dashboard_body):
        """
        Method to compare dashboard versions
        :return: response
        """
        path = '/dashboards/calculate-diff'
        r = self.api.POST(path, json=dashboard_body)
        return r
