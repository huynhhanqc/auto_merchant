FROM python:3.13.2-bookworm

RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    wget \
    xvfb \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v"]
