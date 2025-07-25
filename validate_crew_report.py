import json
import jsonschema
from jsonschema import validate
import argparse

# Set up command-line arguments for flexibility
parser = argparse.ArgumentParser(description="Validate JSON reports against a schema.")
parser.add_argument("--schema", default="report_schema.json", help="Path to the schema file (default: report_schema.json)")
parser.add_argument("--data", default="sample_report.json", help="Path to the JSON data file to validate (default: reports.json)")
args = parser.parse_args()

# Load schema
try:
    with open(args.schema, 'r', encoding='utf-8') as f:
        schema = json.load(f)
except FileNotFoundError:
    print(f"Error: Schema file '{args.schema}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in schema file - {e}")
    exit(1)

# Load JSON data to validate (can be a single object or an array of report objects)
try:
    with open(args.data, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]  # Wrap single object in a list
    elif not isinstance(data, list):
        print("Error: Data file must contain a JSON object or an array of reports.")
        exit(1)
except FileNotFoundError:
    print(f"Error: Data file '{args.data}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in data file - {e}")
    exit(1)

# Validate each item in the list
for i, item in enumerate(data):
    try:
        validate(instance=item, schema=schema)
        print(f"Report {i+1}: VALID")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Report {i+1}: INVALID - {e.message}")