import parser_HH

# full list of variants:
# 'Kafka', 'Airflow', 'Apache Spark', 'Apach Beam', 'MLflow', 'Kuberflow', 'Hadoop', 'DVC', 'Feast'

parser_HH.get_vacancies('Kafka', 'Airflow', 'Apache Spark', save_2_csv=True)
