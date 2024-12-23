# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files from the repository to the container
COPY . /app

# Upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN python3 -m pip install --no-cache-dir textattack nltk numpy

# Download NLTK WordNet data
RUN python3 -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

# Default command to run the script
CMD ["python3", "augmenter_script.py"]
