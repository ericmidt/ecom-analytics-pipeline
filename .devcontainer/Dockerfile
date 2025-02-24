FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install UV package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    ca-certificates \
    gnupg

# Remove any old Google Cloud keys
RUN rm -f /usr/share/keyrings/cloud.google.gpg

# Add the new Google Cloud SDK repository key (properly formatted)
RUN curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google-archive-keyring.gpg

# Add the Google Cloud SDK repository and install `google-cloud-cli`
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google-archive-keyring.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list \
    && apt-get update \
    && apt-get install -y google-cloud-cli

# Clean up package lists after installation
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Move UV binaries to a location accessible to vscode
RUN mkdir -p /home/vscode/.local/bin && \
    mv /root/.local/bin/uv /home/vscode/.local/bin/ && \
    mv /root/.local/bin/uvx /home/vscode/.local/bin/ && \
    chown -R vscode:vscode /home/vscode/.local

# Set PATH for the vscode user
ENV PATH="/home/vscode/.local/bin:$PATH"

WORKDIR /workspace

CMD ["tail", "-f", "/dev/null"]
