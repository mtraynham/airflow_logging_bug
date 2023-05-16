start_2_5_3:
	AIRFLOW_VERSION="2.5.3-python3.10" docker stack deploy airflow --compose-file docker-compose.yml
.PHONY: start_2_5_3

start_2_6_0:
	AIRFLOW_VERSION="2.6.0-python3.10" docker stack deploy airflow --compose-file docker-compose.yml
.PHONY: start_2_6_0

stop:
	docker stack rm airflow
.PHONY: stop
