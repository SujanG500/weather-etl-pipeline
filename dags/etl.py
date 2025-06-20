from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
import pendulum

LATITUDE = 27.7172
LONGITUDE = 85.3240
POSTGRESS_CONN_ID = "postgres-default"
API_CONN_ID = 'open_met_API'

default_args = {
    'owner': 'airflow',
    'start_date': pendulum.now().subtract(days=1),
}

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dags:

    @task()
    def extract_weather_data():
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        endpoint = f'v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'
        response = http_hook.run(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    @task()
    def transfrom_weather_data(weather_data):
        current_weather = weather_data['current_weather']
        return {
            'latitude': LATITUDE,
            'longitude': LONGITUDE,
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }

    @task()
    def load_weather_data(transformed_data):
        pg_hook = PostgresHook(postgres_conn_id=POSTGRESS_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data(
                latitude FLOAT, 
                longitude FLOAT,
                temperature FLOAT,
                windspeed FLOAT,
                winddirection FLOAT,
                weathercode FLOAT
            );
        """)

        cursor.execute("""
            INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            transformed_data['latitude'],
            transformed_data['longitude'],
            transformed_data['temperature'],
            transformed_data['windspeed'],
            transformed_data['winddirection'],
            transformed_data['weathercode'],
        ))

        conn.commit()
        cursor.close()
        conn.close()

    # DAG flow
    weather_data = extract_weather_data()
    transformed_data = transfrom_weather_data(weather_data)
    load_weather_data(transformed_data)
