import requests
import pandas as pd


def get_vacancies(*titles: str, save_2_csv=True):
    number_of_pages = 100

    # titles = ['Kafka', 'Airflow', 'Apache Spark', 'Apach Beam', 'MLflow', 'Kuberflow', 'Hadoop', 'DVC', 'Feast']
    # titles = ['Kafka', 'Airflow']

    symbol = "' or '"

    job = ["'" + symbol.join(titles) + "'"]
    data = []
    for i in range(number_of_pages):
        url = 'https://api.hh.ru/vacancies'
        par = {'text': job, 'area': '113', 'per_page': '10', 'page': i, 'only_with_salary': 'true'}  # 113 – Russia
        r = requests.get(url, params=par)
        e = r.json()
        data.append(e)

    vacancy_details = data[0]['items'][0].keys()
    df_vacancies = pd.DataFrame(columns=list(vacancy_details))
    ind = 0
    for i in range(len(data)):
        for j in range(len(data[i]['items'])):
            df_vacancies.loc[ind] = data[i]['items'][j]
            ind += 1

    if save_2_csv:
        csv_name = job[0] + ".csv"
        df_vacancies.to_csv(csv_name)

    return df_vacancies