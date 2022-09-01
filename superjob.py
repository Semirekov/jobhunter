from datetime import datetime
import time

from utils_env import get_settins
from utils_request import get_json_from_api_request


def get_unixtime(date_str=''):
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    return time.mktime(date.timetuple())


class VacanceProvider:

    def __init__(self) -> None:
        self._base_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.vacancies_count = 0

    
    def _read_vacancies_from_api(self, langue, town, date=0, page=0, per_page=100):
        params = {
            'town': town,
            'date_published_from': get_unixtime(date),
            'page': page,
            'count': per_page,
            'keyword': langue
        }   
        
        env = get_settins()
        headers = {
            'X-Api-App-Id': env.superjob_token,
            'Authorization': f'Bearer r.000000000000001.{env.superjob_token}'
        }
        return get_json_from_api_request(self._base_url, headers, params)


    def _salary_exist(self, vacance):        
        return vacance['currency'] == 'rub' and (vacance['payment_from'] or vacance['payment_to'])


    def _get_single_salary(self, vacance):
        return [vacance['payment_from'], vacance['payment_to']]


    def get_all_vacancies(self, language, area, date):

        page_index, per_page  = 0, 100        
        raw_vacancies = self._read_vacancies_from_api(language, area, date, page_index, per_page)
        
        self.vacancies_count = raw_vacancies['total']
        vacancies = raw_vacancies['objects']    
        has_more = raw_vacancies['more']

        while has_more:
            raw_vacancies = self._read_vacancies_from_api(language, area, date, page_index, per_page)
            vacancies += raw_vacancies['objects']    
            has_more = raw_vacancies['more']        
    
        return vacancies

    
    def get_all_salary(self, language, area, date):        
        vaсancies = self.get_all_vacancies(language, area, date)
        return [self._get_single_salary(vacance) for vacance in vaсancies if self._salary_exist(vacance)]

