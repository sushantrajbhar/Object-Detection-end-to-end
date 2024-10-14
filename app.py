import sys
import os
import logging
from Object_detection.pipeline.training_pipeline import TrainPipeline
from Object_detection.exception import SignException
from Object_detection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
import shutil

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def trainRoute():
    logger.info("Starting training pipeline...")
    obj = TrainPipeline()
    obj.run_pipeline()
    logger.info("Training successful!")
    return "Training Successful!" 



@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        # Define paths
        input_image_path = "C:/Users/HP/Desktop/Learn Machine Learning/Learn Machine Learning/Projects for Resume/1. Object detection end to end/Object-Detection-end-to-end/data/inputImage.jpg"
        weights_path = "C:/Users/HP/Desktop/Learn Machine Learning/Learn Machine Learning/Projects for Resume/1. Object detection end to end/Object-Detection-end-to-end/yolov9/best.pt"
        output_dir = "yolov9/runs/predict-seg/exp"
        output_image_path = os.path.join(output_dir, "inputImage.jpg")

        # Check if input image exists
        if not os.path.exists(input_image_path):
            print(f"Input image does not exist at path: {input_image_path}")
            return Response("Input image does not exist.")

        # Create the command
        command = f"cd yolov9/segment && python predict.py --weights \"{weights_path}\" --img 640 --conf 0.5 --source \"{input_image_path}\""
        print("Running command:", command)  # Debugging print

        # Run the prediction command
        exit_code = os.system(command)
        print("Command exit code:", exit_code)  # Debugging print

        # Check if the output directory exists after running the command
        if not os.path.exists(output_dir):
            print(f"Output directory does not exist at path: {output_dir}")
            return Response("Output directory was not created.")

        # Check if output image exists
        if not os.path.exists(output_image_path):
            print(f"Output image does not exist at path: {output_image_path}")
            return Response("Output image was not created.")

        # If output image exists, encode it into base64
        opencodedbase64 = encodeImageIntoBase64(output_image_path)
        result = {"image": opencodedbase64.decode('utf-8')}
        
        # Clean up runs directory if necessary
        # os.system("rm -rf yolov9/runs")
        shutil.rmtree("yolov9/runs")


    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error: incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)
@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        weights_path = "C:/Users/HP/Desktop/Learn Machine Learning/Learn Machine Learning/Projects for Resume/1. Object detection end to end/Object-Detection-end-to-end/yolov9/best.pt"
        command = f"cd yolov9/segment && python predict.py --weights \"{weights_path}\" --img 640 --conf 0.5 --source 0"
        os.system(command)
        shutil.rmtree("yolov9/runs")
        return "Camera starting!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)
