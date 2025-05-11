# Telegram Bot

A Telegram bot for facilitating meaningful conversations between people.

## Setup

### Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Telegram Bot token:
   ```bash
   cp env.example .env
   # Edit .env and add your actual token
   ```

5. Run the bot:
   ```bash
   python main.py
   ```

### Using Docker

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a `.env` file with your Telegram Bot token:
   ```bash
   cp env.example .env
   # Edit .env and add your actual token
   ```

3. Build and run using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Deployment

### Manual Deployment

1. Build the Docker image:
   ```bash
   docker build -t telegram-bot:latest .
   ```

2. Run the container:
   ```bash
   docker run -d --name telegram-bot --env-file .env telegram-bot:latest
   ```

### GitHub Container Registry

The bot is automatically built and pushed to GitHub Container Registry when changes are pushed to the main branch.

To pull and run the latest image:

```bash
docker pull ghcr.io/<username>/<repository>:latest
docker run -d --name telegram-bot --env-file .env ghcr.io/<username>/<repository>:latest
```

## CI/CD

GitHub Actions is used for CI/CD:
- Automatically builds and pushes a new Docker image when code is pushed to the main branch
- The workflow is defined in `.github/workflows/docker-build.yml`