import sqlite3
from datetime import datetime

from api import get_agencies, get_title, get_title_json
from const import dbName, yearMin, yearMax
from utils import flatten_json
import json
import os

fullPath = os.path.dirname(os.path.abspath(__file__))
def download_data():
    try:
        # Connect to SQLite database (creates a new file if it doesn't exist)
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()

        # Create Agency table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agency (
                slug TEXT PRIMARY KEY,
                display_name TEXT,
                name TEXT,
                short_name TEXT,
                sortable_name TEXT,
                TITLE INTEGER,
                SUBTITLE TEXT,
                CHAPTER TEXT,
                SUBCHAP TEXT,
                PART TEXT
            )
        ''')

        # Create Analysis table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis (
                slug TEXT,
                year INTEGER,
                word_count INTEGER,
                PRIMARY KEY (slug, year)
            )
        ''')

        # Populate Agency table
        agencies = get_agencies()
        uniqueTitles = []

        if isinstance(agencies, dict):  # Check if it's a dictionary
            for agencyO in agencies['agencies']:
                agency = flatten_json(agencyO)
                # collect unique list of titles along the way
                title = agency.get('title',None)
                if title is not None and title not in uniqueTitles:
                    uniqueTitles.append(title)
                insertString = "INSERT or IGNORE INTO agency (slug, display_name, name, short_name, TITLE, SUBTITLE, CHAPTER, SUBCHAP, PART, sortable_name) VALUES (?,?,?,?,?,?,?,?,?,?)"
                cursor.execute(insertString, (agency.get('slug',None),agency.get('display_name',None),agency.get('name',None),agency.get('short_name',None),agency.get('title',None),agency.get('subtitle',None),agency.get('chapter',None),agency.get('subchapter',None),agency.get('part',None),agency.get('sortable_name',None)))
                for year in range(yearMin, yearMax + 1):   
                    insertAnalysisString = "INSERT or IGNORE INTO analysis (slug, year) VALUES (?,?)"
                    cursor.execute(insertAnalysisString, (agency.get('slug',None), year))

        conn.commit()

        # # Create Title table
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS title (
        #         title INTEGER,
        #         date TEXT,
        #         raw TEXT,
        #         PRIMARY KEY (title, date)
        #     )
        # ''')

        # Populate Title table
        # Use cache of files instead - better for storage
        # Make sure missing queries aren't just timing out
        uniqueTitles.sort()
        for year in range(yearMin, yearMax + 1):
            for title in uniqueTitles:
                date = f'{year}-12-31'
                path = fullPath
                filenameXML = f'{path}/cache/{date}_{title}'
                 # Check if file exists in this case instead of calling the API
                if os.path.exists(filenameXML):
                    print(f'{filenameXML} exists - not re-downloading!')
                else:
                    titleResponse = get_title(date, title)
                    if (titleResponse is not None):
                        with open(filenameXML, "w") as file:
                            file.write(titleResponse.decode())
                
                filenameJSON = filenameXML + '.json'
                 # Check if file exists in this case instead of calling the API
                if os.path.exists(filenameJSON):
                    print(f'{filenameJSON} exists - not re-downloading!')
                else:
                    titleResponseJSON = get_title_json(date, title)
                    if (titleResponseJSON is not None):
                        with open(filenameJSON, "w") as file:
                            json.dump(titleResponseJSON, file)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    download_data()