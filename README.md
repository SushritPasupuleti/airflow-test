# Airflow Test

Trying out Apache Airflow

## Setup

### Init venv

> Use `airflow_env` as the venv name as it has been excluded in `.gitignore`.

```bash
python -m venv airflow_env
```

Activate the venv as per platform.

### Install Airflow

```bash
pip install "apache-airflow[celery]==2.3.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.0/constraints-3.7.txt"
```

### Create Airflow Database

```bash
airflow db init
```

cd into `airflow` directory.

```bash
cd ~/airflow
```

### Create Airflow Users

```bash
airflow users create \
--username admin \
--firstname FIRST_NAME \
--lastname LAST_NAME \
--role Admin \
--email admin@example.org
```

## Running everything

Start webserver

```bash
airflow webserver -D
```

Run Schedules

```bash
airflow scheduler -D
```

## Disable examples

Edit `~/airflow.cfg` and change:

```cfg
load_examples = False
```

```bash
airflow db reset
```

## Setup (Docker)

(Optional) Perform memory check to see if you have enough memory to run the image.

About 8GB will be required

```bash
docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
```

Get `docker-compose.yaml`

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml'
```

It contains the following:

- `airflow-scheduler` - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

- `airflow-webserver` - The webserver is available at <http://localhost:8080>.

- `airflow-worker` - The worker that executes the tasks given by the scheduler.

- `airflow-init` - The initialization service.

- `flower` - The flower app for monitoring the environment. It is available at <http://localhost:5555>.

- `postgres` - The database.

- `redis` - The redis - broker that forwards messages from scheduler to worker.

Mounted directories include:

- `./dags` - you can put your DAG files here.

- `./logs` - contains logs from task execution and scheduler.

- `./plugins` - you can put your custom plugins here.

### Run the image

Init the DB

```bash
docker-compose up airflow-init
```

This creates an admin account with `airflow` as both username and password.

```bash
docker-compose up
```

### Clean Up

```bash
docker-compose down --volumes --rmi all
```