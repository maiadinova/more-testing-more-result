from kubernetes import client, config

config.load_kube_config()

v1 = client.AppsV1Api()

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-deployment"),
    spec=client.V1DeploymentSpec(
        replicas=2,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-container",
                        image="nginx:latest"
                    )
                ]
            )
        )
    )
)

v1.create_namespaced_deployment(namespace="default", body=deployment)
