# Use an official Python runtime as a base image
FROM python:3.10.13-bookworm

RUN apt-get update && apt-get install -y supervisor

# Set the working directory in the container
WORKDIR /app

# Set environment variables
# ENV MODEL_NAME=default_model_name
# ENV FLASK_API_PORT=3000
# ENV MLFLOW_PORT=5000

# Copy the current directory contents into the container at /app
COPY . /app

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port available to the world outside this container
EXPOSE 3000 5000


# Run app.py when the container launches
CMD ["/usr/bin/supervisord"]
