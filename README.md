# System Report

A lightweight Python tool that collects and presents key system information in one place.  
Designed as a practical diagnostics and learning project, with a focus on clean structure and scalability.

## Features (Current)
- Retrieves the currently logged-in user
- Detects the operating system (raw identifier and human-friendly alias)
- Collects system information in a single snapshot object
- Separate data collection from presentation logic

## Project Structure
- `system_report.py` — core logic and reporting
- `SystemReport` class — stores a snapshot of system information
- Getter functions — responsible for individual data collection tasks
- Reporting functions — handle output and presentation

## Design Goals
- Clear separation of concerns
- Cross-platform compatibility (Windows, macOS, Linux)
- Incremental extensibility (networking, hardware, sensors)
- Readable, maintainable Python code

## Planned Features
- Hostname / computer name
- OS version and architecture
- CPU model and core count
- Memory and disk usage
- Network interfaces (IP and MAC addresses)
- Optional export formats (JSON / text)

## Usage
```bash
python system_report.py
