from __future__ import print_function
import time
import sys
from flask import Flask
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    configuration = swagger_client.Configuration()
    configuration.host = 'https://www.ecfr.gov'
    # create an instance of the API class
    api_instance = swagger_client.AdminServiceApi(swagger_client.ApiClient(configuration))

    try:
        # Agencies
        api_response = api_instance.api_admin_v1_agencies_json_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminServiceApi->api_admin_v1_agencies_json_get: %s\n" % e)
    title = '7' # str | Restricts results to the given title number: Format: '1', '2', '50', etc
    try:
        # Corrections title route returns all corrections for the supplied title.
        api_response = api_instance.api_admin_v1_corrections_title_title_json_get(title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminServiceApi->api_admin_v1_corrections_title_title_json_get: %s\n" % e)
    print('hi')
    return {'time': time.time()}