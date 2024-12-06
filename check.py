import xml.etree.ElementTree as ET
import os

def check_mappings(xml_file, json_file):
    if not os.path.exists(xml_file):
        print(f"Error: The file '{xml_file}' does not exist.")
        return

    if not os.path.exists(json_file):
        print(f"Error: The file '{json_file}' does not exist.")
        return

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML file '{xml_file}'. {e}")
        return

    xml_categories = set()
    for category in root.findall(".//category"):
        xml_categories.add(category.text.strip().split()[0])

    try:
        with open(json_file, 'r') as file:
            json_content = file.read()
    except Exception as e:
        print(f"Error: Failed to read JSON file '{json_file}'. {e}")
        return

    missing_categories = [category for category in xml_categories if category not in json_content]
    if missing_categories:
        print("The following categories are missing in the nistcsf2.0.json file:")
        for category in missing_categories:
            print(category)
    else:
        print("All categories are present in the nistcsf2.0.json file.")

xml_file = 'ref.xml'
json_file = 'nist-reference/nistcsf2.0.json'
check_mappings(xml_file, json_file)