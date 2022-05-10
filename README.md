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