import json

import connexion
import numpy
import six
import operator

from swagger_server.encoder import JSONEncoder
from swagger_server.models.base_model_ import Model
from swagger_server.models.nums import Nums  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server import util

results = {}


def get_results():  # noqa: E501
    """Get previous results

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[Results]
    """
    return list(results.values())


def summ2_nums(body):  # noqa: E501
    """summ 2 numbers

     # noqa: E501

    :param body: 2 numbers to operate with
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Nums.from_dict(connexion.request.get_json())  # noqa: E501
    num1 = body.num1
    num2 = body.num2

    operations = {
        "+": operator.add,
        "*": lambda x, y: x * y,
        "-": operator.sub
    }
    result = operations[body.operation](num1, num2)

    res2 = Results(result, str(num1) + " " + body.operation + " " + str(num2))
    global results
    results.update({str(len(results) + 1): res2})
    return result
