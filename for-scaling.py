from kubernetes import client, config

config.load_kube_config()

v1 = client.AppsV1Api()

deployment_name = "my-deployment"
namespace = "default"
replica_count = 3

scale = client.V1Scale(
    metadata=client.V1ObjectMeta(name=deployment_name),
    spec=client.V1ScaleSpec(replicas=replica_count)
)

v1.patch_namespaced_deployment_scale(
    name=deployment_name,
    namespace=namespace,
    body=scale
)
