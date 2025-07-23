# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a standardized JSON schema and template project for documenting crew reports in space analog research missions (MDRS, HI-SEAS, etc.). The project enables structured data sharing and automated analysis across international analog stations.

## Key Files and Structure

- `crew_report_template.jsonc` - Human-readable template with comments (not valid JSON)
- `crew_report_template_strict.json` - Machine-parseable template without comments (use this for code)
- `report_schema.json` - JSON Schema validation rules for crew reports
- `validate_crew_report.py` - Python validation script
- `sample_report.json` - Example single report
- `reports.json` - Example batch of reports

## Common Commands

### Validation
- Validate default sample report: `python validate_crew_report.py`
- Validate custom file: `python validate_crew_report.py --data my_reports.json --schema report_schema.json`
- Validate batch reports: `python validate_crew_report.py --data reports.json`

### Dependencies
- Install required Python packages: `pip install jsonschema`

## Template Structure

The JSON template defines structured crew reports with:

**Required Fields:**
- `report_id`, `title`, `publish_date`, `author`, `station`, `mission_name`, `crew_number`, `mission_type`, `mission_start_date`, `mission_duration_day`, `report_date`, `report_type`, `content`

**Optional Fields:**
- `crew_members` (array), `categories`, `tags`, `objectives`, `outcomes`  
- `resource_usage`, `environmental_data`, `health_and_safety`, `metadata` (objects)

**Date Format:** All dates use ISO 8601 format (e.g., "2025-07-15T17:45:00Z")

**Content Field:** Supports free-form text including Markdown for rich formatting

## Validation Requirements

- All reports must validate against `report_schema.json`
- Use the validation script before committing changes to template files
- Single reports should be JSON objects; batch reports should be JSON arrays
- The `.jsonc` template file contains comments and is not valid JSON - use `crew_report_template_strict.json` for programmatic work

## Development Notes

- This is a data template project, not a software application
- Focus on JSON schema correctness and template usability
- The project aims for interoperability across different analog research stations
- Extensions should use the `metadata.custom` field for station-specific data