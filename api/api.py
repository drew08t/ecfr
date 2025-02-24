from __future__ import print_function
import time
import sys
from flask import Flask, request
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

from utils import count_words_in_xml

app = Flask(__name__)
configuration = swagger_client.Configuration()
configuration.host = 'https://www.ecfr.gov'

def startup_function():
    print('Initializing...')

@app.before_request
def before_first_request_func():
    startup_function()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/agencies')
def get_agencies():
    
    try:
        admin_instance = swagger_client.AdminServiceApi(swagger_client.ApiClient(configuration))
        api_response = admin_instance.api_admin_v1_agencies_json_get()
        return api_response
    except ApiException as e:
        print("Exception when calling AdminServiceApi->api_admin_v1_agencies_json_get: %s\n" % e)
    
@app.route('/count')
def get_words():
    date = request.args.get('date')
    title = request.args.get('title')
    subtitle = request.args.get('subtitle')
    chapter = request.args.get('chapter')
    subchapter = request.args.get('subchapter')
    part = request.args.get('part')
    subpart = request.args.get('subpart')
    section = request.args.get('section')
    appendix = request.args.get('appendix')

    args = {}
    if date:
        args['_date'] = date
    if title:
        args['title'] = title
    if subtitle:
        args['subtitle'] = subtitle
    if chapter:
        args['chapter'] = chapter
    if subchapter:
        args['subchapter'] = subchapter
    if part:
        args['part'] = part
    if subpart:
        args['subpart'] = subpart
    if section:
        args['section'] = section
    if appendix:
        args['appendix'] = appendix

    print(args)

    try:
        time.sleep(1)
        versioner_instance = swagger_client.VersionerServiceApi(swagger_client.ApiClient(configuration))
        api_response = versioner_instance.api_versioner_v1_full_date_title_title_xml_get(**args)
        result = count_words_in_xml(api_response)
        return({"count": result})
    except ApiException as e:
        if e.status == 429:
            try:
                time.sleep(1)
                api_response = versioner_instance.api_versioner_v1_full_date_title_title_xml_get(**args)
                result = count_words_in_xml(api_response)
                return({"count": result})
            except ApiException as e2:
                print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e2)
        print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e)