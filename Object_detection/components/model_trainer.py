import os,sys
import yaml
from Object_detection.utils.main_utils import read_yaml_file
from Object_detection.logger import logging
from Object_detection.exception import SignException
from Object_detection.entity.config_entity import ModelTrainerConfig
from Object_detection.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            # Create weights folder and download weights if not already present
            weights_dir = os.path.join(os.getenv("HOME"), "weights")
            os.makedirs(weights_dir, exist_ok=True)
            weight_path = os.path.join(weights_dir, "gelan-c-seg.pt")

            if not os.path.exists(weight_path):
                os.system(f"wget -P {weights_dir} -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c-seg.pt")
            else:
                logging.info("Weights already exist, skipping download.")
            os.system("unzip grocery.zip")
            os.system("rm grocery.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)
            logging.info(f"Model config file: {model_config_file_name}")
            config = read_yaml_file(f"yolov9/models/segment/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov9/models/segment/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            os.system(f"cd yolov9/segment/train.py --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg .models/segment/custom_gelan-c-seg.yaml --weights ./weights/gelan-c-seg.pt --name yolov9_seg_Results --hyp hyp.scratch-high.yaml --no-overlap --workers 8 --cache")
            os.system("cp yolov9/runs/train/yolov9_seg_Results/weights/best.pt yolov9/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov9/runs/train/yolov9_seg_Results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
            os.system("rm -rf yolov9/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov9/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise SignException(e, sys)