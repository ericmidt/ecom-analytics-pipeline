# .devcontainer/Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up environment variables if needed (e.g., for Google BigQuery authentication)
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /workspace
