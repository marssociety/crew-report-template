# Crew Report JSON Template for Space Analog Missions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/marssociety/crew-report-template)](https://github.com/marssociety/crew-report-template/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/marssociety/crew-report-template)](https://github.com/marssociety/crew-report-template/network)
[![GitHub issues](https://img.shields.io/github/issues/marssociety/crew-report-template)](https://github.com/marssociety/crew-report-template/issues)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

A standardized JSON schema and template for documenting crew reports in space analog research missions, enabling structured data sharing, archival, and automated scientific analysis across international analog stations.

## Overview

This project provides a universal JSON template (`crew-report-template.json`) for crew reports from space analog missions, such as those at the Mars Desert Research Station (MDRS), Flashline Arctic Research Station, or other simulated environments. The template is designed to capture essential mission data in a consistent, machine-readable format, promoting interoperability and collaboration in the analog research community.

### Key Goals
- **Standardized Data Sharing**: Facilitate the exchange and archival of crew reports in a common format, reducing silos between analog stations and research teams.
- **Enabling Automation**: Support the development of tools for generating, searching, browsing, and analyzing reports—such as automated dashboards, AI-driven insights, or database integrations—to advance scientific research in space analogs.

Inspired by guidelines like the [International Guidelines and Standards for Space Analogs (IGSA)](https://analogstandards.space/), this template emphasizes flexibility for various mission types while ensuring key elements (e.g., health & safety, resource usage) are captured uniformly.

## Recent Changes
- **EVA Data Structure**: Added `eva_data` section with planned and actual waypoints, UTM coordinates, sample collection details, and field observations for comprehensive EVA tracking.
- **Report UUID Field**: Added `report_uuid` field using UUID v4 format for unique identification without requiring central authority coordination.
- **Equipment Assignment**: Added `equipment_assigned` array to crew members for tracking mesh radios, GPS units, and other equipment assignments per person.

## Features
- **JSON Template**: A sample report structure with required and optional fields for easy adoption.
- **Strict JSON Template**: `crew_report_template_strict.json` is a machine-parseable version of the template, with all comments removed.
- **JSON Schema**: Validation rules in `report_schema.json` to ensure data consistency.
- **Validation Script**: A Python script (`validate_crew_report.py`) for checking individual or batch reports against the schema.
- **Extensibility**: Optional fields and a `metadata` section for station-specific customizations.

## Installation

### Prerequisites
- Python 3.x (for the validation script)
- Required Python libraries: `jsonschema` (install via `pip install jsonschema`)

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/marssociety/crew-report-template.git
   cd crew-report-template
   ```

2. (Optional) Install dependencies for validation:
   ```
   pip install jsonschema
   ```

## Usage

### The Crew Report Template

There are two template files provided:

- **`crew_report_template_strict.json`**: This is a strict, machine-parseable JSON file with no comments. Use this as a starting point for creating your own reports or for programmatic processing.
- **`crew_report_template.jsonc`** (if present): This file contains the same structure but includes comments for human reference. It is not valid JSON and should not be used directly in code.

The template defines a JSON object for a single crew report. It includes:
- **Required Fields**: Essentials like `report_id`, `title`, `publish_date`, `author`, `station`, `mission_name`, `crew_number`, `mission_type`, `mission_start_date`, `mission_duration_day`, `report_date`, `report_type`, and `content`.
- **Optional Fields**: Arrays like `crew_members`, `categories`, `tags`; objects like `resource_usage`, `environmental_data`, `health_and_safety`, `metadata`; and strings like `objectives`, `outcomes`.
- **Formatting**: The `content` field supports free-form text, including Markdown for rich narratives (e.g., headings, lists, links).

Example snippet:
```json
{
  "report_id": "123",
  "title": "Sol Summary Report - July 15, 2025",
  "content": "# Full Report\n\n**Summary:** EVA successful.\n- Objective: Sample collection\n"
}
```

> **Note:** If you copy from `crew_report_template.json`, remove all comments before using in code or validation. For direct use, prefer `crew_report_template_strict.json`.

To create a report:
1. Copy the template and fill in your data.
2. Ensure dates use ISO 8601 format (e.g., "2025-07-15T17:45:00Z").
3. For batch reports, create an array of these objects in a file like `reports.json`.

### Validating Reports with the Schema and Script
Use the provided schema (`report_schema.json`) and validation script to ensure your JSON reports conform to the template.

#### Step 1: Prepare Your Data
- Individual report: Save as a single JSON object (e.g., `sample_report.json`).
- Batch reports: Use a JSON array (e.g., `reports.json`):
  ```json
  [
    { "report_id": "123", /* ... */ },
    { "report_id": "124", /* ... */ }
  ]
  ```

#### Step 2: Run the Validation Script
The script (`validate_crew_report.py`) checks reports against the schema. It supports command-line arguments for flexibility.

Example commands:
- Validate default file (`reports.json`):
  ```
  python validate_crew_report.py
  ```

- Validate a custom file:
  ```
  python validate_crew_report.py --data my_reports.json --schema report_schema.json
  ```

Output example:
```
Report 1: VALID
Report 2: INVALID - 'content' is a required property
```

If validation fails, review the error messages and adjust your JSON to match the schema (e.g., add missing required fields).

#### Why Validate?
Validation ensures reports are consistent, making them suitable for automated tools like search engines, data aggregators, or analysis scripts. This aligns with the project's goal of enabling community-wide data processing for scientific insights.

## Contributing
We welcome contributions from the analog research community! Whether it's schema enhancements, new examples, or tool integrations:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by and pending submission to the [International Guidelines and Standards for Space Analogs (IGSA)](https://analogstandards.space/).
- Built with open-source tools like JSON Schema and Python's `jsonschema` library.
- Thanks to the Mars Society and analog mission participants for their pioneering work.

For questions or feedback, open an issue or contact [jamesburk](https://github.com/jamesburk) - [Email](mailto:jburk@marssociety.org).
