# утановить bs4
import requests

def get_hhru_data(employer_ids):
    """Получение данных о работодателях и вакансиях с помощью API HH.ru."""

    data = []
    for employer_id in employer_ids:
        response_employer = requests.get('https://api.hh.ru/employers/' + employer_id)
        employer_data = response_employer.json()

        vacancy_data = []
        response_vacancy = requests.get('https://api.hh.ru/vacancies?employer_id=' + employer_id)
        response_text_vac = response_vacancy.json()

        vacancy_data.extend(response_text_vac['items'])

        data.append({
            'employers': employer_data,
            'vacancies': vacancy_data
        })

    return data

def create_database(database_name, params):
    """Создание базы данных"""






def save_data_to_database(data, database_name, params):
    """сохранение данных в бвзе данных"""









employer_ids = ['3127', '3776']    #мегафон мтс


print(get_hhru_data(employer_ids))


# employer_ids = [
#     '1753496',  # ООО Бизапс
#     '1795330',  # Ateuco
#     '2751250',  # AdminDivision
#     '1975782',  # ООО 101
#     '669853',  # BeFresh
#     '2450307',  # ООО АльянсТелекоммуникейшнс
#     '10170495',  # ООО 20 тонн
#     '3446179',  # Gembo
#     '5536919',  # Come&Pass
#     '193400',  # АВТОВАЗ
#     ]
