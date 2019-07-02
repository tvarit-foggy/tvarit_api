from .base import Base


class Annotations(Base):
    def __init__(self, api):
        super(Annotations, self).__init__(api)
        self.api = api

    def list_annotations(self, **kwargs):
        """
        Method to list all annotations
        :return: response
        """
        path = '/annotations'
        params = []
        if kwargs.get('from'):
            params.append('from=%s' % kwargs['from'])

        if kwargs.get('to'):
            params.append('to=%s' % kwargs['to'])

        if kwargs.get('limit'):
            params.append('limit=%s' % kwargs['limit'])

        if kwargs.get('alertId'):
            params.append('alertId=%s' % kwargs['alertId'])

        if kwargs.get('dashboardId'):
            params.append('dashboardId=%s' % kwargs['dashboardId'])

        if kwargs.get('panelId'):
            params.append('panelId=%s' % kwargs['panelId'])

        if kwargs.get('userId'):
            params.append('userId=%s' % kwargs['userId'])

        if kwargs.get('type'):
            params.append('type=%s' % kwargs['type'])

        if kwargs.get('tags'):
            params.extend(['tags=%s' % v for v in kwargs['tags']])

        if params:
            path += '?'
            path += '&'.join(params)

        r = self.api.GET(path)
        return r

    def create_annotation(self, annotation):
        """
        Method to create a new annotation
        :param annotation: annotation json request
        :return: response
        """
        path = '/annotations'
        r = self.api.POST(path, json=annotation)
        return r

    def create_annotation_in_graphite(self, annotation):
        """
        Method to create annotation in graphite format
        :param annotation: annotation json request
        :return: response
        """
        path = '/annotations/graphite'
        r = self.api.POST(path, json=annotation)
        return r

    def update_annotation(self, annotation_id, annotation):
        """
        Method to update annotation
        :param annotation_id: id of annotation
        :param annotation: json body of annotation
        :return: response
        """
        path = '/annotations/%s' % annotation_id
        r = self.api.PUT(path, json=annotation)
        return r

    def delete_annotation(self, annotation_id):
        """
        Method to delete annotation
        :param annotation_id: id of annotation
        :return: response
        """
        path = '/annotations/%s' % annotation_id
        r = self.api.DELETE(path)
        return r

    def delete_region_annotations(self, region_id):
        """
        Method to delete region annotations
        :param region_id: ID of region
        :return: response
        """
        path = '/annotations/region/%s' % region_id
        r = self.api.DELETE(path)
        return r
