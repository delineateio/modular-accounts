ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# program installs ----------------------------------------------------------------

RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y install apt-transport-https ca-certificates gnupg gcc musl-dev acl
RUN npm install -g @go-task/cli

# pip installs -------------------------------------------------------------------

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
     && rm -rf /tmp/pip-tmp

# gcloud --------------------------------------------------------------------------

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | tee /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-sdk google-cloud-sdk-pubsub-emulator -y

# init ---------------------------------------------------------------------------
RUN echo "export PUBSUB_EMULATOR_HOST=localhost:8085" | tee -a /home/vscode/.bashrc >> /home/vscode/.zshrc
RUN echo "source /home/vscode/.devcontainer.env" | tee -a /home/vscode/.bashrc >> /home/vscode/.zshrc
RUN echo "task init" | tee -a /home/vscode/.bashrc >> /home/vscode/.zshrc
