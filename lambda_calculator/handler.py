import json
import os
import logging
from pydantic import BaseModel, ValidationError
from enum import Enum

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Action(Enum):
    plus = "plus"
    minus = "minus"
    times = "times"
    divided_by = "divided-by"


class HTTPStatus(Enum):
    SUCCESS = 200
    REDIRECT = 302
    BAD_REQUEST = 400
    UN_AUTHORIZED = 401
    NOT_FOUND = 404
    CONFLICT = 409
    ERROR = 500


class InputEvent(BaseModel):
    class Config:
        use_enum_values = True

    action: Action
    x: int
    y: int


ACTIONS = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "times": lambda x, y: x * y,
    "divided-by": lambda x, y: x / y
}


def lambda_handler(event, context):
    """
    Accepts an action and two numbers,
    performs the specified action on the numbers,
    and returns the result.
    :param event: The event dict that
    contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """
    # Set the log level based on a variable
    # configured in the Lambda environment.
    logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
    logger.debug(f"Event: {event}")
    response = None

    try:
        # Validate Input using Pydantic
        input_event = InputEvent(**event)
        action = input_event.action
        func = ACTIONS.get(input_event.action)
        x = input_event.x
        y = input_event.y
        status_code = 200

        # If input is OK, execute logic
        try:
            if func is not None and \
                    x is not None and \
                    y is not None:
                result = func(x, y)
                response = f"{x} {action} {y} = {result}"
                logger.info(response)
                status_code = HTTPStatus.SUCCESS.value
            else:
                logger.error(f"I can't calculate {x} {action} {y}")
        except ZeroDivisionError:
            logger.warning(f"I can't divide {x} by 0!")
            response = f"I can't divide {x} by 0!"

    except ValidationError as e:
        status_code = HTTPStatus.BAD_REQUEST.value
        logger.error(e.errors())
        response = json.loads(e.json())
    except Exception as general_exception:
        status_code = HTTPStatus.ERROR.value
        logger.error(general_exception)
        response = "Internal Server Error Occurred"

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Response ": response
        })
    }
