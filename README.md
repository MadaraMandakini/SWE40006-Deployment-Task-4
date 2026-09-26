# SWE40006 Deployment Portfolio Task 4

Docker applications developed for SWE40006 Software Deployment and Evolution. This repository contains the source code and Dockerfiles for the Credit, Distinction and High Distinction levels.

## Repository structure

- `credit/` — Basic Flask web application (Task 4.2)
- `distinction/` — Deployment dashboard with environment configuration and a container health check (Task 4.3)
- `hd/` — Non-web CSV processing application (Task 4.4)

Task 4.1 was verified by pulling and running Docker's official `hello-world` image. Its execution evidence is included in the submission report.

## Task 4.2 — Credit

The Flask application serves a page and a `/health` endpoint on container port 5000.

From the `credit` folder:

```bash
docker build -t deployment-task-4-credit:1.0 .
docker run -d --name task4-credit -p 8080:5000 deployment-task-4-credit:1.0
```

Open `http://localhost:8080/` or `http://localhost:8080/health`.

The image was also published to Docker Hub as `madii1234/deployment-task-4-credit:1.0`, then pulled and run on a separate Amazon EC2 Docker host.

## Task 4.3 — Distinction

The dashboard displays its deployment environment and the current UTC time. The `APP_ENV` environment variable is supplied when starting the container.

From the `distinction` folder:

```bash
docker build -t deployment-task-4-distinction:1.0 .
docker run -d --name task4-distinction-local -p 8081:5000 -e APP_ENV=local deployment-task-4-distinction:1.0
```

Open `http://localhost:8081/` or `http://localhost:8081/health`.

The image was published to Docker Hub as `madii1234/deployment-task-4-distinction:1.0`. On EC2, it was run with `APP_ENV=aws-ec2` and host port 8081. The Dockerfile installs dependencies in a separate layer, uses a non-root user, and defines a health check.

## Task 4.4 — High Distinction

This is a command-line CSV processor, not a web server. It reads `data/sales.csv` through a read-only host mount, calculates the total quantity and value, writes the result to container logs, and exits.

From the `hd` folder:

```bash
docker build -t deployment-task-4-hd:1.0 .
docker run -d --name task4-hd --mount "type=bind,source=$(pwd)/data,target=/data,readonly" deployment-task-4-hd:1.0
docker logs task4-hd
docker ps -a --filter name=task4-hd
```

For the included sample CSV, the expected result is 15 total items and a total value of 37.50. `Exited (0)` indicates successful completion.

## Deployment evidence

The submission report contains the Docker build and run outputs, Docker Hub repository pages, EC2 configuration and container states, public browser verification screenshots, and troubleshooting evidence. The AWS Learner Lab instance may be stopped after verification in accordance with course instructions, so its previously recorded public IP may not remain available.
