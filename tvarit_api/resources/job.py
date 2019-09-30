from .base import Base


class Job(Base):
    def __init__(self, api):
        super(Job, self).__init__(api)
        self.api = api

    def run_job(self, job):
        endpoint = "/jobs"
        return self.api.POST(endpoint, json=job)

    def rerun_job(self, job_id):
        endpoint = "/{}/rerun".format(job_id)
        return self.api.POST(endpoint)

    def abort_job(self, job_id):
        endpoint = "/{}/abort".format(job_id)
        return self.api.POST(endpoint)

    def job_status(self, job_id):
        endpoint = "/{}/status".format(job_id)
        return self.api.POST(endpoint)

    def job_logs(self, job_id):
        endpoint = "/{}/logs".format(job_id)
        return self.api.POST(endpoint)
