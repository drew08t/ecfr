from __future__ import print_function
import sqlite3
import time
import sys
from flask import Flask, jsonify, request
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

from utils import count_words_in_xml
from const import dbName, host

app = Flask(__name__)
configuration = swagger_client.Configuration()
configuration.host = host

def startup_function():
    print('Initializing...')

@app.before_request
def before_first_request_func():
    startup_function()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/agencies-unique')
def get_agencies_db():
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM agency where instance = 1")
    
        # Fetch all rows
        rows = cursor.fetchall()
        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]
        # Convert to list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            conn.close()

def get_agencies_db():
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM agency")
    
        # Fetch all rows
        rows = cursor.fetchall()
        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]
        # Convert to list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            conn.close()

@app.route('/analysis')
def get_analysis_db():
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM analysis")
    
        # Fetch all rows
        rows = cursor.fetchall()
        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]
        # Convert to list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        print(results)
        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            conn.close()

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

def get_title(date, title, subtitle=None, chapter=None, subchapter=None, part=None, subpart=None, section=None, appendix=None):
    args = {}
    # override default swagger timeout for larger queries
    args['_request_timeout'] = (30, 120)
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

    # For some reason including a blank subtitle causes the API to not timeout and run much faster, go figure...
    args['subtitle'] = ''

    print(args)

    try:
        versioner_instance = swagger_client.VersionerServiceApi(swagger_client.ApiClient(configuration))
        return versioner_instance.api_versioner_v1_full_date_title_title_xml_get(**args)
    except ApiException as e:
        if e.status == 429:
            try:
                time.sleep(1)
                return versioner_instance.api_versioner_v1_full_date_title_title_xml_get(**args)
            except ApiException as e2:
                print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e2)
        print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e)

def get_title_json(date, title):
    args = {}
    # override default swagger timeout for larger queries
    args['_request_timeout'] = (30, 120)
    if date:
        args['_date'] = date
    if title:
        args['title'] = title

    print(args)

    try:
        versioner_instance = swagger_client.VersionerServiceApi(swagger_client.ApiClient(configuration))
        # return versioner_instance.api_versioner_v1_full_date_title_title_xml_get(**args)
        return versioner_instance.api_versioner_v1_structure_date_title_title_json_get(**args)
    except ApiException as e:
        if e.status == 429:
            try:
                time.sleep(1)
                return versioner_instance.api_versioner_v1_structure_date_title_title_json_get(**args)
            except ApiException as e2:
                print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e2)
        print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e)