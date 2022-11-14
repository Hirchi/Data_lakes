# Lab1 : Data lakes and data integration

### Create a virtual environment

python -m venv .venv
source .venv/bin/activate

### Install the azure dependencies

pip install -r requirements.text

### Upload our unstructured data files

I used the BlobServiceClient to upload local data in Azure Storage Account blob container

![results.png](Lab1%20Data%20lakes%20and%20data%20integration%20ef66b744cc3e4554a49efec296470129/results.png)

Data is well stored as a data lake inside our blob container.