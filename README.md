# DevOps CI/CD Automation Project

Автоматизация сборки, тестирования и развертывания контейнеризированного Python-приложения с использованием Docker, GitHub Actions и GitHub Container Registry.

Проект демонстрирует практическое применение инструментов DevOps для организации CI/CD pipeline и автоматического развертывания приложения на удалённом Linux-сервере.

## Архитектура проекта

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions (CI/CD)
    |
    +---- Run Tests
    |
    +---- Build Docker Image
    |
    +---- Push Image to GHCR
    |
    v
GitHub Container Registry
    |
    v
Remote Ubuntu Server
    |
    +---- Docker Compose
    |
    +---- FastAPI Application
    |
    +---- PostgreSQL
    |
    v
Nginx Reverse Proxy
    |
    v
Health Check
```

## Technologies

| Technology | Purpose |
|---|---|
| Linux (Ubuntu, Kali Linux) | Server administration and development |
| Python | Application development |
| FastAPI | Backend framework |
| PostgreSQL | Relational database |
| Docker | Application containerization |
| Docker Compose | Multi-container orchestration |
| Git | Version control |
| GitHub | Source code management |
| GitHub Actions | CI/CD automation |
| GitHub Container Registry (GHCR) | Docker image storage |
| SSH | Secure remote server access |
| Nginx | Reverse proxy |

## Project Structure

```text
d-project/
│
├── app/
│   └── main.py
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## CI/CD Pipeline

The project uses GitHub Actions to automate the application delivery process.

When changes are pushed to the `main` branch, the pipeline automatically performs the following steps:

1. **Testing** — runs automated Python tests.
2. **Docker Build** — builds a Docker image of the application.
3. **Image Publishing** — publishes the Docker image to GitHub Container Registry.
4. **Remote Deployment** — connects to the Ubuntu server via SSH.
5. **Application Update** — pulls the latest Docker image and restarts the application.
6. **Health Check** — checks whether the deployed application is available.

This workflow reduces manual deployment operations and makes application updates more consistent.

## Application Deployment

The application runs on a remote Ubuntu server using Docker and Docker Compose.

Nginx is configured as a reverse proxy and forwards incoming HTTP requests to the FastAPI application.

PostgreSQL is used as the application database.

## Configuration

The deployment requires the following GitHub Actions repository secrets:

| Secret | Description |
|---|---|
| `VPS_HOST` | Server address |
| `VPS_USER` | SSH deployment username |
| `VPS_SSH_KEY` | Private SSH key |

Sensitive configuration values and credentials are stored outside the repository.

**Important:** Never commit private SSH keys, access tokens, passwords or `.env` files to Git.

## Running Locally

Clone the repository:

```bash
git clone https://github.com/cursedocks/d-project.git
cd d-project
```

Configure the environment variables in the `.env` file according to the Docker Compose configuration.

Build and start the application:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

## Key Features

- Containerized Python application.
- PostgreSQL database integration.
- Multi-container orchestration with Docker Compose.
- Automated testing with GitHub Actions.
- Automated Docker image building.
- Image publishing to GHCR.
- SSH-based remote deployment.
- Nginx reverse proxy configuration.
- Automated deployment health checks.

## Project Goals

The main goal of this project is to gain practical experience with DevOps tools and practices:

- Linux server administration.
- Containerization and orchestration.
- CI/CD pipeline development.
- Automated application deployment.
- Remote server management.
- Infrastructure configuration.
- Basic monitoring and application health validation.

## Author

**GitHub:** [@cursedocks](https://github.com/cursedocks)

**Repository:** [d-project](https://github.com/cursedocks/d-project)
