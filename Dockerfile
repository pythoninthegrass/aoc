FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential python3.10 python3.10-distutils python3.10-dev python3.10-venv python3-pip python3-wheel \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
RUN python3.10 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel && pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install --no-install-recommends -y python3.10 python3.10-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home appuser \
    && mkdir -p /home/appuser/app \
    && chown appuser:appuser /home/appuser/app

USER appuser

COPY --from=builder-image --chown=appuser:appuser /opt/venv /opt/venv

# activate virtual environment
# Keeps Python from generating .pyc files in the container
# Turns off buffering for easier container logging
ENV VIRTUAL_ENV="/opt/venv" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy user code into application code
COPY --chown=appuser:appuser solutions /home/appuser/app

WORKDIR /home/appuser/app

# ENV EC2_KEY='not defined' K8S_KEY='not defined'

# Default arguments (originally /bin/bash)
ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT [ "/opt/venv/bin/python", "main.py" ]
