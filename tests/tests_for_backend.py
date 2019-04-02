import unittest
import requests
from json import dumps


class TestAuthentication(unittest.TestCase):
    def test_correct_login_and_password(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'Password123'})).json()

        self.assertEqual(answer, {'errors': None,
                                  'user': [
                                      1,
                                      'REnard',
                                      'renard',
                                      1,
                                      answer['user'][-1]
                                  ]
                                  })

    def test_incorrect_login_letter_case(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'renard',
                'password': 'Password123'
            })).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'reNARD',
                'password': 'Password123'
            })).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

    def test_incorrect_login_special_symbols(self):
        answer_only_special_sym = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': '!@#$%^&*()_+-=?.,><][{}\\\'\"`~',
                'password': 'Password123'
            })).json()

        self.assertEqual(answer_only_special_sym, {'errors': 'error',
                                                   'user': None})

        answer_special_sym_normal_sym = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'rewaffs!@#$%^&*()_+-=?.,><][{}\\\'\"`~',
                'password': 'Password123'
            })).json()
        self.assertEqual(answer_special_sym_normal_sym, {'errors': 'error',
                                                         'user': None})

    def test_incorrect_login_ru_language(self):
        answer_only_ru = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'КУтфкв',
                'password': 'Password123'
            })).json()

        self.assertEqual(answer_only_ru, {'errors': 'error',
                                          'user': None})

        answer_ru_en = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'КУтnard',
                'password': 'Password123'
            })).json()

        self.assertEqual(answer_ru_en, {'errors': 'error',
                                        'user': None})

    def test_incorrect_login_wrong(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'pavel',
                'password': 'Password123'})).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

    def test_incorrect_password_letter_case(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'password123'
            })).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'pASSWORD123'})).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

    def test_incorrect_password_special_symbols(self):
        answer_only_special_sym = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': '!@#$%^&*()_+-=?.,><][{}\\\"\''
            })).json()

        self.assertEqual(answer_only_special_sym, {'errors': 'error',
                                                   'user': None})

        answer_special_sym_normal_sym = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'adhfajsfh!@@$@#^%$#&&kljgsk;d$^654376`~'
            })).json()

        self.assertEqual(answer_special_sym_normal_sym, {'errors': 'error',
                                                         'user': None})

    def test_incorrect_password_ru_language(self):
        answer_only_ru = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'Зфыыщцв123'
            })).json()

        self.assertEqual(answer_only_ru, {'errors': 'error',
                                          'user': None})

        answer_ru_en = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'Pasыцщкв123'
            })).json()

        self.assertEqual(answer_ru_en, {'errors': 'error',
                                        'user': None})

    def test_incorrect_password_wrong(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'REnard',
                'password': 'incorrect'
            })).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

    def test_incorrect_login_and_password(self):
        answer = requests.post(
            'http://localhost:8000/Login',
            data=dumps({
                'login': 'renard',
                'password': 'ddjssfajf1'
            })).json()

        self.assertEqual(answer, {'errors': 'error',
                                  'user': None})

    def test_incorrect_data_type(self):
        answer_list = requests.post(
            'http://localhost:8000/Login',
            data=dumps([
                'login', 'renard',
                'password', 'ddjssfajf1'
            ])).json()

        self.assertEqual(answer_list, {
            'errors': 'data is not json or wrong json',
            'user': None
        })

        answer_string = requests.post(
            'http://localhost:8000/Login',
            data=dumps('login''renard''password''ddjssfajf1')).json()

        self.assertEqual(answer_string, {
            'errors': 'data is not json or wrong json',
            'user': None
        })

        answer_int = requests.post(
            'http://localhost:8000/Login',
            data=dumps(1833)).json()

        self.assertEqual(answer_int, {
            'errors': 'data is not json or wrong json',
            'user': None
        })


class TestRegistration(unittest.TestCase):
    def test_correct_login_password(self):
        answer = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test1',
                'password': 'testpassword123тест',
                'user_name': 'Тестовый аккаунт'
            })).json()

        self.assertEqual(answer, 'success')

    def test_incorrect_password_length(self):
        answer_small = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test2',
                'password': '1234',
                'user_name': 'aba'
            })).json()

        self.assertEqual(answer_small, 'Password Error')

        answer_big = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test3',
                'password': 'skjfafhajfkhasfjssfkjueqeurigksugjuiew',
                'user_name': 'aba'
            })).json()

        self.assertEqual(answer_big, 'Password Error')

    def test_incorrect_password_used_characters(self):
        answer_only_letter = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test4',
                'password': 'TestPassword',
                'user_name': 'test'
            })).json()

        self.assertEqual(answer_only_letter, 'Password Error')

        answer_only_int = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test5',
                'password': '124454234',
                'user_name': 'test'
            })).json()

        self.assertEqual(answer_only_int, 'Password Error')

    def test_incorrect_login_existing(self):
        answer = requests.post(
            'http://localhost:8000/Register',
            data=dumps({
                'login': 'test1',
                'password': 'TestPassword1234',
                'user_name': 'test_again'
            })).json()

        self.assertEqual(answer, 'Login Error')

    def test_incorrect_data_type(self):
        answer_list = requests.post(
            'http://localhost:8000/Register',
            data=dumps([
                'login', 'renard',
                'password', 'ddjssfajf1'
            ])).json()

        self.assertEqual(answer_list, 'data is not json or wrong json')

        answer_string = requests.post(
            'http://localhost:8000/Register',
            data=dumps('login''renard''password''ddjssfajf1')).json()

        self.assertEqual(answer_string, 'data is not json or wrong json')

        answer_int = requests.post(
            'http://localhost:8000/Register',
            data=dumps(1833)).json()

        self.assertEqual(answer_int, 'data is not json or wrong json')


class TestAddingProblem(unittest.TestCase):
    pass


class TestSearch(unittest.TestCase):
    def test_normal_search(self):
        answer = requests.post(
            'http://localhost:8000/Find',
            data=dumps({
                'searchValue': 'сгорел коммутатор',
                'idUser': -1,
                'datetime': 500
            })).json()

        self.assertEqual(len(answer['answers']), 5)

    def test_incorrect_data_type(self):
        answer_list = requests.post(
            'http://localhost:8000/Find',
            data=dumps([
                'login', 'renard',
                'password', 'ddjssfajf1'
            ])).json()

        self.assertEqual(answer_list['errors'], 'data is not json or wrong json')

        answer_string = requests.post(
            'http://localhost:8000/Find',
            data=dumps('login''renard''password''ddjssfajf1')).json()

        self.assertEqual(answer_string['errors'], 'data is not json or wrong json')

        answer_int = requests.post(
            'http://localhost:8000/Login',
            data=dumps(1833)).json()

        self.assertEqual(answer_int['errors'], 'data is not json or wrong json')


if __name__ == '__main__':
    unittest.main()
