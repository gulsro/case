# Case Project
 
## Introduction

This Django project allows you to manage hotel data, including city information and hotel-city relationships. It provides a user-friendly interface to choose a city and view its associated hotels.

## Prerequisites

Docker: https://docs.docker.com/desktop/install/windows-install/
Python 3.10 (included in the Docker image)
Installation

## Clone this Repository:

```bash
git clone https://github.com/gulsro/case.git
```

## Navigate to the Project Directory:

```bash
cd case
```

## Running the Application

Build the Docker Image:

```bash
docker build -t case .
```

Run the Container in Detached Mode (Background):

```bash
docker run -d -p 8000:8000 case
```

This command runs the container in the background (-d) and maps port 8000 on the host machine to port 8000 within the container, allowing you to access the Django application.

## Data import
The SQLite database is automatically initialized when you run the container using the entrypoint script.

Access the Django Application in Your Browser:

Open http://localhost:8000/ in your browser.

