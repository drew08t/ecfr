import sqlite3

from api import get_agencies, get_title, get_title_json
from const import dbName, yearMin, yearMax, recentDate
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
                slug TEXT,
                instance INTEGER,
                display_name TEXT,
                name TEXT,
                short_name TEXT,
                sortable_name TEXT,
                TITLE INTEGER,
                SUBTITLE TEXT,
                CHAPTER TEXT,
                SUBCHAP TEXT,
                PART TEXT,
                PRIMARY KEY (slug, instance)
            )
        ''')

        # Create Analysis table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis (
                slug TEXT,
                instance, INTEGER,
                year INTEGER,
                word_count INTEGER,
                PRIMARY KEY (slug, instance, year)
            )
        ''')

        # Populate Agency table
        agencies = get_agencies()
        uniqueTitles = []

        if isinstance(agencies, dict):  # Check if it's a dictionary
            for agency in agencies['agencies']:
                i = 0
                for instance in agency.get('cfr_references'):
                    i += 1
                    # collect unique list of titles along the way
                    title = instance.get('title',None)
                    if title is not None and title not in uniqueTitles:
                        uniqueTitles.append(title)
                    insertString = "INSERT or IGNORE INTO agency (slug, instance, display_name, name, short_name, TITLE, SUBTITLE, CHAPTER, SUBCHAP, PART, sortable_name) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
                    cursor.execute(insertString, (agency.get('slug',None),i,agency.get('display_name',None),agency.get('name',None),agency.get('short_name',None),instance.get('title',None),instance.get('subtitle',None),instance.get('chapter',None),instance.get('subchapter',None),instance.get('part',None),agency.get('sortable_name',None)))
                    for year in range(yearMin, yearMax + 1):   
                        insertAnalysisString = "INSERT or IGNORE INTO analysis (slug, instance, year) VALUES (?,?,?)"
                        cursor.execute(insertAnalysisString, (agency.get('slug',None), i, year))
                for child in agency.get('children'):
                    for instance in child.get('cfr_references'):
                        i += 1
                        # collect unique list of titles along the way
                        title = instance.get('title',None)
                        if title is not None and title not in uniqueTitles:
                            uniqueTitles.append(title)
                        insertString = "INSERT or IGNORE INTO agency (slug, instance, display_name, name, short_name, TITLE, SUBTITLE, CHAPTER, SUBCHAP, PART, sortable_name) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
                        cursor.execute(insertString, (agency.get('slug',None),i,agency.get('display_name',None),agency.get('name',None),agency.get('short_name',None),instance.get('title',None),instance.get('subtitle',None),instance.get('chapter',None),instance.get('subchapter',None),instance.get('part',None),agency.get('sortable_name',None)))
                        for year in range(yearMin, yearMax + 1):   
                            insertAnalysisString = "INSERT or IGNORE INTO analysis (slug, instance, year) VALUES (?,?,?)"
                            cursor.execute(insertAnalysisString, (agency.get('slug',None), i, year))

        conn.commit()

        # Use cache of files - better for storage
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

        # Try to add recent data
        for title in uniqueTitles:
            date = recentDate
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

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    download_data()