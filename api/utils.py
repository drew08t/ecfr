import xml.etree.ElementTree as ET
import re
import os
from typing import Optional, Dict, List,Union

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


def parse_xml_by_div_raw_xml(
    xml_input: str,
    div_number: Optional[int] = None,
    attributes: Optional[Dict[str, str]] = None,
    is_file_path: bool = True
) -> Optional[str]:
    """
    Parse XML from file path or string and return a string with raw XML content 
    including tags from DIV elements.
    
    Args:
        xml_input (str): Path to XML file or XML string content
        div_number (int, optional): Specific DIV number to match (e.g., 3 for DIV3)
        attributes (dict, optional): Dictionary of attribute key-value pairs to match
        is_file_path (bool): True if xml_input is a file path, False if it's an XML string
        
    Returns:
        String with full XML markup of matching elements, separated by newlines,
        or None if no matches
    """
    try:
        # Parse the XML based on input type
        if is_file_path:
            tree = ET.parse(xml_input)
            root = tree.getroot()
        else:
            root = ET.fromstring(xml_input)
        
        # List to store raw XML strings
        xml_parts = []
        
        # Iterate through all elements
        for elem in root.iter():
            tag = elem.tag
            
            # Check if tag starts with 'DIV'
            if tag.startswith('DIV'):
                # Extract number from tag if present
                div_num = None
                if len(tag) > 3 and tag[3:].isdigit():
                    div_num = int(tag[3:])
                
                # Check if we should include this element
                should_include = True
                
                # Filter by specific DIV number if provided
                if div_number is not None and div_num != div_number:
                    should_include = False
                
                # Filter by attributes if provided
                if attributes and should_include:
                    should_include = all(
                        elem.get(attr) == value 
                        for attr, value in attributes.items()
                    )
                
                if should_include:
                    # Get full XML string for this element including tags
                    raw_xml = ET.tostring(elem, encoding='unicode', method='xml').strip()
                    xml_parts.append(raw_xml)
        
        # Join all parts with newlines
        return '\n'.join(xml_parts) if xml_parts else None
        
    except FileNotFoundError:
        print(f"Error: File '{xml_input}' not found")
        return None
    except ET.ParseError:
        print(f"Error: Invalid XML format in input")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return None


def parse_xml_by_nested_attributes(
        

    xml_input: str,
    attribute_sets: List[Dict[str, str]],
    div_number: Optional[int] = None,
    is_file_path: bool = True
) -> Optional[str]:
    """
    Parse XML by applying multiple attribute filters sequentially, drilling down through
    the results with each set of attributes.
    
    Args:
        xml_input (str): Path to XML file or XML string content
        attribute_sets (List[Dict]): List of attribute dictionaries to match sequentially
        div_number (int, optional): Specific DIV number to match (e.g., 3 for DIV3)
        is_file_path (bool): True if xml_input is a file path, False if it's an XML string
        
    Returns:
        String with full XML markup of final matching elements, separated by newlines,
        or None if no matches remain after any iteration
    """
    # Initial result is either the full input or None
    current_input = xml_input
    
    # Process each attribute set sequentially
    for attributes in attribute_sets:
        # Call the base parsing function with current input
        result = parse_xml_by_div_raw_xml(
            current_input,
            div_number=div_number,
            attributes=attributes,
            is_file_path=is_file_path
        )
        
        # If no matches at any point, return None
        if not result:
            return None
        
        # Wrap the result in a root element to make it valid XML for next iteration
        current_input = f"<root>\n{result}\n</root>"
        is_file_path = False  # Subsequent iterations use string input
    
    return result
