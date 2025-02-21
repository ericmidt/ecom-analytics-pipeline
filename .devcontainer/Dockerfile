FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Move uv binaries to a location accessible to vscode
RUN mkdir -p /home/vscode/.local/bin && \
    mv /root/.local/bin/uv /home/vscode/.local/bin/ && \
    mv /root/.local/bin/uvx /home/vscode/.local/bin/ && \
    chown -R vscode:vscode /home/vscode/.local

# Set PATH for the vscode user
ENV PATH="/home/vscode/.local/bin:$PATH"

WORKDIR /workspace

CMD ["tail", "-f", "/dev/null"]
