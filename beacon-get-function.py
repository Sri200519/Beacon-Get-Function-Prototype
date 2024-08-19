import functions_framework
import requests
from gcloud import storage


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'blob_name' in request_json:
        blob_name = request_json['blob_name']
    elif request_args and 'blob_name' in request_args:
        blob_name = request_args['blob_name']

    bucket_name = "beacon-database"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    content = blob.download_as_string()

    return content