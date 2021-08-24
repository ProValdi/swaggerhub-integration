# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestClearController(BaseTestCase):
    """ClearController integration test stubs"""

    def test_delete_results(self):
        """Test case for delete_results

        clear list of requests
        """
        response = self.client.open(
            '/server//clear',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
