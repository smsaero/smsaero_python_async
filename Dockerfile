FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpython3-dev \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install 'aiohttp==3.9.5'
RUN python setup.py develop && pip install -e .[dev]
