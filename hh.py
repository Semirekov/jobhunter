from utils_request import get_json_from_api_request

class VacanceProvider:

    def __init__(self) -> None:
        self.__base_url = 'https://api.hh.ru/vacancies/'
        self.vacancies_count = 0


    def _read_vacancies_from_api(self, key_world, area=1, date='', page=0, per_page=1):
        params = {
            'area': area,
            'specialization': 1,
            'page': page,
            'per_page': per_page,
            'text': key_world,
            'search_field': 'name',
            'date_from': date
        }
    
        return get_json_from_api_request(self.__base_url, None, params)

    
    def _salary_exist(self, vacance):
        salary = vacance['salary']
        return salary and salary['currency'] == 'RUR'  


    def _get_single_salary(self, vacance):
        return [vacance['salary']['from'], vacance['salary']['to']]

    
    def get_all_vacancies(self, language, area, date):
        page_index, per_page  = 0, 100        
        raw_vacancies = self._read_vacancies_from_api(language, area, date, page_index, per_page)
        
        self.vacancies_count  = raw_vacancies['found']
        page_count = raw_vacancies['pages']
        vacancies = raw_vacancies['items']    
    
        for page_index in range(1, page_count):
            vacancies += self._read_vacancies_from_api(language, area, date, page_index, per_page)['items']            
    
        return vacancies


    def get_all_salary(self, language, area, date=''):                
        vaсancies = self.get_all_vacancies(language, area, date)        
        return [self._get_single_salary(vacance) for vacance in vaсancies if self._salary_exist(vacance)]

