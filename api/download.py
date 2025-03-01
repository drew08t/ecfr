import sqlite3
from datetime import datetime

from api import get_agencies, get_title
from utils import flatten_json
import json

def create_database():
    try:
        # Connect to SQLite database (creates a new file if it doesn't exist)
        conn = sqlite3.connect('ecfr.db')
        cursor = conn.cursor()

        # Create Agency table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agency (
                slug TEXT PRIMARY KEY,
                display_name TEXT,
                name TEXT,
                short_name TEXT,
                sortable_name TEXT,
                title INTEGER,
                subtitle TEXT,
                chapter TEXT,
                subchapter TEXT,
                part TEXT
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
                insertString = "INSERT or IGNORE INTO agency (slug, display_name, name, short_name, title, subtitle, chapter, subchapter, part, sortable_name) VALUES (?,?,?,?,?,?,?,?,?,?)"
                cursor.execute(insertString, (agency.get('slug',None),agency.get('display_name',None),agency.get('name',None),agency.get('short_name',None),agency.get('title',None),agency.get('subtitle',None),agency.get('chapter',None),agency.get('subchapter',None),agency.get('part',None),agency.get('sortable_name',None)))

        conn.commit()
        print(uniqueTitles)

        # Create Title table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS title (
                title INTEGER,
                date TEXT,
                raw TEXT,
                PRIMARY KEY (title, date)
            )
        ''')

        # Populate Title table
        # Use cache of files instead - better for storage
        # Make sure missing queries aren't just timing out
        yearMin = 2016
        yearMax = 2024
        uniqueTitles.sort()
        for year in range(yearMin, yearMax + 1):
            for title in uniqueTitles:
                date = f'{year}-12-31'
                # TODO check if it exists before querying
                # Check if file exists in this case instead of querying the database
                titleResponse = get_title(date, title)
                
                print(title)
                print(date)
                insertString = "INSERT or IGNORE INTO title (title, date, raw) VALUES (?,?,?)"

                if (titleResponse is not None):
                    with open(f'./cache/{date}_{title}', "w") as file:
                        file.write(titleResponse.decode())
                    # cursor.execute(insertString, (title,date,titleResponse))
                    # conn.commit()

        # For each agency, parse appropriate title file for applicable content
        # Store content (maybe) in agency with metric calculations

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("Database connection closed.")

# Function to view some sample data
def view_sample_data():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        
        print("\nSample data from Products:")
        cursor.execute("SELECT * FROM products LIMIT 2")
        for row in cursor.fetchall():
            print(row)
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database()
    # view_sample_data()