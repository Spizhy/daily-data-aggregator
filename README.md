# Automated Daily Data Aggregator

## Overview
This project is an automated reporting pipeline built in Python. It eliminates the manual effort of gathering daily metrics by automatically extracting data from multiple sources (REST APIs and local CSVs), processing the data, generating a comprehensive PDF report with visualizations, and distributing it to stakeholders via email.

## Key Features
- **Automated Extraction:** Fetches daily metrics from configured REST APIs and CRM exports.
- **Data Transformation:** Cleans and aggregates data using `pandas`.
- **Visual Reporting:** Generates dynamic PDF reports with embedded charts using `matplotlib` and `ReportLab`.
- **Email Distribution:** Automatically dispatches the final report using the SMTP protocol.
- **Scheduling:** Designed to be run via cron jobs or Windows Task Scheduler.

## Tech Stack
- **Language:** Python 3.10+
- **Libraries:** `pandas`, `requests`, `matplotlib`, `reportlab`, `pytest`

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/daily-data-aggregator.git](https://github.com/yourusername/daily-data-aggregator.git)
