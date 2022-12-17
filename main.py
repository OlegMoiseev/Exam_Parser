import parser

# full list of variants:
# 'Kafka', 'Airflow', 'Apache Spark', 'Apach Beam', 'MLflow', 'Kuberflow', 'Hadoop', 'DVC', 'Feast'

parser.get_vacancies('Kafka', 'Airflow', 'Apache Spark', save_2_csv=True)
