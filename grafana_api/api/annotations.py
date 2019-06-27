from .base import Base


class Annotations(Base):

    def __init__(self, api):
        super(Annotations, self).__init__(api)
        self.api = api

    def list_annotations(self):
        """
        Method to list all annotations
        :return: response
        """
        path = '/annotations'
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
        path = 'annotations/graphite'
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
        path = 'annotations/region/%s' % region_id
        r = self.api.DELETE(path)
        return r
