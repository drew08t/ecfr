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
from swagger_client.api.versioner_service_api import VersionerServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVersionerServiceApi(unittest.TestCase):
    """VersionerServiceApi unit test stubs"""

    def setUp(self):
        self.api = VersionerServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_versioner_v1_ancestry_date_title_title_json_get(self):
        """Test case for api_versioner_v1_ancestry_date_title_title_json_get

        Ancestors route returns all ancestors (including self) from a given level through the top title node.  # noqa: E501
        """
        pass

    def test_api_versioner_v1_full_date_title_title_xml_get(self):
        """Test case for api_versioner_v1_full_date_title_title_xml_get

        Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.  # noqa: E501
        """
        pass

    def test_api_versioner_v1_structure_date_title_title_json_get(self):
        """Test case for api_versioner_v1_structure_date_title_title_json_get

        Structure JSON for a title  # noqa: E501
        """
        pass

    def test_api_versioner_v1_titles_json_get(self):
        """Test case for api_versioner_v1_titles_json_get

        Summary information about each title  # noqa: E501
        """
        pass

    def test_api_versioner_v1_versions_title_title_json_get(self):
        """Test case for api_versioner_v1_versions_title_title_json_get

        Returns an array of all sections and appendices inside a title.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
