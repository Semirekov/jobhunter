from datetime import datetime, timedelta
from math import ceil
import time

from utils_env import get_settins
from utils_request import get_json_from_api_request


def get_unixtime(date_str=''):
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    return time.mktime(date.timetuple())


def read_vacancies_from_sj(langue, town, date=0, page=0, per_page=100):
    params = {
        'town': town,
        'date_published_from': get_unixtime(date),
        'page': page,
        'count': per_page,
        'keyword': langue
    }   

    base_url = 'https://api.superjob.ru/2.0/vacancies/'
    env = get_settins()
    headers = {
        'X-Api-App-Id': env.superjob_token,
        'Authorization': f'Bearer r.000000000000001.{env.superjob_token}'
    }
    return get_json_from_api_request(base_url, headers, params)


def get_pages_count(found, respone_limit, per_page):        
    page_count = ceil(found / per_page)        
    page_count_max = ceil(respone_limit / per_page)

    return min(page_count, page_count_max)


def salary_exist(vacance):        
    return vacance['currency'] == 'rub' and (vacance['payment_from'] or vacance['payment_to'])


def get_vacance_count(langue, town, date):
    return read_vacancies_from_sj(langue, town, date)['total']


def get_all_vacancies(language, area, date):
    respone_limit, per_page = 500, 100    
    vacance_count = get_vacance_count(language, area, date)    
    page_count = get_pages_count(vacance_count, respone_limit, per_page)

    vacancies = []
    for page_index in range(page_count):
        vacancies += read_vacancies_from_sj(language, area, date, page_index, per_page)['objects']
    
    return vacancies


def get_salary(vacance):
    return [vacance['payment_from'], vacance['payment_to']]
    

def get_all_salary(language, area, date):        
    vaсancies = get_all_vacancies(language, area, date)
    return [get_salary(vacance) for vacance in vaсancies if salary_exist(vacance)]
    