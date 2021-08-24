# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.nums import Nums  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSummController(BaseTestCase):
    """SummController integration test stubs"""

    def test_get_results(self):
        """Test case for get_results

        Get previous results
        """
        response = self.client.open(
            '/v2/summ',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_summ2_nums(self):
        """Test case for summ2_nums

        summ 2 numbers
        """
        body = Nums()
        response = self.client.open(
            '/v2/summ',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
