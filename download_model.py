import os
from google.cloud import storage
# code from https://github.com/FelipeAdachi/fake-news-deploy/blob/main/download_model.py modified for our model 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fake-news-detection-342019-e6faaed029ef.json'
client = storage.Client()
bucket = client.get_bucket('fake-news-detection-csce5214')

models_folder = "models"

def download_model_from_gcp(model_name):
    destination_path = model_name
    if not os.path.exists(os.path.join(models_folder,destination_path)):
        os.mkdir(os.path.join(models_folder,destination_path))
    model_path = models_folder + "/" + model_name
    blobs = bucket.list_blobs(prefix=model_path)  # Get list of files
    for blob in blobs:
        if 'joblib' in blob.name or 'pickle' in blob.name:
            filename = blob.name.split("/")[-1]
            blob.download_to_filename(model_path+"/"+filename)
