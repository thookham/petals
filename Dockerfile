# Use PyTorch base image as Petals requires it
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

WORKDIR /app

# Install git and other system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy local code (if any) or prepare for volume mount
COPY . /app

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Install petals if not present (as a fallback/demo)
# RUN pip install petals

# Default command
CMD ["python3"]
