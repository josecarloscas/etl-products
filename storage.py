from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=;AccountKey=;EndpointSuffix=core.windows.net"
container_name = ""

blob_service = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service.get_container_client(container_name)

def upload_to_azure(local_file, blob_name):
    with open(local_file, "rb") as data:
        container_client.upload_blob(
            name=blob_name,
            data=data,
            overwrite=True
        )