import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ACTIONS = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "times": lambda x, y: x * y,
    "divided-by": lambda x, y: x / y
}


def lambda_handler(event, context):
    """
    Accepts an action and two numbers, performs the specified action on the numbers,
    and returns the result.
    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """
    # Set the log level based on a variable configured in the Lambda environment.
    logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
    logger.debug(f"Event: {event}")

    action = event.get("action")
    func = ACTIONS.get(action)
    x = event.get("x")
    y = event.get("y")
    result_str = None
    try:
        if func is not None and x is not None and y is not None:
            result = func(x, y)
            result_str = f"{x} {action} {y} = {result}"
            logger.info(result_str)
        else:
            logger.error(f"I can't calculate {x} {action} {y}")
    except ZeroDivisionError:
        logger.warning(f"I can't divide {x} by 0!")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Response ": result_str
        })
    }
