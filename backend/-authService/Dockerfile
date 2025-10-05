FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -U app && \
    chown -R app:app /app

# Install Python dependencies
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=app:app . .

# Make start script executable
RUN chmod +x start.sh

# Switch to non-root user
USER app

# Set production environment
ENV PYTHONUNBUFFERED=1

# Expose both FastAPI and Socket.IO ports
EXPOSE 8001 8003

# Command to run both servers using start.sh
CMD ["./start.sh"] 