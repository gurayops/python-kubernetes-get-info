import falcon
from kubernetes import client, config

class KubernetesPodInfo:
    def __init__(self):
        config.load_incluster_config()
        self.k8s = client.CoreV1Api()

    def on_get(self, req, resp, namespace):
        pods = self.k8s.list_namespaced_pod(namespace).items

        podStatus = {pod.metadata.name: pod.status.phase for pod in pods}
        resp.media = podStatus


api = falcon.API()
api.add_route('/pods/{namespace}', KubernetesPodInfo())

