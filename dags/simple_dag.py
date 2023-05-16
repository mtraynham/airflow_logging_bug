import logging

from airflow import DAG
from airflow.operators import python
import pendulum

logger = logging.getLogger(__name__)


with DAG(
    dag_id='simple_dag',
    description='Simple DAG',
    start_date=pendulum.datetime(2023, 5, 15, tz='UTC'),
    is_paused_upon_creation=False
) as dag:
    def task():
        logger.info('foo')


    python.PythonOperator(
        task_id='simple_task',
        python_callable=task
    )
