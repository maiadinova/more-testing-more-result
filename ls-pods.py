from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
namespace = "default"

print("Listing pods in namespace:", namespace)
pods = v1.list_namespaced_pod(namespace)
for pod in pods.items:
    print(pod.metadata.name)
