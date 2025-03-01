import sqlite3
from api import get_agencies_db
from utils import count_words_in_xml, parse_xml_by_nested_attributes
from const import yearMin, yearMax, dbName


def analysis():
    try:
        # Connect to SQLite database (creates a new file if it doesn't exist)
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
            
        # Identifiers we are interested in:
        # DIV1 => TYPE="TITLE"
        # DIV2 => TYPE="SUBTITLE"
        # DIV3 => TYPE="CHAPTER"
        # DIV4 => TYPE="SUBCHAP"
        # DIV5 => TYPE="PART"
        mainIdentifier = 'TITLE'
        subIdentifiers = ['SUBTITLE', 'CHAPTER', 'SUBCHAP', 'PART']

        agencies = get_agencies_db()
        for agency in agencies:
            title = agency.get(mainIdentifier)
            slug = agency.get('slug')
            searchAttributes = []
            for id in subIdentifiers:
                agencyID = agency.get(id)
                if agencyID is not None:
                    searchAttributes.append({'TYPE': id, 'N': agencyID})
            for year in range(yearMin, yearMax + 1):   
                print(title, searchAttributes)
                try:
                    wordCount = count_words_in_xml(parse_xml_by_nested_attributes(f'./cache/{year}-12-31_{title}',searchAttributes,None,True))
                    insertAnalysisString = "INSERT or REPLACE INTO analysis (slug, year, word_count) VALUES (?,?,?)"
                    cursor.execute(insertAnalysisString, (slug, year, wordCount))
                except Exception as e:
                    print(e)
            conn.commit()

                
            # print(searchAttributes)
            # for year in range(yearMin, yearMax + 1):   
                
        # print(agencies) 
        # For each agency, parse appropriate title file for applicable content

        # Store content in analysis with metric calculations
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    analysis()