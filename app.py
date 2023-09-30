from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Either load a local Kubernetes configuration or in-cluster config
# config.load_kube_config()
config.load_incluster_config()

# Create a Kubernetes API client for Jobs
batch_api = client.BatchV1Api()

# Define the job configuration
def create_job_object(job_name, container_image, command):
    container = client.V1Container(
        name=job_name,
        image=container_image,
        command=command
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": job_name}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]),
    )

    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=client.V1JobSpec(ttl_seconds_after_finished=60, template=template),
    )

    return job


# Create and submit a job
def create_and_submit_job(job_name, container_image, command):
    job = create_job_object(job_name, container_image, command)
    try:
        batch_api.create_namespaced_job(namespace="default", body=job)
        print(f"Job {job_name} created successfully.")
    except ApiException as e:
        print(f"Error creating job {job_name}: {e}")


# Defining job details
job_name = "hello-world"
container_image = "python:alpine"
command = ["python", "-c", "print('Hello, World')"]

# Create and submit the job
create_and_submit_job(job_name, container_image, command)
