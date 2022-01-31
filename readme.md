# GenerateWaveform container
This container gets an audio file from Azure Blob Storage, generates a waveform in JSON format and uploads that JSON file back to Azure Blob Storage.

## Building the docker image
```
docker build . -t waveform-generator
```
## Running the docker container
```
docker run -e AZURE_ACCESS_KEY='<access_key>' \
    -e AZURE_STORAGE_ACCOUNT='<storage_account_name>' \
    -e AZURE_STORAGE_CONTAINER='<container_name>' \
    -e FILE_ID='<file_id>' \
    -e FILE_EXT='<file_ext>' \
    waveform-generator
```