from flask import render_template, jsonify
from flask_classy import FlaskView
from webargs import fields
from webargs.flaskparser import use_kwargs

from config import config
from services.messente_api import Messente, HlrAPI


class LookupView(FlaskView):
    post_args = {
        'phone_numbers': fields.List(fields.Str()),
    }
    route_base = '/'

    def index(self):
        return render_template('lookup.html')

    @use_kwargs(post_args)
    def post(self, **kwargs):
        phone_numbers = kwargs.get('phone_numbers', None)

        hlr_api = HlrAPI()

        lookup = hlr_api.lookup(phone_numbers)
        response = lookup.get_result()
        return jsonify(self.format_number_lookup_results(response['result']))

    def format_number_lookup_results(self, results):
        return [lookup for lookup in results]
