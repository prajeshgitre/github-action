# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Create the app directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the code
COPY . .

# Set the entrypoint
ENTRYPOINT ["python", "main.py"]
