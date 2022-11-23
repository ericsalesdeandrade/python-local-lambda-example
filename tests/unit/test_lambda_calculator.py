import json
from lambda_local.main import call
from lambda_local.context import Context
import lambda_calculator.handler as handler

with open("./tests/unit/test_events/test_event_plus.json") as te:
    test_event_plus = json.loads(te.read())

context = Context(5)


def test_lambda_handler():
    result = call(handler.lambda_handler, test_event_plus, context)
    print(result)
