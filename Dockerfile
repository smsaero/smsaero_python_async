FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpython3-dev \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir 'aiohttp==3.9.5' setuptools wheel pip
RUN python setup.py develop && pip install --no-cache-dir -e .[dev]
