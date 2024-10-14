## Object Detection End-to-End Pipeline 🚀
# Overview
This project demonstrates a complete end-to-end workflow for an object detection system. It includes building the necessary components from data ingestion, preprocessing, and model training, to deploying the final model as a web application.

## Project Structure 🏗️
The workflow follows a modular structure to maintain clarity and ease of development. The core components of the project are:

Constants - Store all constants and configuration values used across the project.
Entity - Define structured entities used for passing data between components.
Artifact Entity - Responsible for managing the artifact outputs from each component.
Components - Core logic for various stages of the object detection pipeline:
Data Ingestion
Data Preprocessing
Model Training
Model Evaluation
Pipeline - The orchestration of all components in a sequential flow.
Endpoint - A web-based interface to interact with the model using Flask (app.py).
## Setup and Installation ⚙️
To run the project on your local machine, follow the steps below:
1. Create a Virtual Environment
virtualenv object_detection_venv

2. Activate the Environment
# For Windows:
cd object_detection_venv
Scripts\activate

3. Install Required Dependencies
pip install -r requirements.txt

4. Run the Application
python app.py


## Key Features ✨
Modular Design: The project is designed to be highly modular, with each component handling a distinct part of the workflow.
End-to-End Pipeline: From raw data ingestion to serving predictions, every step is automated and reusable.
Extensibility: You can easily extend or modify any part of the pipeline, including swapping out the object detection model.
Web Interface: The project is served through a Flask app, allowing users to interact with the model via an intuitive web interface.
Technology Stack 🛠️
Python: The core language used for all components.
Flask: Used for building the web interface.
YOLOv9: For state-of-the-art object detection and image segmentation.
Virtualenv: To manage project dependencies in an isolated environment.