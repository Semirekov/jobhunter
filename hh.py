from math import ceil

from utils_request import get_json_from_api_request


def read_vacancies_from_hh(language, area=1, date='', page=0, per_page=1):
    base_url = 'https://api.hh.ru/vacancies/'

    params = {
        'area': area,
        'specialization': 1,
        'page': page,
        'per_page': per_page,
        'text': language,
        'search_field': 'name',
        'date_from': date
    }
    
    return get_json_from_api_request(base_url, None, params)


def salary_exist(vacance):
    salary = vacance['salary']
    return salary and salary['currency'] == 'RUR'        


def get_vacance_count(language, area, date=''):
    return read_vacancies_from_hh(language, area, date, 0, 1)['found']     


def get_pages_count(found, respone_limit, per_page):        
    page_count = ceil(found / per_page)        
    page_count_max = ceil(respone_limit / per_page)

    return min(page_count, page_count_max)
       

def get_all_vacancies(language, area, date):
    respone_limit, per_page = 2000, 100    
    vacance_count = get_vacance_count(language, area, date)    
    page_count = get_pages_count(vacance_count, respone_limit, per_page)

    vacancies = []
    for page_index in range(page_count):
        vacancies += read_vacancies_from_hh(language, area, date, page_index, per_page)['items']
    
    return vacancies


def get_salary(vacance):
    return [vacance['salary']['from'], vacance['salary']['to']]


def get_all_salary(language, area, date=''):        
    vaсancies = get_all_vacancies(language, area, date)
    return [get_salary(vacance) for vacance in vaсancies if salary_exist(vacance)]

