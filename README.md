# Weather ETL Pipeline with Apache Airflow

## Overview

This project is an Apache Airflow DAG that performs an ETL (Extract, Transform, Load) process to fetch, process, and store weather data for Kathmandu, Nepal using the Open-Meteo API and PostgreSQL.

---

## Features

- **Extract:** Retrieves current weather data for specified latitude and longitude via the Open-Meteo API.
- **Transform:** Processes the JSON response to extract relevant weather attributes such as temperature, wind speed, and direction.
- **Load:** Stores the transformed data into a PostgreSQL table named `weather_data`. The table is created if it does not exist.

---

## Components

- **Airflow DAG:** Defined in `weather_etl_pipeline` with a daily schedule.
- **Tasks:**  
  - `extract_weather_data`: Calls the Open-Meteo API using Airflow's `HttpHook`.  
  - `transfrom_weather_data`: Parses and selects key weather fields.  
  - `load_weather_data`: Inserts data into PostgreSQL using `PostgresHook`.

---

## Prerequisites

- Apache Airflow installed and configured.
- Airflow connections set up:
  - `open_met_API`: HTTP connection for Open-Meteo API (no auth required).
  - `postgres-default`: PostgreSQL connection for the target database.
- Python packages required: `apache-airflow`, `pendulum`, `requests` (via Airflow providers).
- PostgreSQL database accessible with appropriate permissions.

---

## Usage

1. Clone this repository and place the DAG file into your Airflow DAGs folder.
2. Ensure your Airflow connections (`open_met_API` and `postgres-default`) are configured.
3. Start your Airflow scheduler and webserver.
4. The DAG `weather_etl_pipeline` will run automatically every day (or trigger manually).
5. Monitor the DAG progress and logs from the Airflow UI at `http://localhost:8080`.

---

## Database Schema

The DAG creates (if not exists) a table with the following structure:

| Column        | Type    |
| ------------- | ------- |
| latitude      | FLOAT   |
| longitude     | FLOAT   |
| temperature   | FLOAT   |
| windspeed     | FLOAT   |
| winddirection | FLOAT   |
| weathercode   | FLOAT   |

---

## Notes

- The latitude and longitude are hardcoded for Kathmandu, Nepal (27.7172, 85.3240).
- The DAG uses the TaskFlow API style with the `@task` decorator.
- Error handling is included for API request failures.

---

## License

This project is open source and available under the MIT License.
