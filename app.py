from flask import (
    Flask,
    request,
)

import sentry_sdk

sentry_sdk.init(
    dsn="https://deb7a6a91a904acfb63bc877d67482c0@o388665.ingest.sentry.io/5225844",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)

from api.calculator.calculator import Calculator

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():
    return operation('add', 2)

@app.route('/api/subtract', methods=['POST'])
def subtract():
    return operation('subtract', 2)

@app.route('/api/multiply', methods=['POST'])
def multiply():
    return operation('multiply', 2)

@app.route('/api/divide', methods=['POST'])
def divide():
    return operation('divide', 2)

def operation(method, num_factors):
    factors = []
    if num_factors == 2:
        factors.append(float(request.json.get('x')))
        factors.append(float(request.json.get('y')))

    return str(getattr(Calculator, method)(*factors))

@app.route('/error')
def ohno():
    Calculator.explode(1,0)
    return

app.run(host='0.0.0.0', port=8080)