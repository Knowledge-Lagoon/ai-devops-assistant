# Incident Analyzer Module

## Overview

The `incident_analyzer` module is responsible for analyzing logs and generating incident reports using the Retrieval-Augmented Generation (RAG) pipeline. It extracts significant events from logs, analyzes them, and provides actionable insights for troubleshooting.

## Features

1. **Log Parsing**:
   - Extracts significant events from logs using predefined error keywords.
   - Supports filtering and summarizing logs for relevant information.

2. **Incident Analysis**:
   - Analyzes extracted log events to determine:
     - Incident type
     - Severity
     - Likely root cause
     - Evidence
     - Recommended actions
   - Uses the RAG pipeline to retrieve relevant context from the knowledge base.

3. **Integration with RAG**:
   - Leverages the `ask_with_rag` function to query the knowledge base and generate detailed incident reports.

## Key Components

### `parser.py`
- **Purpose**: Parses logs to extract significant events.
- **Functions**:
  - `extract_events(log_text: str) -> list[str]`: Extracts lines containing error keywords.
  - `summarize_log(log_text: str) -> dict`: Summarizes the log by counting events and providing a list of detected issues.

### `analyzer.py`
- **Purpose**: Analyzes extracted log events and generates incident reports.
- **Functions**:
  - `analyze(log_events: list[str]) -> str`: Uses the RAG pipeline to analyze log events and generate a report.

### `prompts.py`
- **Purpose**: Contains the prompt template for incident analysis.
- **Key Prompt**:
  - `INCIDENT_PROMPT`: Defines the structure and rules for generating incident reports.

## Usage

1. **Log Parsing**:
   - Use `extract_events` to parse logs and identify significant events.
   - Example:
     ```python
     from app.incident_analyzer.parser import extract_events
     log_text = "..."
     events = extract_events(log_text)
     print(events)
     ```

2. **Incident Analysis**:
   - Use `analyze` to generate an incident report based on extracted events.
   - Example:
     ```python
     from app.incident_analyzer.analyzer import analyze
     events = ["Error: Connection timeout", "Error: Unable to connect"]
     report = analyze(events)
     print(report)
     ```

## Dependencies

- `app.rag.chat`: Provides the `ask_with_rag` function for querying the knowledge base.
- `app.config`: Loads environment variables for configuration.

## Example Workflow

1. Parse logs using `parser.py` to extract significant events.
2. Analyze the extracted events using `analyzer.py` to generate an incident report.
3. Use the generated report to troubleshoot and resolve the issue.

## Future Enhancements

- Add support for more log formats.
- Enhance error keyword detection with machine learning models.
- Integrate with external monitoring tools for real-time analysis.

## Example Usage

Run the analyzer:
python -m app.incident_analyzer.analyzer