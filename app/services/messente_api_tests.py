import unittest

from .messente_api import Messente, HlrAPI, API


class TestMessenteLibrary(unittest.TestCase):
    def test_modules_init(self):
        messente = Messente(urls="https://test.example.com")
        self.assertIsInstance(messente.hlr, HlrAPI)

        apis = [messente.hlr]
        for item in apis:
            self.assertIsInstance(item, API)


class TestApiLibrary(unittest.TestCase):
    def test_get_api_base_urls_without_custom_url(self):
        api = API('hlr')
        self.assertGreater(len(api.api_urls), 0)

    def test_get_api_base_urls_with_custom_url(self):
        api = API('hlr')
        new_urls = api.get_api_base_urls('https://www.custom_url.com')
        self.assertEqual(len(new_urls), 1)

    def test_get_data_without_password_with_password(self):
        new_dict = API.get_data_without_password({'username': 'foobar', 'password': 'hidden'})
        self.assertEqual(new_dict, {'username': 'foobar'})

    def test_get_data_without_password_without_password(self):
        new_dict = API.get_data_without_password({'username': 'foobar'})
        self.assertEqual(new_dict, {'username': 'foobar'})

    def test_get_data_without_password_empty_dict(self):
        new_dict = API.get_data_without_password({})
        self.assertEqual(new_dict, {})


class TestHlrApi(unittest.TestCase):
    """
    TODO: Skipping this test class to keep the scope of test task smaller. Also it's easier to
    create tests if I'm writing code for pull-request and have access to utils class.
    So I don't have to reinvent the code.
    """
    pass
