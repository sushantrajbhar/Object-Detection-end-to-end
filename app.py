import os
from Object_detection.pipeline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()


# import gdown

# url = 'https://drive.google.com/uc?id=1vma-9hUkc-kh4fYvaZMOeclH9FmJGn-K'
# output = '20150428_collected_images.tgz'
# gdown.download(url, output, quiet=False)