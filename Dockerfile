# Use the official Python image from the Docker Hub
FROM python:3.9-slim

RUN mkdir /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

# Expose the port the app runs on
EXPOSE 5000

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Run the application
CMD ["python", "main.py"]

