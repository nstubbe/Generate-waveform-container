import os, subprocess
from azure.storage.blob import BlobServiceClient

key = os.environ['AZURE_ACCESS_KEY']
storage_account = os.environ['AZURE_STORAGE_ACCOUNT']
container = os.environ['AZURE_STORAGE_CONTAINER']
file_id = os.environ['FILE_ID']
file_extension = os.environ['FILE_EXT']

connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account};AccountKey={key}"

source_filename = f"{file_id}.{file_extension}"
result_filename = f"{file_id}.json"

try:
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    source_blob_client = blob_service_client.get_blob_client(container=container, blob=source_filename)
    result_blob_client = blob_service_client.get_blob_client(container=container, blob=result_filename)

    # Download file
    download_file_path = os.path.join(source_filename)
    print(f"Downloading blob {source_filename} to {download_file_path}")
    with open(download_file_path, "wb") as download_file:
        download_file.write(source_blob_client.download_blob().readall())

    # Generate waveform
    print(f"Generate waveform for {source_filename}")
    command = f'audiowaveform -i {source_filename} -o {result_filename} -z 256 -b 8'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Upload JSON file
    print("Uploading waveform")
    with open(f"{file_id}.json", "rb") as data:
                result_blob_client.upload_blob(data)
    print("Finished successfully")

except Exception as ex:
    print('Exception:')
    print(ex)