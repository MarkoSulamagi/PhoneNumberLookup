import json

import messente
from messente.api import api, Response, utils
from messente.api.error import ConfigurationError
from messente.constants import VERSION
import requests


class Messente(messente.Messente):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hlr = HlrAPI(**kwargs)


class HlrResponse(Response):

    def __init__(self, *args, **kwargs):
        Response.__init__(self, *args, **kwargs)

    def get_result(self):
        return json.loads(self.get_raw_text()) if self.is_ok() else None


class API(api.API):

    def __init__(self, config_section, **kwargs):
        super().__init__(config_section, **kwargs)

    def get_api_base_urls(self, custom_api_url):
        api_urls = [custom_api_url] if custom_api_url else self.api_urls

        if not api_urls:
            raise ConfigurationError("No urls configured")

        return api_urls

    @staticmethod
    def get_data_without_password(data):
        data_without_password = data.copy()
        data_without_password.pop('password', None)

        return data_without_password

    def request(self, method, url, data, headers, auth):
        method = method.upper()

        if method == "GET":
            return requests.get(
                url,
                params=data,
                headers=headers,
                allow_redirects=True,
                auth=auth
            )
        elif method == "POST":
            return requests.post(
                url,
                json=data,
                params=data,
                headers=headers,
                allow_redirects=True,
                auth=auth
            )

    def call_api(self, endpoint, data=None, **kwargs):
        data = (data or {})
        method = kwargs.pop("method", "GET")
        custom_api_url = kwargs.pop("api_url", None)
        with_http_basic_auth = kwargs.pop('with_http_basic_auth', False)

        api_urls = self.get_api_base_urls(custom_api_url)

        if not with_http_basic_auth:
            data.update(dict(
                username=self.get_option("username"),
                password=self.get_option("password"),
            ))

        headers = {
            "User-Agent": "messente-python/%s" % str(VERSION)
        }

        # first url that yields any response makes the function return
        for url in api_urls:
            url = "{url}/{endpoint}".format(url=url, endpoint=endpoint)

            self.log.info("%s: %s", method, url)
            self.log.debug("%s", HlrAPI.get_data_without_password(data))

            try:
                auth = (self.get_option('username'), self.get_option('password')) if with_http_basic_auth else None
                return self.request(method, url, data, headers, auth)
            except Exception as e:
                self.log.exception(e)
        self.log.error("No more urls to try. Giving up.")
        return None


class HlrAPI(API):

    def __init__(self, **kwargs):
        super().__init__('hlr', **kwargs)

    def lookup(self, phone_numbers):
        """
        String or list of phone numbers with country code

        :param phone_numbers: String|List
        :return: HlrResponse
        """
        phone_numbers = [phone_numbers] if not isinstance(phone_numbers, (list, )) else phone_numbers

        self.validate(phone_numbers)

        api_response = self.call_api('hlr/sync', data={'numbers': phone_numbers}, method='POST',
                                     api_url='https://api.messente.com', with_http_basic_auth=True)
        response = HlrResponse(api_response)
        self.log_response(response)
        return response

    def _validate(self, data, **kwargs):
        errors = {}

        if not data:
            self.set_error_required(errors, 'phone_numbers')

        for number in data:
            if not utils.is_phone_number_valid(number):
                self.set_error(errors, number)

        return not len(errors), errors
