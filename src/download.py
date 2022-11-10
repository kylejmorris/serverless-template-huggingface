# In this file, we define download_model
# It runs during container build time to get model weights locally

# In this example: A Huggingface BERT model

from transformers import pipeline

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    pipeline('fill-mask', model='bert-base-uncased')

if __name__ == "__main__":
    if os.getenv("HF_AUTH_TOKEN") is None:
        exit(0)
    
    download_model()
