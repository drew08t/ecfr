from utils import count_words_in_xml, parse_xml_by_div_raw_xml, parse_xml_by_nested_attributes
    # examples to check
    # title 1, chapter 3: Administrative Conference of the United States - 12.36k words
    # title 1, chapter IV, part 425: President's Commission on White House Fellowships - 1.43k words
    # title 32, chapter XIX: Central Intelligence Agency - 30.62K words
    # title 22, chapter XIV, subchapter C: General Counsel of the Federal Labor Relations Authority - 20.5k
    # title 36, chapter IV: American Battle Monuments Commission - 12.43K
    # title 1, chapter IV, part 500: Employment Policy, National Commission for - 3.6k
    # title 48, subtitle A, chapter 10, subchapter A, Secretary of the Treasury, Office of
    # title 5, subtitle A, chapter LIII: Special Education and Rehabilitative Services, Office of
    # title 41, subtitle D, chapter 201: Federal Acquisition Security Council - 5.62k
    # title 22, chapter XIV, subchapter D: Foreign Service Impasse Disputes Panel - 8.65k TODO does not match?


search = {'TYPE': 'CHAPTER', 'N': 'IV', 'TYPE': 'PART', 'N': '425' }
print(count_words_in_xml(parse_xml_by_div_raw_xml('./cache/2024-12-31_1',None,search)))

search = {'TYPE': 'CHAPTER', 'N': 'XIX' }
print(count_words_in_xml(parse_xml_by_div_raw_xml('./cache/2024-12-31_32',None,search)))

searchAttributes = [{'TYPE': 'CHAPTER', 'N': 'XIV' },{'TYPE': 'SUBCHAP', 'N': 'C'}]
print(count_words_in_xml(parse_xml_by_nested_attributes('./cache/2024-12-31_22',searchAttributes,None,True)))

search = {'TYPE': 'CHAPTER', 'N': 'IV'}
print(count_words_in_xml(parse_xml_by_div_raw_xml('./cache/2024-12-31_36',None,search)))

searchChapter = {'TYPE': 'CHAPTER', 'N': 'IV', }
rawChapter = parse_xml_by_div_raw_xml('./cache/2024-12-31_1',None,searchChapter)
searchSubChapter = {'TYPE': 'PART', 'N': '500'}
rawSubChapter = parse_xml_by_div_raw_xml(rawChapter,None,searchSubChapter,False)
print(count_words_in_xml(rawSubChapter))

searchAttributes = [{'TYPE': 'SUBTITLE', 'N': 'D' },{'TYPE': 'CHAPTER', 'N': '201'}]
print(count_words_in_xml(parse_xml_by_nested_attributes('./cache/2024-12-31_41',searchAttributes,None,True)))

searchAttributes = [{'TYPE': 'CHAPTER', 'N': 'XIV' },{'TYPE': 'SUBCHAP', 'N': 'D'}]
print(count_words_in_xml(parse_xml_by_nested_attributes('./cache/2024-12-31_22',searchAttributes,None,True)))
