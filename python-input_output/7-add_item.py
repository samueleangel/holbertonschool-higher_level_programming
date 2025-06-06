#!/usr/bin/python3
"""Script that adds command line arguments to a list and saves to JSON file."""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items or initialize empty list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
