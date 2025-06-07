#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json

def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file."""
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
        
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
