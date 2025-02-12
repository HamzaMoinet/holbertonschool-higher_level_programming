#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error occurred during serialization: {e}")
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {child.tag: child.text for child in root}
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None
