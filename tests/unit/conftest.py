import json
import pytest


@pytest.fixture(scope="module")
def event_plus():
    with open("./tests/unit/test_events/"
              "test_event_plus.json") as te:
        test_event_plus = json.loads(te.read())
        return test_event_plus


@pytest.fixture(scope="module")
def event_minus():
    with open("./tests/unit/test_events/"
              "test_event_minus.json") as te:
        test_event_minus = json.loads(te.read())
        return test_event_minus


@pytest.fixture(scope="module")
def event_times():
    with open("./tests/unit/test_events/"
              "test_event_times.json") as te:
        test_event_times = json.loads(te.read())
        return test_event_times


@pytest.fixture(scope="module")
def event_divided_by():
    with open("./tests/unit/test_events/"
              "test_event_divided_by.json") as te:
        test_event_divided_by = json.loads(te.read())
        return test_event_divided_by


@pytest.fixture(scope="module")
def event_divided_by_zero():
    with open("./tests/unit/test_events/"
              "test_event_divided_by_zero.json") as te:
        test_event_divided_by_zero = json.loads(te.read())
        return test_event_divided_by_zero


@pytest.fixture(scope="module")
def event_error_invalid_x():
    with open("./tests/unit/test_events/"
              "test_event_error_invalid_x.json") as te:
        test_event_error_invalid_x = json.loads(te.read())
        return test_event_error_invalid_x


@pytest.fixture(scope="module")
def event_error_invalid_action():
    with open("./tests/unit/test_events/"
              "test_event_error_invalid_action.json") as te:
        test_event_error_invalid_action = json.loads(te.read())
        return test_event_error_invalid_action
