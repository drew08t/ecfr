# coding: utf-8

"""
    My Project

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.admin_service_api import AdminServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdminServiceApi(unittest.TestCase):
    """AdminServiceApi unit test stubs"""

    def setUp(self):
        self.api = AdminServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_admin_v1_agencies_json_get(self):
        """Test case for api_admin_v1_agencies_json_get

        Agencies  # noqa: E501
        """
        pass

    def test_api_admin_v1_corrections_json_get(self):
        """Test case for api_admin_v1_corrections_json_get

        Corrections route returns all eCFR corrections.  # noqa: E501
        """
        pass

    def test_api_admin_v1_corrections_title_title_json_get(self):
        """Test case for api_admin_v1_corrections_title_title_json_get

        Corrections title route returns all corrections for the supplied title.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
