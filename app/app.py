from flask import Flask, abort, url_for, request, jsonify
from webargs.flaskparser import parser
from flask_cors import CORS

from config import debug

from resources.lookup import LookupView

app = Flask(__name__, template_folder='templates')
CORS(app, supports_credentials=True)

app.jinja_env.globals = {
    'debug': debug(),
    'url_for': url_for
}
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

LookupView.register(app)


@app.before_request
def before_request():
    # Wipe Jinja2 cache for local development with every request.
    if 'localhost' in request.host_url or '0.0.0.0' in request.host_url:
        app.jinja_env.cache = {}


@parser.error_handler
def handle_request_parsing_error(err):
    abort(jsonify(error_code='validation_error', message=err.messages))


if __name__ == '__main__':
    app.run(debug=debug())
