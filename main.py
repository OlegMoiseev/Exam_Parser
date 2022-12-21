import parser_HH

# full list of variants:
# 'Kafka', 'Airflow', 'Apache Spark', 'Apach Beam', 'MLflow', 'Kuberflow', 'Hadoop', 'DVC', 'Feast'

parser_HH.get_vacancies('Kafka', save_2_csv=True, only_last_day=True)
