import json
from lambda_local.main import call
from lambda_local.context import Context
import lambda_calculator.handler as handler

context = Context(5)


def test_lambda_handler_event_plus(event_plus):
    result = call(handler.lambda_handler, event_plus, context)
    expected_response = ({'statusCode': 200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "4 plus 4 = 8"}'}, None)
    assert result == expected_response


def test_lambda_handler_event_minus(event_minus):
    result = call(handler.lambda_handler, event_minus, context)
    expected_response = ({'statusCode': 200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "10 minus 5 = 5"}'}, None)
    assert result == expected_response


def test_lambda_handler_event_times(event_times):
    result = call(handler.lambda_handler, event_times, context)
    expected_response = ({'statusCode': 200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "10 times 5 = 50"}'}, None)
    assert result == expected_response


def test_lambda_handler_event_divided_by(event_divided_by):
    result = call(handler.lambda_handler, event_divided_by, context)
    expected_response = ({'statusCode': 200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "10 divided-by 5 = 2.0"}'}, None)
    assert result == expected_response
