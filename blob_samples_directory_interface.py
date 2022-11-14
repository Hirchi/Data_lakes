from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess

import os

connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

container_name = "blob-container-01"



def upload_file(source, dest):

    

    print(f'Uploading {source} to {dest}')

    with open(source, 'rb') as data:

      client.upload_blob(name=dest, data=data)



def upload_dir(source, dest):



    prefix = '' if dest == '' else dest + '/'

    prefix += os.path.basename(source) + '/'

    for root, dirs, files in os.walk(source):

        for name in files:

            dir_part = os.path.relpath(root, source)

            dir_part = '' if dir_part == '.' else dir_part + '/'

            file_path = os.path.join(root, name)

            blob_path = prefix + dir_part + name

            upload_file(file_path, blob_path)

try:

    dest = '' # dest is the target folder name  

    service_client = BlobServiceClient.from_connection_string(connect_str)

    client = service_client.get_container_client(container_name)

    upload_dir("data", dest)

except Exception as ex:

    print('Exception:')