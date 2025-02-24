import xml.etree.ElementTree as ET
import re
import os

def count_words_in_xml(xml_source):
    # Check if xml_source is likely a file path or XML string
    if os.path.exists(xml_source):  # If it's an existing file
        tree = ET.parse(xml_source)
        root = tree.getroot()
    else:
        # Assume it's an XML string if not a valid file path
        try:
            root = ET.fromstring(xml_source)
        except ET.ParseError as e:
            print(f"Invalid XML format: {e}")
            return None
    
    # Function to extract text content recursively
    def get_text(element):
        text_content = []
        if element.text:
            text_content.append(element.text.strip())
        for child in element:
            text_content.extend(get_text(child))
        if element.tail:
            text_content.append(element.tail.strip())
        return text_content
    
    # Get all text and count words
    all_text = ' '.join(get_text(root))
    words = re.findall(r'\b\w+\b', all_text.lower())
    return len(words)