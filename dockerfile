# Use a base Python image
FROM python:3.10-slim

# Define the working directory in the container
WORKDIR /app

# Copy the Python script and other necessary files into the container
COPY weather-classification-TP.py /app/
COPY requirements.txt /app/

# Create mount directories for volumes
RUN mkdir -p /app/data /app/output

# Copy the model file into the good repository
COPY ./data/ResNet152V2-Weather-Classification-03.h5 /app/data/ResNet152V2-Weather-Classification-03.h5

# List the files to see if the model exists in the data folder
RUN ls -l /app/data/ResNet152V2-Weather-Classification-03.h5

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Desactivate CUDA if necessary
ENV CUDA_VISIBLE_DEVICES=""

# Default command to run the Python script
CMD ["python", "weather-classification-TP.py"] 
