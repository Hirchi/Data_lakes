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

  def download(self, source, dest):
    '''
    Download a file or directory to a path on the local filesystem
    '''
    if not dest:
      raise Exception('A destination must be provided')

    blobs = self.ls_files(source, recursive=True)
    if blobs:
      # if source is a directory, dest must also be a directory
      if not source == '' and not source.endswith('/'):
        source += '/'
      if not dest.endswith('/'):
        dest += '/'
      # append the directory name from source to the destination
      dest += os.path.basename(os.path.normpath(source)) + '/'

      blobs = [source + blob for blob in blobs]
      for blob in blobs:
        blob_dest = dest + os.path.relpath(blob, source)
        self.download_file(blob, blob_dest)
    else:
      self.download_file(source, dest)

  def download_file(self, source, dest):
    '''
    Download a single file to a path on the local filesystem
    '''
    # dest is a directory if ending with '/' or '.', otherwise it's a file
    if dest.endswith('.'):
      dest += '/'
    blob_dest = dest + os.path.basename(source) if dest.endswith('/') else dest

    print(f'Downloading {source} to {blob_dest}')
    os.makedirs(os.path.dirname(blob_dest), exist_ok=True)
    bc = self.client.get_blob_client(blob=source)
    if not dest.endswith('/'):
        with open(blob_dest, 'wb') as file:
          data = bc.download_blob()
          file.write(data.readall())

try:

    dest = '' # dest is the target folder name  

    service_client = BlobServiceClient.from_connection_string(connect_str)

    client = service_client.get_container_client(container_name)

    upload_dir("data", dest)
    client.download('data', 'data')
    print(glob.glob('downloads/**', recursive=True))

except Exception as ex:

    print('Exception:')
