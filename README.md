
Simplifying ML Model Deployment and Tracking with Docker and MLflow


Introduction
This project aims to simplify the deployment, tracking, and management of machine learning models using Flask, Docker, and MLflow. It provides an easy-to-use Flask API for model serving and utilizes MLflow for model tracking and performance metrics.

Table of Contents
- Introduction
- Features
- Prerequisites
- Installation
- Usage
- Contributing
- Features
- Flask API for model serving
- MLflow for model tracking and performance metrics
- Dockerized setup for hassle-free deployment

Prerequisites
- Python 3.10
- Docker
- Docker Compose

Installation
- Clone the repository:

    git clone https://github.com/yourusername/your-repo-name.git

- Navigate to the project directory:

    cd your-repo-name

- Build the Docker images:

    docker-compose build

- Usage
    
    Start the containers:

        docker-compose up
    
    Access the Flask API at http://localhost:3000 and the MLflow UI at http://localhost:5000.

    To make predictions, send a POST request to http://localhost:3000/predict.

    To track models, navigate to the MLflow UI and check the metrics and parameters.