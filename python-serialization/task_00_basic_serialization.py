#!/usr/bin/env python3
"""Basic JSON serialization/deserialization module."""

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Deserialize JSON file to recreate a Python dictionary.
    
    Args:
        filename (str): Name of the JSON file to load
        
    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
