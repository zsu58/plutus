# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Python output is sent straight to terminal (container logs)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy files into the container
COPY . .

# Install any needed packages specified in requirements.txt
# (Added --no-cache-dir to keep image small)
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "-m", "plutus.main"]